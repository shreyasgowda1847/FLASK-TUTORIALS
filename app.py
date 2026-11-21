from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello Man!'
@app.route("/about")
def about():
    return "About me"
@app.route("/contact")
def contact():
    return "Contact me"
@app.route("/users")
def users():
    return "Users page"
@app.route("/user/<username>")
def user(username):
    return f"heloo {username}"
if __name__=='__main__':
    app.run(debug=True)