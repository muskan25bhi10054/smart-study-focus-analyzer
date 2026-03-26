import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("study_data.csv")

# Features & target
X = data[['Sleep_Hours', 'Screen_Time', 'Study_Hours', 'Breaks']]
y = data['Focus']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

print("Model Accuracy:", model.score(X_test, y_test))


# REASON FUNCTION 
def explain(sleep, screen, study, breaks):
    reasons = []
    
    if sleep < 6:
        reasons.append("You are not getting enough sleep")
    if screen > 4:
        reasons.append("Too much screen time is distracting you")
    if study < 3:
        reasons.append("Your study time is too low")
    if breaks > 4:
        reasons.append("Too many breaks reduce focus")

    return reasons


# SUGGESTION FUNCTION 
def suggest(sleep, screen, study, breaks):
    tips = []
    
    if sleep < 6:
        tips.append("Try to sleep at least 7 hours")
    if screen > 4:
        tips.append("Reduce screen time before studying")
    if study < 3:
        tips.append("Increase focused study time")
    if breaks > 4:
        tips.append("Limit unnecessary breaks")

    return tips


#  PRODUCTIVITY SCORE 
def productivity_score(sleep, screen, study, breaks):
    score = 50
    score += sleep * 5
    score -= screen * 4
    score += study * 6
    score -= breaks * 3

    return max(0, min(100, score))


def focus_meaning(level):
    if level == "High":
        return "You are highly focused and productive"
    elif level == "Medium":
        return "Your focus is average, can be improved"
    else:
        return "You are easily distracted and need improvement"


def performance_label(score):
    if score >= 85:
        return "Excellent 🌟"
    elif score >= 70:
        return "Good 👍"
    elif score >= 50:
        return "Average ⚠️"
    else:
        return "Poor ❌"


#  USER INPUT 
sleep = float(input("Enter sleep hours: "))
screen = float(input("Enter screen time: "))
study = float(input("Enter study hours: "))
breaks = float(input("Enter breaks: "))

import pandas as pd

input_data = pd.DataFrame([[sleep, screen, study, breaks]],
                          columns=['Sleep_Hours', 'Screen_Time', 'Study_Hours', 'Breaks'])

prediction = model.predict(input_data)

import pandas as pd

input_data = pd.DataFrame([[sleep, screen, study, breaks]],
                          columns=['Sleep_Hours', 'Screen_Time', 'Study_Hours', 'Breaks'])

prediction = model.predict(input_data)

print("\n===================================")
print("🤖 SMART STUDY FOCUS ANALYZER")
print("===================================")

print(f"\n📊 Input Summary:")
print(f"Sleep: {sleep} hrs | Screen: {screen} hrs | Study: {study} hrs | Breaks: {breaks}")

print("\n-----------------------------------")

print("\n🔹 Predicted Focus Level:", prediction[0])

print("🔹 Focus Insight:", focus_meaning(prediction[0]))

reasons_list = explain(sleep, screen, study, breaks)
if reasons_list:
    print("\n🔹 Reasons:")
    for r in reasons_list:
        print("  •", r)
else:
    print("\n🔹 Reasons: Good habits detected!")

suggestions_list = suggest(sleep, screen, study, breaks)
if suggestions_list:
    print("\n🔹 Suggestions:")
    for s in suggestions_list:
        print("  •", s)
else:
    print("\n🔹 Suggestions: Keep it up! 👍")

score = productivity_score(sleep, screen, study, breaks)

print("\n🔹 Productivity Score:", score)
print("🔹 Performance Level:", performance_label(score))