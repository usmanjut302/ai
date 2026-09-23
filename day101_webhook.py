from flask import Flask,request
app=Flask(__name__)

@app.route("/webhook",methods=["POST"])
def webhook():
    data=request.json
    event=data["event"]
    customer=data["customer"]
    amount=data["amount"]
    if event=="payment_failed":
        print("Payment Failed detected ")
        print("Customer notification required")
        print("Amount: ",amount)
        print("Customer: ",customer)

    elif event=="payment_success":
        print("Payment success detected")
        print("Customer notification required")
        print("Amount: ",amount)
        print("Customer: ",customer)
    elif event=="order_created":
        print("new order received ")  
    else:
        print("unknown event")      

    return{"message":"webhook received"},200
if __name__=="__main__":
    app.run(debug=True)
    