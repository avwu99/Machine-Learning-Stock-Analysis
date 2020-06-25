import processing
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split

class learner():
    def __init__(self):
        self.l = tree.DecisionTreeClassifier()
        self.train_features = None
        self.train_targets = None
        self.test_features = None
        self.test_targets = None

    def split(self, features, targets):
        X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.33)

        self.train_features = X_train
        self.train_targets = y_train

        self.test_features = X_test
        self.test_targets = y_test

    def fit_learner(self):
        self.l.fit(self.train_features, self.train_targets)

    def test_learner(self):
        correct = 0
        total = self.test_features.shape[0]

        predicted = self.l.predict(self.test_features)
        #print(predicted)

        for i in range(total):
            if predicted[i] == self.test_targets[i]:
                correct += 1

        return correct/total

################################## TESTING #####################################
##consumercyc
data = processing.processor('C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/consumercyc/', 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/consumercycMACD/', 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/consumercycRSI/', 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/consumercycHistorical/')
data.populate_data()

features = np.array(data.features)
targets = np.array(data.targets)

print(features.shape)
machine = learner()

total = 0
for i in range(100):
    machine.split(features, targets)
    machine.fit_learner()
    percentage = machine.test_learner()
    total += percentage

avg = total/100

print("Consumer Cyc Average Accuracy: ", avg)

## Energy
data = processing.processor('C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/energy/', 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/energyMACD/', 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/energyRSI/', 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/energyHistorical/')

data.populate_data()

features = np.array(data.features)
targets = np.array(data.targets)
print(features.shape)

machine = learner()

total = 0
for i in range(100):
    machine.split(features, targets)
    machine.fit_learner()
    percentage = machine.test_learner()
    total += percentage

avg = total/100

print("Energy Average Accuracy: ", avg)


## Tech
data = processing.processor('C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/tech/', 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/techMACD/', 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/techRSI/', 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/techHistorical/')

data.populate_data()

features = np.array(data.features)
targets = np.array(data.targets)
print(features.shape)
machine = learner()

total = 0
for i in range(100):
    machine.split(features, targets)
    machine.fit_learner()
    percentage = machine.test_learner()
    total += percentage

avg = total/100

print("Tech Average Accuracy: ", avg)
