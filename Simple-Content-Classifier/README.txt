Task 1: Webtoon Content Classifier

Overview:
This task involved creating a simple content classifier that categorizes webtoon descriptions into genres such as romance, action, and fantasy. A small dataset of 15 webtoon descriptions was utilized to train the model.

Approach:
Data Preparation: Collected a dataset with webtoon descriptions and their respective categories.
Feature Extraction: Used CountVectorizer to convert text data into numerical format.
Model Training: Implemented a logistic regression model from the scikit-learn library to classify descriptions.
Evaluation: The model’s accuracy was calculated and displayed.

Code Documentation:
The script contains comments to explain each step, from data loading to model evaluation.
Accuracy and classification results are printed for user feedback.

Usage:
Run the script, input a description, and receive the predicted category along with the accuracy score.
