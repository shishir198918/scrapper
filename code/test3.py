from flask import Flask,request

page=Flask(__name__)

@page.route("/url_p1/",methods=["GET","POST"])
def d1():
    if request.method=="GET":

        num1=request.args.get("marks",type=int)
        roll=request.args.get("rollno",type=str)
        return f"{num1},{roll}"