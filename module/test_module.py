from flask import Blueprint, render_template, request

test_module = Blueprint("test_module", __name__)

@test_module.route("/result", methods=["POST"])
def test_result():
    input_license = request.form['input_license']
    if input_license=="2009":
        check = "Online"
    else:
        check = "Offline"
    return render_template("test_result.html", license=input_license, check_license=check)

