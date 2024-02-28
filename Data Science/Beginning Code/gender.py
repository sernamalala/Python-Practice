#from sklearn package use tree module
from sklearn import tree


X = [[181,80,44], [177,70,43], [160,60,38], [154,54,37], [166,65,40], [190,90,47], [175,64,39], [177,70,40], [159, 66, 40], [171,75,42], [181,85,43]]

Y = ['male','female','female', 'male','female', 'male', 'female','female','male', 'male','female']

classify_gender = tree.DecisionTreeClassifier()

classify_gender = classify_gender.fit(X,Y)

prediction = classify_gender.predict([[190,70,43]])

print(prediction)