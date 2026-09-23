webhook_data = {
    "event": "payement_failed",
    "customer": "ali",
    "product": "Phone",
    "amount": 45000
}

# print(webhook_data)
event=webhook_data["event"]
customer=webhook_data["customer"]
product=webhook_data["product"]
amount=webhook_data["amount"]

print("Event: ",event)
print("Customer: ",customer)
print("Product: ",product)
print("Amount: ",amount)

if event=="payment_failed":
    print("Payment failed detected")
    print("Customer notification required ....")


