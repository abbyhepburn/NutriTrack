foods = []
def add_food(calories, protein, carbs, fat, sugar, sodium, serving):
    foods.append((float(calories), float(protein), float(carbs), float(fat), float(sugar), float(sodium), int(serving)))
    return f"Logged ({calories} cal, {protein}g Protein, {carbs}g Carbs, {fat}g Fats), {sugar}g Added Sugars, {sodium}g Sodium, {serving} Servings of Fruits/Vegs"
advice = []
def check_nut():
    advice.clear()
    last = foods[-1]
    calories = last[0]
    protein = last[1]
    if protein < 45:
        advice.append("Low protein try eating more eggs ")
    elif protein > 120:
        advice.append("High protein ")
    else:
        advice.append("Protein is on track")
    carbs = last[2]
    if carbs < 130:
        advice.append("Low carbs try eating more bread ")
    elif carbs > 300:
        advice.append("High carbs ")
    else:
        advice.append("Carbs is on track")
    fat = last[3]
    targetf = calories * .3
    if fat > targetf:
        advice.append("Too many fats ")
    else:
        advice.append("Good Fats")
    sugars = last[4]
    targets = calories * .1
    if sugars > targets:
        advice.append("Too much sugar")
    else:
        advice.append("Good Sugar")
    sodium = last[5]
    if sodium > 5:
        advice.append("Too much sodium ")
    else:
        advice.append("Sodium is on track")
    serving = last[6]
    if serving < 5:
        advice.append("Not enough fruits and vegetables ")
    else:
        advice.append("Good")
    return advice
#add_food(1000,155,60,35,2,3,4)
#print(check_nut())
