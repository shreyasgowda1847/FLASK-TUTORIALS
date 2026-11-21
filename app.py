from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello home!'
@app.route("/about")
def about():
    return "About me"
@app.route("/contact")
def contact():
    return "Contact me"
if __name__=='__main__':
    app.run(debug=True)