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
    pwd_condition = password_advisor(pwd)[0]
    pwd_issues = password_advisor(pwd)[1]

    return render_template("get_password.html", pwd_condition=pwd_condition, pwd_issues=pwd_issues)


if __name__ == "__main__":
    app.run(debug=True)
