from flask import Flask, render_template, request
import nutritrack

app = Flask(__name__)

weights = []

# Dashboard page (home page)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Weight tracking page1

@app.route("/log_weight", methods=["GET", "POST"])
def log_weight():
    if request.method == "POST" and "weight" in request.form:
        weight = request.form["weight"]
        height = request.form["height"]
        sex = request.form["sex"]
        waist = request.form["waist"]
        neck = request.form["neck"]
        hip = request.form["hip"]
        nutritrack.weight_info(weight, height, sex, waist, neck, hip)
    return render_template("advice.html", advice_type="weight", advice = nutritrack.weightstate)


# Nutrition tracking page
@app.route("/log_nutrition", methods=["GET", "POST"])
def log_nutrition():
    if request.method == "POST" and "calories" in request.form:
        cal = request.form["calories"]
        pro = request.form["protein"]
        carb = request.form["carbs"]
        fat = request.form["fat"]
        sugars = request.form["sugars"]
        sodium = request.form["sodium"]
        serving = request.form["serving"]

        nutritrack.add_food(cal, pro, carb, fat, sugars, sodium, serving)
        nutritrack.check_nut()
    return render_template("advice.html", advice_type="nutrition", foods=nutritrack.foods, advice=nutritrack.advice)

if __name__ == "__main__":
    app.run(debug=True)
#new