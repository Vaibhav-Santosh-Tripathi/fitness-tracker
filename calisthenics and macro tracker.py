from datetime import date, timedelta
activity_levels = {"sedentary": 1.2,"light": 1.375,"moderate": 1.55,"active": 1.725,"very_active": 1.9}
protein_per_kg = {"cut": 2.2, "maintain": 1.8, "bulk": 2.0}
calorie_change = {"cut": -500, "maintain": 0, "bulk": 300}
exercises = [["Push-ups", "reps"],["Pike Push-ups", "reps"],["Dips", "reps"],["Pull-ups", "reps"],["Chin-ups", "reps"],["Inverted Rows", "reps"],["Bodyweight Squats", "reps"],["Lunges", "reps"],["Glute Bridges", "reps"],["Plank", "seconds"],["Hanging Leg Raises", "reps"],["Burpees", "reps"]]
difffoods = [["Chicken Breast (cooked)", 165, 31.0, 0.0, 3.6],["Eggs (whole)", 155, 13.0, 1.1, 11.0],["White Rice (cooked)", 130, 2.7, 28.0, 0.3],["Oats (dry)", 389, 16.9, 66.3, 6.9],["Banana", 89, 1.1, 22.8, 0.3],["Whole Milk", 61, 3.2, 4.8, 3.3],["Paneer", 265, 18.3, 1.2, 20.8],["Lentils (cooked, dal)", 116, 9.0, 20.1, 0.4],["Roti (whole wheat)", 297, 11.0, 60.0, 3.5],["Peanut Butter", 588, 25.0, 20.0, 50.0],["Greek Yogurt", 59, 10.0, 3.6, 0.4],["Almonds", 579, 21.2, 21.6, 49.9]]
def filekareader(filename):
    try:
        f = open(filename, "r")
        lines = f.readlines()
        f.close()
    except FileNotFoundError:
        lines = []
    return lines
def add2file(filename, line):
    f = open(filename, "a")
    f.write(line + "\n")
    f.close()
def load_users():
    users = []
    for line in filekareader("users.txt"):
        p = line.strip().split(",")
        if len(p) == 8:
            
            users.append([int(p[0]), p[1], int(p[2]), p[3], float(p[4]), float(p[5]), p[6], p[7]])
    return users
def newfoodkaloader():
    
    for line in filekareader("difffoods.txt"):
        p = line.strip().split(",")
        if len(p) == 5:
            difffoods.append([p[0], float(p[1]), float(p[2]), float(p[3]), float(p[4])])
def intgetter(message, low, high):
    while True:
        try:
            num = int(input(message))
            if num >= low and num <= high:
                return num
            print("Enter a number between", low, "and", high)
        except ValueError:
            print("Please enter a whole number")
def getfloat(message, low, high):
    while True:
        try:
            num = float(input(message))
            if num >= low and num <= high:
                return num
            print("Enter a number between", low, "and", high)
        except ValueError:
            print("Please enter a number")
def choicegetter(message, options):
    while True:
        text = input(message).strip().lower()
        if text in options:
            return text
        print("Choose from:", options)
def get_date(message):

    while True:
        text = input(message).strip()
        if text == "":
            return str(date.today())
        try:
            d = date.fromisoformat(text)
            return str(d)
        except ValueError:
            print("Wrong format, write like 2026-09-30")
def get_text(message):

    text = input(message).strip()
    return text.replace(",", " ")
def find_targets(user):
   
    age = user[2]
    gender = user[3]
    height = user[4]
    weight = user[5]
    activity = user[6]
    goal = user[7]
   
    bmr = 10 * weight + 6.25 * height - 5 * age
    if gender == "male":
        bmr = bmr + 5
    else:
        bmr = bmr - 161
    tdee = bmr * activity_levels[activity]
    calories = tdee + calorie_change[goal]
    protein = protein_per_kg[goal] * weight
    fat = 0.8 * weight

    remaining = calories - protein * 4 - fat * 9
    if remaining < 0:
        remaining = 0
    carbs = remaining / 4
    return [round(calories), round(protein), round(carbs), round(fat)]
def foodfinder(name):
    for f in difffoods:
        if f[0] == name:
            return f
    return None
def day_totals(user_id, day):
    cal = 0
    pro = 0
    carb = 0
    fat = 0
    for line in filekareader("meals.txt"):
        p = line.strip().split(",")
        if len(p) == 5 and int(p[0]) == user_id and p[2] == day:
            f = foodfinder(p[1])
            if f != None:
                grams = float(p[4])
                cal = cal + f[1] * grams / 100
                pro = pro + f[2] * grams / 100
                carb = carb + f[3] * grams / 100
                fat = fat + f[4] * grams / 100
    return [round(cal, 1), round(pro, 1), round(carb, 1), round(fat, 1)]
