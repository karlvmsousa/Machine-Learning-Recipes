# Machine-Learning-Recipes
Machine Learning Recipes is a [series of introductory videos](https://goo.gl/KewA03) covering codes and insights about ML with python and opensource libraries (TensorFlow and Scikit-learn).

## #1 Hello World
Six lines of Python is all it takes to write a simple machine learning program. We will collect some simple data and with a decision tree, predict wheter an input represents an orange or an apple, by its weight and texture.

![helloworld](https://user-images.githubusercontent.com/31048109/58599496-ec041680-8256-11e9-8cc2-8d0fba546883.jpg)

## #2 Visualizing a Decision Tree
We'll build a decision tree on a real dataset, add code to visualize it, and practice reading it. 

![image](https://user-images.githubusercontent.com/31048109/58599704-c9263200-8257-11e9-9212-2dcd5d9d4b8c.png)

## #3 What Makes a Good Feature? 
Good features are informative, independent, and simple. These concepts will be introduced by using a histogram to visualize a feature from a toy dataset. There are other great examples of histograms codes, that you can find here:
https://matplotlib.org/examples/statistics/histogram_demo_multihist.html

![image](https://user-images.githubusercontent.com/31048109/58599828-4356b680-8258-11e9-95f3-5d49524bbde8.png)

## #4 Writing a pipeline
We use the Iris data set again, but with another classifier, the k-Nearest Neighbors (KNN). Using the model_selection we can randomly select the train data from the Iris data set, and try to predict the rest of the samples. At the end we will measure the accuracy of both classifiers.

![image](https://user-images.githubusercontent.com/31048109/58675739-08be4e00-832c-11e9-8c8b-2ae69e94c421.png)

## #5 Writing our first classifier
In order to really understand what is behind a classifier, we will build our own, base on the k-Nearest Neighbors (KNN). At the end, we compare the accuracy of a random prediction, our classifier KNN, and the KNN from the library.

![image](https://user-images.githubusercontent.com/31048109/58675887-a44fbe80-832c-11e9-8d4f-27d527a27b7c.png)

## #6 Train an Image Classifier with TensorFlow for Poets
A brief introduction to Tensorflow. This is a great way to get started learning about and working with image classification. It is important to say that tensorflow is a high level code and a powerful classifier.

![image](https://user-images.githubusercontent.com/31048109/59273614-ff3bbc80-8c2e-11e9-85da-62887fbbbb2f.png)

## #7 Classifying Handwritten Digits with TF.Learn
This time we will create a image classifier using TF.Learn. The problem is to classify handwritten digits from the MNIST dataset. Given an image of a digit we have is to predict which one it is (0-9). At the end we'll visualize the weights the classifier learns and gain intuition on how it works. This lesson is conducted in a .ipynb file, a Notebook that can run python. You can run it by Jupyter or by [Google Colab](https://colab.research.google.com/), an interesting cloud option. 

![image](https://user-images.githubusercontent.com/31048109/58753442-7cc83580-8495-11e9-9317-3ac2b574d37f.png)

## #8 Let’s Write a Decision Tree Classifier from Scratch
In a simple example of predicting the type of fruit, we'll write a decision tree classifier (using CART). Which questions are the best to partition the dataset? How to quantify the uncertainty? We'll build the functions to answer these questions and show how the impurity and information gain are calculated.

![image](https://user-images.githubusercontent.com/31048109/58976837-c4ed9d80-879e-11e9-99d4-c6953f1f1a37.png)

## #9 Intro to Feature Engineering with TensorFlow
In this lesson we will look at ways of represent the features, to turn them in a more useful representation. To visualize what the transformations on the features do, we will use the tool FACETS. We will deal with Bucketing, Crossing, Hashing and Embedding. The goal in this example is to predict if someone's income is greater than US$ 50k.

![image](https://user-images.githubusercontent.com/31048109/59074132-89d39300-88a0-11e9-8eea-b0105be62bc7.png)

## #10 Getting Started with Weka
In this lesson we will work with Weka, a ML library with Graphical User Interface (GUI). The examples are: predict if a person has diabets, based on its glucose levels and predict if a congress person is a Democrat or a Republican based on how they voted on different bills. Also, we'll see how to evaluate the results of these experiments and how to do feature selection.

![image](https://user-images.githubusercontent.com/31048109/59235375-38d8dd00-8bc7-11e9-96d7-82ab8d4dc4fa.png)
