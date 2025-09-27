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
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        sex = request.form["sex"]
        waist = float(request.form["waist"])
        neck = float(request.form["neck"])
        hip = float(request.form["hip"])
        nutritrack.weight_info(weight, height, sex, waist, neck, hip)
    return render_template("advice.html", advice_type="weight", advice = nutritrack.weightstate)


# Nutrition tracking page
@app.route("/log_nutrition", methods=["GET", "POST"])
def log_nutrition():
    if request.method == "POST" and "calories" in request.form:
        cal = float(request.form["calories"])
        pro = float(request.form["protein"])
        carb = float(request.form["carbs"])
        fat = float(request.form["fat"])
        sugars = float(request.form["sugars"])
        sodium = float(request.form["sodium"])
        serving = float(request.form["serving"])

        nutritrack.add_food(cal, pro, carb, fat, sugars, sodium, serving)
        nutritrack.check_nut()
    return render_template("advice.html", advice_type="nutrition", foods=nutritrack.foods, advice=nutritrack.advice)

if __name__ == "__main__":
    app.run(debug=True)
#new