def prog_bar(current, target):
    if target <= 0:
        return "n/a"
    percent = current / target
    filled = int(percent * 20)
    if filled > 20:
        filled = 20
    return "[" + "#" * filled + "-" * (20 - filled) + "] " + str(round(percent * 100)) + "%"
def create_profile(users):
    print("\nLet's make your profile")
    name = get_text("Name: ")
    if name == "":
        name = "Athlete"
    age = intgetter("Age: ", 10, 100)
    gender = choicegetter("Gender (male/female): ", ["male", "female"])
    height = getfloat("Height in cm: ", 100, 250)
    weight = getfloat("Weight in kg: ", 30, 300)
    print("Activity levels: sedentary, light, moderate, active, very_active")
    activity = choicegetter("Activity level: ", list(activity_levels.keys()))
    goal = choicegetter("Goal (cut/maintain/bulk): ", ["cut", "maintain", "bulk"])
    if len(users) == 0:
        new_id = 1
    else:
        new_id = users[-1][0] + 1
    user = [new_id, name, age, gender, height, weight, activity, goal]
    users.append(user)
    line = str(new_id) + "," + name + "," + str(age) + "," + gender + "," + str(height) + "," + str(weight) + "," + activity + "," + goal
    add2file("users.txt", line)
    t = find_targets(user)
    print("\nProfile created! Your daily targets are:")
    print("Calories:", t[0], "kcal")
    print("Protein :", t[1], "g")
    print("Carbs   :", t[2], "g")
    print("Fat     :", t[3], "g")
    return user
def profilechooser(users):
    print("\n===== Calisthenics and Macro Tracker =====")
    if len(users) == 0:
        return create_profile(users)
    print("Profiles:")
    for u in users:
        print(u[0], "-", u[1], "(goal:", u[7] + ")")
    print("0 - Make a new profile")
    while True:
        choice = intgetter("Choose: ", 0, users[-1][0])
        if choice == 0:
            return create_profile(users)
        for u in users:
            if u[0] == choice:
                return u
        print("No profile with that number")
def loggingworkout(user):
    print("\n----- Log a workout -----")
    for i in range(len(exercises)):
        print(i + 1, "-", exercises[i][0], "(" + exercises[i][1] + ")")
    num = intgetter("Exercise number: ", 1, len(exercises))
    day = get_date("Date (YYYY-MM-DD, press enter for today): ")
    sets = intgetter("Number of sets: ", 1, 50)
    amount = intgetter("Reps (or seconds for holds) per set: ", 1, 1000)
    notes = get_text("Notes (optional): ")
    name = exercises[num - 1][0]
    unit = exercises[num - 1][1]
    line = str(user[0]) + "," + name + "," + unit + "," + day + "," + str(sets) + "," + str(amount) + "," + notes
    add2file("workouts.txt", line)
    print("Workout saved!")
def histroyofworkout(user):
    print("\n----- Workout history -----")
    bestnames=[]
    bestvalues=[]
    bestunits=[]
    count=0
    for line in filekareader("workouts.txt"):
        p = line.strip().split(",")
        
        if len(p) == 7 and int(p[0]) == user[0]:
            count = count + 1
            print(p[3], "-", p[1], "-", p[4], "sets x", p[5], p[2], p[6])
            
            amount = int(p[5])
            if p[1] in bestnames:
                i = bestnames.index(p[1])
                if amount > bestvalues[i]:
                    bestvalues[i] = amount
            else:
                bestnames.append(p[1])
                bestvalues.append(amount)
                bestunits.append(p[2])
    if count == 0:
        print("No workouts logged yet")
        return
    print("\nPersonal bests (best single set):")
    for i in range(len(bestnames)):
        print(bestnames[i], ":", bestvalues[i], bestunits[i])
def addingnewfood():
    name = get_text("Food name: ")
    if name == "":
        print("Name cannot be empty")
        return None
    if foodfinder(name) != None:
        print("That food is already in the list")
        return name
    cal = getfloat("Calories per 100g: ", 0, 1000)
    protein = getfloat("Protein per 100g: ", 0, 100)
    carbs = getfloat("Carbs per 100g: ", 0, 100)
    fat = getfloat("Fat per 100g: ", 0, 100)
    difffoods.append([name, cal, protein, carbs, fat])
    line = name + "," + str(cal) + "," + str(protein) + "," + str(carbs) + "," + str(fat)
    add2file("difffoods.txt", line)
    print("Food added!")
    return name
