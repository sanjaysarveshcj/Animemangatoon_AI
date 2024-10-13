import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

data = {
    'description': [
        "A high school romance between a shy girl and the most popular boy.",
        "A fantasy adventure of a young hero who battles monsters and villains.",
        "An intense action-packed story featuring a vigilante fighting crime.",
        "A story of friendship and love in a magical world.",
        "A detective solving supernatural mysteries in a bustling city.",
        "A slice-of-life romance exploring a summer love story.",
        "A fantasy about a warrior who seeks revenge against dark forces.",
        "A high-paced action series with martial arts and powerful enemies.",
        "A touching romance between two rivals who end up falling in love.",
        "A mystical fantasy about a hidden realm and a chosen one."
    ],
    'category': [
        "romance",
        "fantasy",
        "action",
        "fantasy",
        "action",
        "romance",
        "fantasy",
        "action",
        "romance",
        "fantasy"
    ]
}

df = pd.DataFrame(data)

X = df['description']
y = df['category']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

use_decision_tree = True

if use_decision_tree:
    model = DecisionTreeClassifier(random_state=42)
else:
    model = LogisticRegression(max_iter=1000)

model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)

accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")

def classify_webtoon_description(description):
    description_vec = vectorizer.transform([description])
    prediction = model.predict(description_vec)[0]
    return prediction

user_description = input("Enter a webtoon description: ")
predicted_category = classify_webtoon_description(user_description)
print(f"The predicted category for your webtoon is: {predicted_category}")
