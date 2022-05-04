import json

string_as_json = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
data = json.loads(string_as_json)
print(data['messages'][1]['message'])