import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# create dataset
data = {
    'Math': [50, 30, 80, 60, 25],
    'Science': [45, 20, 85, 65, 30],
    'English': [55, 35, 75, 50, 40],
    'Result': ['pass', 'fail', 'pass', 'pass', 'fail']
}

# create DataFrame
df = pd.DataFrame(data)

# features and target
x = df[['Math', 'Science', 'English']]  # features
y = df['Result']  # target

# model training
model = DecisionTreeClassifier()
model.fit(x, y)

# prediction
new_student = [[40, 42, 38]]  # marks
prediction = model.predict(new_student)
print("Prediction:", prediction[0])

# accuracy
print("Model Accuracy:", model.score(x, y))
