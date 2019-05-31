#----------------------------------------------------------------------
#### Machine Learning Recipes with Josh Gordon (Google Developers) ####

# Class 	Let’s Write a Pipeline - Machine Learning Recipes #4
# Link 		https://youtu.be/84gqSbLcBFE
# @Code  	Josh Gordon		
# @Comments Karl Sousa (github.com/karlvandesman)
#----------------------------------------------------------------------

# Summary -------------------------------------------------------------
# We are going to use the Iris data set again. This time, however, we
# will use another classifier, the k-Nearest Neighbors (KNN).
# We can think of a classifier as a funcion, where the x is the input 
# and y as the output, f(x) = y.
# Using the model_selection we can randomly select the train data from
# the Iris data set, and try to predict the rest of the samples. At the
# end we will measure the accuracy of both classifiers.

# Steps
	# 1- Import dataset and collect training data
	# 2- Train the classifiers
	# 3- Make predictions
	# 4- Measure accuracy

# Code ----------------------------------------------------------------

# 1- Import dataset and collect training data
from sklearn import datasets
iris = datasets.load_iris()
x = iris.data
y = iris.target
print ("### Iris data set ###")

# sklearn.cross_validation has changed to sklearn.model_selection
from sklearn.model_selection import train_test_split
test_size = .1
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)

# 2- Train the classifiers
	# 2.1- Decision Tree
from sklearn import tree
clf_tree = tree.DecisionTreeClassifier()
clf_tree.fit(x_train, y_train)

	# 2.2- KNeighbors
from sklearn.neighbors import KNeighborsClassifier
clf_kneighbors = KNeighborsClassifier()
clf_kneighbors.fit(x_train, y_train)

# 3- Make predictions

predictions_tree = clf_tree.predict(x_test)
predictions_kneighbors = clf_kneighbors.predict(x_test)

# 4- Measure Accuracy
# Using the expected output (y_test), we can measure the % of accuracy
from sklearn.metrics import accuracy_score
print ("Test size = %.2f" % ((1-test_size) * 100), "%")
print ("Accuracy Decision Tree: \t %.2f"  % (100 * accuracy_score(y_test, predictions_tree)), "%")
print ("Accuracy K-N Neighbors: \t %.2f" % (100 * accuracy_score(y_test, predictions_kneighbors)), "%")