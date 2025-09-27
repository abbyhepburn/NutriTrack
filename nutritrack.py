import math
weightstate=[]
def convert_weight(pounds):
    weight = pounds / 2.205
    return weight


def convert_height(inches):
    height = (inches * 0.0254) ** 2
    return height


def bmi_calculations(weight, height):
    status = ""
    user_bmi = convert_weight(weight) / convert_height(height)
    weightstate.append("Reminder: Your BMI is just a rough guideline, not a full picture of your "
          "health. Things like muscle, bone structure, and lifestyle aren’t included in this number, "
          "so don’t worry if your score isn’t exactly where you hoped. It doesn’t define you.")

    if user_bmi < 18.5:
        weightstate.append(f"According to your BMI of {round(user_bmi, 1)}, you are currently underweight.")
        status = "underweight"


    elif 18.5 <= user_bmi <= 24.9:
        weightstate.append(f"According to your BMI of {round(user_bmi, 1)}, you are currently within a normal weight.")
        status = "normal"


    elif 25 <= user_bmi <= 29.9:
        weightstate.append(f"According to your BMI of {round(user_bmi, 1)}, you are currently overweight.")
        status = "overweight"


    elif user_bmi >= 30:
        weightstate.append(f"According to your BMI of {round(user_bmi, 1)}, you are currently obese.")
        status = "obese"
    return status


def body_fat_calculations(height, sex, waist, neck, hip):

    if sex == "male":
        hip = 0
        bfp = 86.010 * (math.log((waist - neck), 10)) - 70.041 * (math.log(height, 10)) + 36.76 + hip
        bfp = round(bfp, 1)
        if 2 <= bfp < 5:
            bfp_status = "essential"
        elif 5 <= bfp < 13:
            bfp_status = "athletic"
        elif 13 <= bfp < 17:
            bfp_status = "fit"
        elif 17 <= bfp <= 24:
            bfp_status = "average"
        else:
            bfp_status = "overweight"
    else:  # female
        bfp = 163.205 * (math.log((waist + hip - neck), 10)) - 97.684 * (math.log(height, 10)) - 78.38
        bfp = round(bfp, 1)
        if 10 <= bfp < 14:
            bfp_status = "essential"
        elif 14 <= bfp < 20:
            bfp_status = "athletic"
        elif 20 <= bfp < 24:
            bfp_status = "fit"
        elif 24 <= bfp <= 31:
            bfp_status = "average"
        else:
            bfp_status = "overweight"

    weightstate.append(f"Your body fat percentage is {bfp}% ({bfp_status}).")
    return bfp_status

def weight_info(weight, height, sex, waist, neck, hip):
    bfp_status = body_fat_calculations(height, sex, waist, neck, hip)
    status = bmi_calculations(weight, height)
    if status == "underweight" and bfp_status == "essential":
        weightstate.append("You have very low fat and a very low weight, and because of this you"
              "may lack energy or muscle. Focus on gaining lean muscle through nutrition"
              "and strength training.")
    elif bfp_status == "essential" and status == "normal":
        weightstate.append("You have a very low body fat percentage, but healthy weight. It's likely you're athletic."
              "You should maintain your current routine and ensure proper nutrition to"
              "support your current health!")
    elif bfp_status == "essential" and status == "overweight":
        weightstate.append("You have very low fat, but a high BMI. It is likely that you're very muscular."
              "Continue healthy training and monitor your weight trends.")
    elif bfp_status == "essential" and status == "obese":
        weightstate.append("You have very low fat, but a high BMI which is very unusual."
              "Recheck your measurements or consult a healthcare professional."
              "Your BMI may not properly reflect your body composition.")
    elif bfp_status == "athletic" and status == "underweight":
        weightstate.append("It seems like you are lean and fit, but underweight. Consider building muscle"
              " through resistance training and balanced nutrition.")
    elif bfp_status == "athletic" and status == "normal":
        weightstate.append("You are lean and fit! You have a healthy weight and BMI. Keep up the exercise"
              " to maintain health and fitness.")
    elif bfp_status == "athletic" and status == "overweight":
        weightstate.append("It is likely that you are muscular because you have lean body fat, but your BMI is high. "
              "Your BMI may be overestimating your weight, so continue strength training"
              "and healthy habits.")
    elif bfp_status == "athletic" and status == "obese":
        weightstate.append("You have lean fat, but a very high BMI which is rare. It's likely that you're "
              "muscular, but check your remeasurements and maintain and balanced lifestyle.")
    elif bfp_status == "fit" and status == "underweight":
        weightstate.append("You have low-normal fat, but you're also underweight. Focus on healthy weight"
              "gain with protein and strength exercises.")
    elif bfp_status == "fit" and status == "normal":
        weightstate.append("You have a healthy amount of fat and a healthy BMI! Work on maintaining "
              "activity and balanced nutrition for long-term health.")
    elif bfp_status == "fit" and status == "overweight":
        weightstate.append("You have a high BMI, but healthy amount of body fat. You're possibly muscular,"
              "but be sure to monitor your diet and activity to maintain healthy fat levels.")
    elif bfp_status == "fit" and status == "obese":
        weightstate.append("You have a very high BMI, but your body fat percentage is healthy. Review your"
              "lifestyle habits and aim for gradual fat reduction and activity.")
    elif bfp_status == "average" and status == "underweight":
        weightstate.append("You have the average amount of body fat, but a low weight. Ensure your proper nutrition and"
              "muscle building to reach a healthy weight.")
    elif bfp_status == "average" and status == "normal":
        weightstate.append("You have average fat, and healthy BMI. Maintain activity and a healthy diet"
              "to stay in balance!")
    elif bfp_status == "average" and status == "overweight":
        weightstate.append("You have a relatively high BMI, but average amount of body fat. Focus on reducing fat"
              "through cardio and strength training.")
    elif bfp_status == "average" and status == "obese":
        weightstate.append("You have a relatively high BMI, but average amount of body fat. Increase your"
              "activity and adjust your diet to lower health risks.")
    elif bfp_status == "overweight" and status == "underweight":
        weightstate.append("You have a high body fat percentage, but low BMI. Focus on muscle building"
              "and fat reduction for a better body composition.")
    elif bfp_status == "overweight" and status == "normal":
        weightstate.append("You have a high fat percentage, but healthy BMI. You're what some "
              "would consider 'skinny fat'. Improve your diet and add resistance training"
              "to reduce your body fat percentages.")
    elif bfp_status == "overweight" and status == "overweight":
        weightstate.append("You have a high fat percentage and a high BMI. Work on fat reduction through exercise"
              "and nutrition.")
    elif bfp_status == "overweight" and status == "obese":
        weightstate.append("You have a very high fat percentage and BMI. You're at a high health risk."
              "Implement lifestyle changes and consult a professional.")

# weight_info()

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
#print(check_nut())2
