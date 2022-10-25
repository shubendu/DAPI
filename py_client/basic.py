import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, params={"abc":"123"}, json={"query":"Hello World"})

# print(get_response.text)  #not proper dictionary
print(get_response.json()) #proper python dictionary

# print(get_response.status_code)



#HTTP request --> HTML
#REST API HTTP --> JSON

