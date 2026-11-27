from flask import Flask, request, render_template

app=Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route("/about")
def about():
    return "About me"
@app.route("/contact")
def contact():
    return "Contact me"
"""int  converter"""
@app.route("/name/<int:age>")
def name(age):
    return f"your age {age}"

"""float  converter"""
@app.route("/price/<float:amount>")
def price(amount):
    return f"your amount{amount}"

"""string(default)  converter"""
@app.route("/view/<string:you>")
def view(you):
    return f"your name {you}"

"""UUID converter"""
@app.route("/unique/<uuid:you>")
def unique(you):
    return f"UUID:{you}"

"""query arguments"""
@app.route("/search")
def search():
    names=request.args.get("names","guest")
    course=request.args.get("course","unknown")
    return f"your name {names} course {course}"


if __name__=='__main__':
    app.run(debug=True)