curl -X POST http://172.18.224.1:5000/insert_frames \
-H "Content-Type: application/json" \
-d '{
  "timestamp": "2025-01-13T12:34:56.789Z",
  "tools": ["tool1", "tool2", "tool3"],
  "action": "Example Action",
  "raw_img": {
    "key1": "value1",
    "key2": "value2"
  }
}'