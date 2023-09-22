from flask import request, render_template, Flask, jsonify
from password_evaluator import password_advisor


app = Flask(__name__, template_folder="templates")
app.static_folder = 'static'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/validate_password", methods=["POST"])
def validate_password():
    data = request.get_json()
    pwd = data.get("password")

    pwd_condition, pwd_issues = password_advisor(pwd)

    if not pwd_issues:
        return jsonify({"message": pwd_condition, "issues": ""}), 200
    else:
        return jsonify({"message": "Password is weak! It is highly recommended to strengthen your password.", "issues": pwd_issues}), 200



if __name__ == "__main__":
    app.run(debug=True)
