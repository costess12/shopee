import requests

url = "https://example.com/api"
data = {"key": "value"}
headers = {"Content-Type": "application/json"}

# Enviar uma requisição POST
response = requests.post(url, json=data, headers=headers)

# Exibir a resposta
print(f"Status: {response.status_code}")
print(f"Resposta: {response.text}")
