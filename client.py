import requests
 
#url = "http://localhost:8000/"
url="https://appapiaziz-g9cwbtg8gtfthqcu.canadaeast-01.azurewebsites.net/test"
response = requests.get(url)
response = response.json()
print(response['message'])