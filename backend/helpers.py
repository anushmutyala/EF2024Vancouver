# all imports 

import base64
import json
import re
# from supabase import create_client, Client

# client = OpenAI(api_key="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")

# per img schema -> img_idx will be inserted after openai call
img_schema = """{
    "tools": [list of tools in use in this image],
    "action": action/operation being performed in this image, should be in jot form where every new point starts with a '* ',
    "id": idx of img in Frames table, will always be ordered sequentially in order of when the img was taken 
}"""

#per step schema 
step_schema = """{
    "id": idx of step in Steps table, will always be ordered sequentially in order of when the step was taken
    "title": Step title,
    "progression": what progress is being made in this step,
    "substeps": [list of ids of image frames from Frames table that are part of this step (min 1, max 3 substeps per step -> if exceeding max substep limit, create new steps)],
}"""

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  

def getImageData(client, base64_image, description_text, target_schema, action_context=None, tool_context=None):
    #handling the text description passed in
    if description_text and action_context:
        text = "I am currently working on: {description_text}. For context, the action/operation done prior to this was: {action_context}. Additionally, the tools used were: {tool_context}. Based on the description I gave you as well the context of the task before this, generate a json schema in the format provided that encapsulates this step in a manufacturing procedure: {schema}".format(
           description_text=description_text, 
           action_context=action_context, 
           schema=target_schema, 
           tool_context=tool_context
           )
    else:
        text = "I am currently working on: {description_text}. Based on this image (first of the project) as well the context of this project generate a json schema in the format provided that encapsulates this step in a manufacturing procedure: {schema}".format(description_text=description_text, schema=target_schema)

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", 
            "content": "You are part of an application that helps engineers document their manufacturing process. By analyzing images throughout their workday, you will integrate into an application that generates a flowchart of the step by step procedure for their project."
        },
        {
            "role": "user",
            "content": [
                    {
                        "type": "text", 
                        "text": text,
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{base64_image}"},
                    },
        ],
        }
    ],
    max_tokens=300
    )
    
    # print("response choice", response.choices)
    # data.append(response.choices)
    
    json_str = re.search(r'```json\n(.*?)\n```', response.choices[0].message.content, re.DOTALL).group(1)
   
    json_data = json.loads(json_str)
    
    # json_data["raw_img"] = base64_image
    
    return json_data

def combine_img_frames(res):
    string_img_data = [] # jsons of image frames and metadata -> will follow schema 2
    for img_data in res:
        string_img_data.append(json.dumps(img_data))

    # print(string_img_data[0])

    # merge all image data into one text blob
    combined_img_data = ""
    for img_data in string_img_data:
        combined_img_data += img_data

    return combined_img_data

def generate_steps(client, img_frames):
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", 
            "content": "You are part of an application that helps engineers document their build process. By analyzing images throughout their workday, you will integrate into an application that generates a flowchart of the step by step procedure for their project."
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": """
                    I now have an array of objects per image captured that were taken while I was working through the project that follows the schema below: 
                    {}
                    Here are the combined image objects:
                    {}
                    Your task is to consolidate all the image objects and make a logical timeline by grouping together image objects into steps.
                    Please generate a new json object that captures all the steps in the timeline in the schema format provided:
                    {}
                    """.format(img_schema, img_frames, step_schema),
                }
        ],
        }
    ],
    max_tokens=600,
    )

    print(response.choices[0].message.content)
    # json_str = re.search(r'```(?:json)?\n(.*?)\n```', response.choices[0].message.content, re.DOTALL).group(1)
    # json_str = re.search(r'```json\n(.*?)\n```', response.choices[0].message.content, re.DOTALL).group(1)

    # Simulated response from the API
    response_content = response.choices[0].message.content

    # Regular expression to capture JSON between triple backticks
    match = re.search(r'```json\n(.*?)\n```', response_content, re.DOTALL)

    if match:
        # Extract the JSON string
        json_str = match.group(1)

        try:
            # Parse the JSON string
            json_data = json.loads(json_str)
            print("Extracted JSON object:", json_data)

            # You can now append the JSON data to the steps list or use it elsewhere
            steps = json_data
        except json.JSONDecodeError as e:
            print("Failed to parse JSON:", e)
    else:
        print("No JSON found in the response. Here is the raw response:")
        print(response_content)
    
    return steps



