import requests

headers = {
    "x-api-key": "pub_dfc7d0e839a03ff8a894f20631dc4df12b170219281599c4badf237020bb6aa0"
   }

response = requests.get("https://reqres.in/api/users/22", headers=headers)

print(response.status_code)
print(response.json())

