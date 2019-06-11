## Getting Started with Weka - Machine Learning Recipes #10

### **Video**: https://www.youtube.com/watch?v=TF1yh5PKaqI

#### 1. Downloading and installing Weka

#### 2. Open the Weka using the "Explorer" application
You can run Weka by the following command:
`java -jar weka.jar`

#### 4. Open the dataset
We will download the UCI Repository which contains about 40 datasets.

#### 5. Analyzing the features
Now we can see some information about the dataset opened. Selecting the features, a histogram is shown of how different values correlate to the class we want to predict.

![image](https://user-images.githubusercontent.com/31048109/59236395-52305800-8bcc-11e9-84e5-d867b74e3c73.png)

In the image above we can see the histogram with the plasma concentracion, and clearly we can say that is more likely to have a positive for diabets with concentracions of more than 100.

#### 6. Running the classifier
We just have to choose the classifier and then hit the start button. We can also flip between the results of different results. Test options are available, and a interesting option is cross-validation. It iteratively divide the dataset into two chunks, one being used for training and the other for testing. Then it trains and evaluates the model repeated times, and finally average the results.

![image](https://user-images.githubusercontent.com/31048109/59236687-b7387d80-8bcd-11e9-8508-df519b6f1fb1.png)

#### 7. Evaluating performance
We have available more than the accuracy as a metric for the performance. The others metrics are important mainly when one of the classes is rare. When we are evaluating classifiers, we have to look at accuracy both on the positive and negative cases. So, using the confusion matrix, we can also calculate precision, recall, f-measure, and others metrics.

#### 8. Feature selection
In order to see which feature has a better influence on diagnostic of diabets, we can rank them by their information gain, using the filter tool in Weka. Also, to see the best combination of features, we have to search for a subset of features.
