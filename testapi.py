import requests 

response = requests.post("http://localhost:5000/", files = {'file': open('d.jpg','rb')})

print(response.text)