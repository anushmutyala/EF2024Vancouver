# from flask import Flask, request, jsonify
from quart import Quart, request, jsonify
from supabase import create_client, Client
from openai import OpenAI
from .helpers import *
import asyncio
# Initialize Flask app
# app = Flask(__name__)

# Initialize Quart app
app = Quart(__name__)

# Supabase configuration
SUPABASE_URL = "https://hcrkjwcuigvggxkipdsj.supabase.co/"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imhjcmtqd2N1aWd2Z2d4a2lwZHNqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzY2MjY0ODMsImV4cCI6MjA1MjIwMjQ4M30.QvVRnjvDNdSIPJ07kwApwcVN28He-M1uJjhMFaTrFkk"

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
openai_client = OpenAI(api_key="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")

# global var to store latest base64 image
raw_img = None

@app.route('/')
async def home():
    # return jsonify({"message": "Supabase Flask Server is running!"})
    # return an html template from with the latest image in decoded_image_bytes, refreshes every 5 seconds
    global raw_img
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Supabase Flask Server</title>
        <meta http-equiv="refresh" content="5">
    </head>
    <body>
        <h1>Livestream</h1>
        <img src="data:image/png;base64,{raw_img}" alt="Latest Image" width="500" height="500">
    </body>
    </html>
    """

# Example route to fetch data from a Supabase table
# @app.route('/get_data', methods=['GET'])
# def get_data():
#     try:
#         table_name = request.args.get('table')  # Pass the table name as a query parameter
#         response = supabase.table(table_name).select("*").execute()
#         return jsonify(response.data)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

@app.route('/insert_frames', methods=['POST'])
async def insert_frames():
    global raw_img
    try:
    #     print(f"Request Headers: {request.headers}")
    #     print(f"Request Content-Type: {request.content_type}")
    #     print(f"Request Data: {request.data.decode('utf-8')}")
        # Parse the request body
        # data = request.json
        data = await request.get_json()  # Correctly await the JSON parsing
        raw_img = data.get("base64_img")  # base64 string

        # get the last img frame from the Frames table
        try:
            response = supabase.table("Frames").select("tools, action, id").order("id", desc=True).limit(1).execute()
            if len(response.data) == 0:
                prev_tools = None
                prev_action = None
                prev_id = -1
            else:
                prev_tools = response.data[0]['tools']
                prev_action = response.data[0]['action']
                prev_id = int(response.data[0]['id'])
            # get project description from Projects table
            response = supabase.table("Projects").select("description").execute()
            description_text = response.data[0]['description']
        except Exception as e:
            prev_tools = None
            prev_action = None
            prev_id = -1
        
        img_frame = getImageData(openai_client, raw_img, description_text, img_schema, prev_action, prev_tools)

        img_frame['id'] = prev_id + 1
        print('img_frame: ', img_frame)
        img_frame['raw_img'] = raw_img

        if img_frame['id'] % 5 == 0:
            asyncio.create_task(trigger_flowchart())

        # Validation (optional but recommended)
        # if not timestamp or not isinstance(tools, list) or not action or not raw_img:
        #     return jsonify({"error": "Invalid or missing fields"}), 400

        # Insert data into the Supabase table
        response = supabase.table("Frames").insert(img_frame).execute()

        return jsonify({"message": "Row inserted successfully", "data": response.data}), 201
        # return jsonify({"message": "success"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Example route to update data in a Supabase table
# @app.route('/update_data', methods=['PUT'])
# def update_data():
#     try:
#         table_name = request.json.get('table')
#         query_filter = request.json.get('filter')  # Conditions for update
#         updates = request.json.get('updates')  # Fields to update
#         response = (
#             supabase.table(table_name)
#             .update(updates)
#             .eq(query_filter['key'], query_filter['value'])
#             .execute()
#         )
#         return jsonify({"message": "Data updated successfully!", "response": response.data})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# Example route to delete data from a Supabase table
# @app.route('/delete_data', methods=['DELETE'])
# def delete_data():
#     try:
#         table_name = request.json.get('table')
#         query_filter = request.json.get('filter')  # Conditions for deletion
#         response = (
#             supabase.table(table_name)
#             .delete()
#             .eq(query_filter['key'], query_filter['value'])
#             .execute()
#         )
#         return jsonify({"message": "Data deleted successfully!", "response": response.data})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# Function to trigger the summary API route
async def trigger_flowchart():
    try:
        # retrieve all images from the Frames table
        # response = supabase.table("Frames").select("*").execute()
        # print('response: ', len(response.data))

        # retrieve all image frames from the Frames table, specifically 'tools', 'actions' and 'id' columns
        response = supabase.table("Frames").select("tools, action, id").execute()
        # print('response: ', response.data)
        combined_img_frames = combine_img_frames(response.data)
        # print(combined_img_frames)
        steps = generate_steps(openai_client, combined_img_frames)
        # print('steps: ', steps)
        # response = supabase.table("Steps").insert(steps).execute()
        # rewrite the Steps table with the new steps
        response = supabase.table("Steps").upsert(steps).execute()

        return jsonify({"message": "Flowchart generated successfully", "data": response.data}), 201
        
    except Exception as e:
        print(f"Error triggering summary: {e}")

if __name__ == '__main__':
    app.run()
