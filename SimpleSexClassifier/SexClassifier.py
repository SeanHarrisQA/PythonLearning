from sklearn import tree

# [height, weight, shoesize] Dataset

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

classifier = tree.DecisionTreeClassifier()

classifier = classifier.fit(X,Y)

prediction = classifier.predict([[190,70,43],[175,82.55,44.5]])

print(prediction);