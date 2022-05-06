import requests
#1
response_1 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response_1.text, response_1.status_code)

#2
response_2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"HEAD"})
print(response_2.text, response_2.status_code)

#3
response_3 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
print(response_3.text, response_3.status_code)

#4
type_request = ["post", "put", "delete"]
method_list = [{"method":"GET"}, {"method":"POST"}, {"method":"PUT"}, {"method":"DELETE"}]

for a in type_request:
    for param in method_list:
        response = getattr(requests, a)("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        if response.status_code == 200:
            print(f"method {a} - {param} - {response.status_code} - {response.text}")

type_request = ["get"]
method_list = [{"method":"GET"}, {"method":"POST"}, {"method":"PUT"}, {"method":"DELETE"}]

for a in type_request:
    for param in method_list:
        response = getattr(requests, a)("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        if response.status_code == 200:
            print(f"method {a} - {param} - {response.status_code} - {response.text}")







