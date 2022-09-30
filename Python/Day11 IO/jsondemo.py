import json

d = dict(name='Bob', age=20, score=88)

json_data = json.dumps(d)
print(json_data)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)