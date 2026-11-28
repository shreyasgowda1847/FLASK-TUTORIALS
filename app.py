from flask import Flask, request, render_template

app=Flask(__name__)
# @app.route('/')
# def hello_world():
#     name="shreyas"
#     age=12
#     place="maradahalli"
#     first="shreyas"
#     last=" raj"
#     price=10000
#     return render_template("index.html",name=name,age=age,place=place,first=first,last=last,price=price)
# @app.route("/about")
# def about():
#     return "About me"
# @app.route("/contact")
# def contact():
#     return "Contact me"
# """int  converter"""
# @app.route("/name/<int:age>")
# def name(age):
#     return f"your age {age}"
#
# """float  converter"""
# @app.route("/price/<float:amount>")
# def price(amount):
#     return f"your amount{amount}"
#
# """string(default)  converter"""
# @app.route("/view/<string:you>")
# def view(you):
#     return f"your name {you}"
#
# """UUID converter"""
# @app.route("/unique/<uuid:you>")
# def unique(you):
#     return f"UUID:{you}"
#
# """query arguments"""
# @app.route("/search")
# def search():
#     names=request.args.get("names","guest")
#     course=request.args.get("course","unknown")
#     return f"your name {names} course {course}"
# @app.route("/")
# def index():
#     is_logging=True
#     marks=80
#     return render_template("index.html",is_logging=is_logging,marks=marks)
@app.route("/")
def home():
    courses=["python","flask","ai/ml","ds"]
    student={"name":"shreyas","age":18,"course":"python"}
    return render_template("index.html",courses=courses,student=student)


if __name__=='__main__':
    app.run(debug=True)