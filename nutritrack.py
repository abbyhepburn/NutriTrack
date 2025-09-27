foods = []
def add_food(calories, protein, carbs, fat, sugar, sodium, serving):
    foods.append((float(calories), float(protein), float(carbs), float(fat), float(sugar), float(sodium), int(serving)))
    return f"Logged ({calories} cal, {protein}g Protein, {carbs}g Carbs, {fat}g Fats), {sugar}g Added Sugars, {sodium}g Sodium, {serving} Servings of Fruits/Vegs"
advice = []
def check_nut():
    advice.clear()
    diff = 0
    last = foods[-1]
    calories = last[0]
    protein = last[1]
    if protein < 45:
        diff = 45 - protein
        advice.append(f"Your protein {diff}g below the minimum recommended daily intake! Try including protein in each meal through high-protein foods like eggs, chicken, turkey, fish, Greek yogurt, lentils, chickpeas, and tofu. ")
    elif protein > 120:
        diff = protein - 120
        advice.append(f"Your protein is {diff}g above the maximum recommended daily intake! Consider balancing your diet by reducing protein-rich foods and adding more fruits, vegetables, and whole grains. ")
    else:
        advice.append("Great job! Your protein intake is on track. Keep including a variety of protein sources in your meals to maintain a balanced diet.")
    carbs = last[2]
    if carbs < 130:
        diff = 130 - carbs
        advice.append(f"Your carbohydrate intake {diff}g below the minimum recommended daily intake! Include more whole grains, fruits, and vegetables.")
    elif carbs > 300:
        diff = carbs - 300
        advice.append(f"Your carbohydrate intake is {diff}g above the maximum recommended daily intake! Try to limit refined carbs and focus on whole grains and vegetables.")
    else:
        advice.append("Your carbohydrate intake is on track. Keep balancing whole grains, fruits, and vegetables.")
    fat = last[3]
    targetf = calories * .3
    if fat > targetf:
        diff = fat - targetf
        advice.append(f"Your fat intake is {diff}g above the recommended intake! Focus on healthy fats like nuts, seeds, and olive oil, and reduce fried foods.")
    else:
        advice.append("Good job! Your fat intake is within the recommended range.")
    sugars = last[4]
    targets = calories * .1
    if sugars > targets:
        diff = sugars - targets
        advice.append(f"Your added sugar intake is {diff}g over the recommended daily intake! Try reducing sweets, sugary drinks, and processed foods.")
    else:
        advice.append("Sugar intake is on track. Keep it balanced!")
    sodium = last[5]
    if sodium > 5:
        diff = sodium - 5
        advice.append(f"Your sodium intake is {diff}g over the recommended daily intake! Try to reduce salty foods and processed meals.")
    else:
        advice.append("Sodium intake is on track. Great job!")
    serving = last[6]
    if serving < 5:
        diff = 5-serving
        advice.append(f"Not enough fruits and vegetables! Aim for at least 5 servings per day, right now you are {diff} below that.")
    else:
        advice.append("Great! You’re getting enough fruits and vegetables.")
    return advice
#add_food(1000,155,60,35,2,3,4)
#print(check_nut())
