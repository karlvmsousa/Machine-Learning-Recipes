#----------------------------------------------------------------------
#### Machine Learning Recipes with Josh Gordon (Google Developers) ####

# Class 	What Makes a Good Feature? - Machine Learning Recipes #3
# Link 		https://youtu.be/N9fDIAflCMY
# @Code  	Josh Gordon		
# @Comments Karl Sousa (github.com/karlvandesman)
#----------------------------------------------------------------------

# Summary -------------------------------------------------------------

# In this simple code we will plot a histogram to see the influence of a 
# feature to the ML. This case is about dogs labradors and greyhounds.
# Which features can be useful to specify the dog breed?

# Features:
# 	- Height
# 	- Eye color

# Ideal features are:
# 	- Informative
# 	- Independent
# 	- Simple

# Code ----------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

#Dogs population
greyhounds = 500
labs = 500

#Lets say that the height is normally distributed (averages 28 and 24)
grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_height = 24 + 4 *np.random.randn(labs)

# Plot an histogram with population and heights for each breed
# With this example we can easily see that for higher heights, the
# population of greyhounds is proportionately greater. So, the ML
# will work with this information to decide if a given data
# represents a greyhound or a labrador.
plt.hist([grey_height, lab_height], stacked=True, color=['r', 'b'])
plt.show()