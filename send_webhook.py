import requests
url="http://127.0.0.1:5000/webhook"
webhook_data={
    "event":"payment_failed",
    "customer":"Usman",
    "product":"Phone",
    "amount":45000
    }
response=requests.post(url,json=webhook_data)
print(response.json())
print(response.status_code)