# World Cuisine Classification

### Project Description
This project analyzes dish compositions to predict the probability of an unlabeled sample belonging to one of 20 different world cuisines.
The dataset is sourced from Kaggle: https://www.kaggle.com/datasets/kaggle/recipe-ingredients-dataset/data

### Methodology
* **Data Preprocessing:** Text cleaning, custom stop-word removal, and vectorization using TfidfVectorizer.
* **Models:** Training and performance comparison of MultinomialNB, LogisticRegression, and LinearSVC (wrapped in CalibratedClassifierCV for probability estimation).

### Results:
* **Best model:** LinearSVC+CalibratedClassifierCV.
* **Accuracy:** 78.8%. 
* **Output:** Predicted class probabilities for a test set of 9,944 observations.