def logdameal(user):
    print("\n----- Log a meal -----")
    print("1 - Choose from food list")
    print("2 - Add a new food")
    option = intgetter("Choice: ", 1, 2)
    if option == 2:
        nameoffood = addingnewfood()
        if nameoffood == None:
            return
    else:
        for i in range(len(difffoods)):
            print(i + 1, "-", difffoods[i][0], "(" + str(round(difffoods[i][1])) + " kcal per 100g)")
        num = intgetter("Food number: ", 1, len(difffoods))
        nameoffood = difffoods[num - 1][0]
    day = get_date("Date (YYYY-MM-DD, press enter for today): ")
    typeofmeal = choicegetter("Meal (breakfast/lunch/dinner/snack): ", ["breakfast", "lunch", "dinner", "snack"])
    grams = getfloat("Quantity eaten in grams: ", 1, 5000)
    line = str(user[0]) + "," + nameoffood + "," + day + "," + typeofmeal + "," + str(grams)
    add2file("meals.txt", line)
    print("Meal saved!")
def dailykasummary(user):
    print("\n----- Daily summary -----")
    day = get_date("Date (YYYY-MM-DD, press enter for today): ")
    t = find_targets(user)
    total = day_totals(user[0], day)
    print("\nSummary for", user[1], "on", day)
    print("-" * 50)
    print("Calories:", total[0], "/", t[0], "kcal", prog_bar(total[0], t[0]))
    print("Protein :", total[1], "/", t[1], "g", prog_bar(total[1], t[1]))
    print("Carbs   :", total[2], "/", t[2], "g", prog_bar(total[2], t[2]))
    print("Fat     :", total[3], "/", t[3], "g", prog_bar(total[3], t[3]))
    print("\nMeals eaten:")
    found = False
    for line in filekareader("meals.txt"):
        p = line.strip().split(",")
        if len(p) == 5 and int(p[0]) == user[0] and p[2] == day:
            f = foodfinder(p[1])
            if f != None:
                cals = round(f[1] * float(p[4]) / 100)
                print(p[3], "-", p[1], "-", p[4], "g -", cals, "kcal")
                found = True
    if found == False:
        print("Nothing logged for this day")
def weeksummary(user):
    print("\n----- Weekly summary (last 7 days) -----")
    days = []
    for i in range(6, -1, -1):
        days.append(str(date.today() - timedelta(days=i)))
    activedays = []
    tot_sets = 0
    for line in filekareader("workouts.txt"):
        p = line.strip().split(",")
        if len(p) == 7 and int(p[0]) == user[0] and p[3] in days:
            tot_sets = tot_sets + int(p[4])
            if p[3] not in activedays:
                activedays.append(p[3])
    print("Days trained:", len(activedays), "out of 7")
    print("Total sets  :", tot_sets)
    calories = []
    for d in days:
        calories.append(day_totals(user[0], d)[0])
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("\nmatplotlib is not installed so the chart was not made")
        return
    target = find_targets(user)[0]
    plt.bar(days, calories, label="Calories eaten")
    plt.axhline(target, color="red", linestyle="--", label="Target")
    plt.title("Calories in the last 7 days")
    plt.xlabel("Date")
    plt.ylabel("Calories (kcal)")
    plt.xticks(rotation=30)
    plt.legend()
    plt.tight_layout()
    plt.savefig("calorie_chart.png")
    plt.close()
    print("\nChart saved as calorie_chart.png")
newfoodkaloader()
all_users = load_users()
current_user = profilechooser(all_users)
while True:
    print("\n===== Main Menu (" + current_user[1] + ") =====")
    print("1. Log a workout")
    print("2. View workout history")
    print("3. Log a meal")
    print("4. Daily summary")
    print("5. Weekly summary and chart")
    print("6. Switch or make profile")
    print("0. Exit")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        loggingworkout(current_user)
    elif choice == "2":
        histroyofworkout(current_user)
    elif choice == "3":
        logdameal(current_user)
    elif choice == "4":
        dailykasummary(current_user)
    elif choice == "5":
        weeksummary(current_user)
    elif choice == "6":
        current_user = profilechooser(all_users)
    elif choice == "0":
        print("Stay consistent. See you tomorrow!")
        break
    else:
        print("Invalid choice, try again")





