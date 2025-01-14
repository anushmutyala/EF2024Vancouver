from flask import Flask, request, jsonify
from supabase import create_client, Client
import json

# Initialize Flask app
app = Flask(__name__)

# Supabase configuration
SUPABASE_URL = "https://hcrkjwcuigvggxkipdsj.supabase.co/"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imhjcmtqd2N1aWd2Z2d4a2lwZHNqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzY2MjY0ODMsImV4cCI6MjA1MjIwMjQ4M30.QvVRnjvDNdSIPJ07kwApwcVN28He-M1uJjhMFaTrFkk"

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def home():
    return jsonify({"message": "Supabase Flask Server is running!"})

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
def insert_frames():
    try:
        # Parse the request body
        data = request.json
        # timestamp = data.get("timestamp")
        tools = data.get("tools")  # List of text
        action = data.get("action")
        raw_img = data.get("raw_img")  # JSON object 

        # tools = ["huzz", "bruzz"]
        # action = "ts(this) nod tuff"
        # raw_img is a json binary
        # raw_img = "visiduzz"

        # Validation (optional but recommended)
        # if not timestamp or not isinstance(tools, list) or not action or not raw_img:
        #     return jsonify({"error": "Invalid or missing fields"}), 400

        # Insert data into the Supabase table
        response = supabase.table("Frames").insert({
            # "timestamp": timestamp,
            "tools": tools,
            "action": action,
            "raw_img": raw_img
        }).execute()

        return jsonify({"message": "Row inserted successfully", "data": response.data}), 201

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
