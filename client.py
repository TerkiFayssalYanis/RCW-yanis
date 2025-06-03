import requests
 
#url = "http://localhost:8000/"
url="https://rcw-yanis-dpbyahgrf9bvafdk.canadaeast-01.azurewebsites.net/test"
response = requests.get(url)
response = response.json()
print(response['message'])