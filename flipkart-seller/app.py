from flask import Flask,render_template,request
import requests
import sqlite3 as sql
import json

app=Flask(__name__)
@app.route('/',methods=["POST","GET"])
def home():
    if request.method=="POST":
        image=request.form.get("image")
        product_name=request.form.get("product_name")
        description=request.form.get("description")
        price=request.form.get("price")
        quantity=request.form.get("quantity")
        dict_1={}
        dict_1.update({"image":image})
        dict_1.update({"product_name":product_name})
        dict_1.update({"description":description})
        dict_1.update({"price":price})
        dict_1.update({"quantity":quantity})
        url="http://127.0.0.1:5000/api"
        response=requests.post(url,json=dict_1)
        return{"data":"response"}
    return render_template("form.html")

if __name__=="__main__":
    app.run(debug=True,port=5001)