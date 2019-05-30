#----------------------------------------------------------------------
#### Machine Learning Recipes with Josh Gordon (Google Developers) ####

# Class 	Visualizing a Decision Tree - Machine Learning Recipes #2
# Link 		https://youtu.be/tNa99PG8hR8
# @Code  	Josh Gordon		
# @Comments 	Karl Sousa
#----------------------------------------------------------------------

# Summary -------------------------------------------------------------
	# We will create a ML using the standard dataset Iris, from sklearn.
	# Still using the decision tree, we will now be able to visualize it.
	# Actually there are few models (as this one) that can be
	# interpretable, and we can see why the classifier makes a decision.
	
	# There are 150 samples in this dataset, and to make some predictions
	# We will exclude some of them of the training data and try to predict
	# what they are (their labels), from their features.

	# Features (can be viewed with iris.feature_names):
		# Sepal length:	0
		# Sepal width: 	1
		# Petal length:	2
		# Petal width: 	3
	# Lables
		# Setosa:	0
		# Versicolor:	1
		# Virginica:	2

# Goals:
	# 1- Import dataset
	# 2- Train a classifier
	# 3- Predict label for new flower
	# 4- Visualize the tree

# Code ----------------------------------------------------------------

import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris() # Iris flower data set

# Printing the features, lables and the first sample
print("Feature names: ", iris.feature_names)
print("Target names:", iris.target_names)
print("First sample (iris.data[0]): ", iris.data[0])

# There are 50 for each type of flower, and they are ordered, so the
# first setose is at index 0, versicolor at 50, and virginica at 100.
test_idx = [0, 50, 100]

# 2- Train classifier
# The training data is composed by the iris data, excluding the data
# with the indexes set in test_idx
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# Testing data
test_target = iris.target[test_idx]	#lables expected ("output")
test_data = iris.data[test_idx] 	#features ("input")

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

# 3- Predict label for new flower

print("Output expected: ", test_target)
print("Output predicted: ", clf.predict(test_data))

# 4- Visualize the tree (viz code)

from sklearn.externals.six import StringIO
import pydot

dot_data = StringIO()
tree.export_graphviz(clf,
						out_file = dot_data,
						feature_names = iris.feature_names,
						class_names = iris.target_names,
						filled = True, rounded = True,
						impurity = False)

graph = pydot.graph_from_dot_data(dot_data.getvalue())

# pydot.graph_from_dot_data returns a list, so we have to get its first element
graph[0].write_pdf("iris.pdf")
