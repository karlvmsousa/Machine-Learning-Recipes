#----------------------------------------------------------------------
#### Machine Learning Recipes with Josh Gordon (Google Developers) ####

# Class 	Hello World - Machine Learning Recipes #1
# Link		https://youtu.be/cKxRvEZd3Mw
# @Code 	Josh Gordon		
# @Comments 	Karl Sousa
#----------------------------------------------------------------------

# Summary -------------------------------------------------------------
	# We will create a ML to distinguish between oranges and apples
	# Features: Weight and texture
		# Smooth = 1
		# Bumpy = 0
	# Labels: Orange and Apple
		# Orange = 1
		# Apple = 0

# Steps:
	# 1- Collect training data
	# 2- Train classifier
	# 3- Make Predictions

from sklearn import tree
# Scikit-learn uses real-value features, so we have to
# "translate" the features words into numbers

# Code ----------------------------------------------------------------
# 1 - Collect training data
features = [[140, 1], [130, 1], [150, 0], [170, 0]]	#input data
labels = [0, 0, 1, 1]					#output data

# 2 - Train classifier (we will use the Decision tree)
clf = tree.DecisionTreeClassifier()

# We still need a learning algorithm to build the rules for 
# this decision tree
clf = clf.fit(features, labels)

# 3 - Make Predictions
# Now, we just have to use the function
# clf.predict([[feature1, feature2]]) and see what is the output
print (clf.predict([[150, 0]]))
