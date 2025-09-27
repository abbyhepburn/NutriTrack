from flask import Flask, render_template, request
import nutrition

app = Flask(__name__)


# Optional: store weights if you have weight logging
weights = []


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        # Check if this is weight input or nutrition input
        if "weight" in request.form:
            weight = request.form["weight"]
            weights.append(float(weight))
            message = f"Logged weight: {weight} kg"

        elif "calories" in request.form:
            # get nutrition form inputs
            cal = request.form["calories"]
            pro = request.form["protein"]
            carb = request.form["carbs"]
            fat = request.form["fat"]
            sugar = request.form["sugar"]
            sodium = request.form["sodium"]
            serving = request.form["serving"]

            # log nutrition
            nutrition.add_food(cal, pro, carb, fat, sugar, sodium, serving)

            # check nutrition and generate advice
            nutrition.check_nut()

    return render_template("index.html",
                           weights=weights,
                           foods=nutrition.foods,
                           advice=nutrition.advice)


if __name__ == "__main__":
    app.run(debug=True)
