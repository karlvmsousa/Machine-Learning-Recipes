#----------------------------------------------------------------------
#### Machine Learning Recipes with Josh Gordon (Google Developers) ####

# Class 	Writing Our First Classifier - Machine Learning Recipes #5
# Link 		https://youtu.be/AoeEHqVSNOw
# @Code  	Josh Gordon		
# @Comments Karl Sousa (github.com/karlvandesman)
#----------------------------------------------------------------------

# Summary -------------------------------------------------------------
# In order to really understand what is behind a classifier, we will 
# build our own.
# Implement a class and its methods 

# Steps
	# 1- Create the classifiers
	# 2- Import dataset and collect training data
	# 3- Train the classifiers
	# 4- Make predictions
	# 5- Measure accuracy

# Code ----------------------------------------------------------------

# 1- Create the classifiers
import random

class randomKNN():
	def fit(self, x_train, y_train):
		self.x_train = x_train
		self.y_train = y_train

	def predict(self, x_test):
		predictions = []

		for row in x_test:
		# Here we are just guessing the output, randomly
			label = random.choice(self.y_train)
			predictions.append(label)
		return predictions

from scipy.spatial import distance 

def euc(a, b):
	return distance.euclidean(a, b)

class myKNN():
	def fit(self, x_train, y_train):
		self.x_train = x_train
		self.y_train = y_train

	def predict(self, x_test):
		predictions = [] 
		for row in x_test:
			label = self.closest(row)
			predictions.append(label)
		return predictions

	def closest(self, row):
		best_dist = euc(row, self.x_train[0])
		best_index = 0
		for i in range(1, len(self.x_train)):
			dist = euc(row, self.x_train[i])
			if dist < best_dist:
				best_dist
				best_index = i
		return self.y_train[best_index]

# 2- Import dataset and collect training data
from sklearn import datasets
iris = datasets.load_iris()
x = iris.data
y = iris.target
print ("### Iris data set ###")

# sklearn.cross_validation has changed to sklearn.model_selection
from sklearn.model_selection import train_test_split
test_size = .1
print ("Test size = %.2f" % ((1-test_size) * 100), "%")

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)

# 3- Train the classifiers
from sklearn.neighbors import KNeighborsClassifier

clf_randomKNN = randomKNN()
clf_randomKNN.fit(x_train, y_train)

clf_myKNN = myKNN()
clf_myKNN.fit(x_train, y_train)

clf_kneighbors = KNeighborsClassifier()
clf_kneighbors.fit(x_train, y_train)

# 4- Make predictions

predictions_randomKNN = clf_randomKNN.predict(x_test)
predictions_myKNN = clf_myKNN.predict(x_test)
predictions_kneighbors = clf_kneighbors.predict(x_test)

# 5- Measure Accuracy
# Using the expected output (y_test), we can measure the % of accuracy
from sklearn.metrics import accuracy_score

print ("Accuracy random KNN: \t %.2f" % (100 * accuracy_score(y_test, predictions_randomKNN)), "%")
print ("Accuracy myKNN: \t %.2f" % (100 * accuracy_score(y_test, predictions_myKNN)), "%")
print ("Accuracy original KNN: \t %.2f" % (100 * accuracy_score(y_test, predictions_kneighbors)), "%")