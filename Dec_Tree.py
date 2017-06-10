from sklearn import tree

x = [[184,81,41],[167,67,45],[182,72,39],[178,67,36],[175,84,42],[185,82,20],[188,82,42],[186,75,35],[184,81,41],[184,85,45]]
y = ['male','female','female','male','male','male','female','female','female','male']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

prediction = clf.predict([[185,85,42]])
print(prediction)