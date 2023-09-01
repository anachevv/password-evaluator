from flask import request, render_template, Flask
from password_evaluator import password_advisor


app = Flask(__name__, template_folder="templates")
app.static_folder = 'static'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_password", methods=["POST"])
def get_password():
    pwd = request.form["user_input"]
    result = password_advisor(pwd)
    
    return result

if __name__ == "__main__":
    app.run(debug=True)
