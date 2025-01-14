# all imports 

import base64
import os
# from openai import OpenAI
from PIL import Image
from ultralytics import YOLO, FastSAM
import matplotlib.pyplot as plt
import torch
import clip  # pip install git+https://github.com/openai/CLIP.git
import json
import re
import random
import datetime
from pprint import pprint
# from supabase import create_client, Client

# client = OpenAI(api_key="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")

# per img schema -> img_idx will be inserted after openai call
img_schema = """{
    "tools": ["list of tools in use in this image"],
    "action": "action/operation being performed in this image",
}"""

#per step schema 
step_schema = """{
    "title": "Step title",
    "progression": "what progress is being made in this step",
    "substeps": [ (some steps may just be independent, single substep)
        {
            "title": "Substep title",
            "tools": ["list of tools in use in this image"],
            "action": "action/operation being performed in this image",
            "img_idx": "idx of img in frames table"
        }
    ]
}"""

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  

def getImageData(client, base64_image, description_text, target_schema, action_context=None):
    #handling the text description passed in
    if description_text and action_context:
        text = "I am currently working on: {description_text}. For context, the action/operation done prior to this was: {action_context}. Based on the description I gave you as well the context of the task before this, generate a json schema in the format provided that encapsulates this step in a manufacturing procedure: {schema}".format(description_text=description_text, action_context=action_context, schema=target_schema)
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
    
    #print("resposne choice", response.choices)
    # data.append(response.choices)
    
    json_str = re.search(r'```json\n(.*?)\n```', response.choices[0].message.content, re.DOTALL).group(1)

    # Parse the extracted JSON string
    json_data = json.loads(json_str)
    # json_data["raw_img"] = base64_image
    
    return json_data

