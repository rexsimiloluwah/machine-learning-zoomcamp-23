## 1.1 Introduction to Machine Learning

- Machine learning extracts underlying patterns from data using suitable algorithms to make predictions on new samples of data.

- Machine learning involves training to learn relationships between features and targets and developing a model.

## 1.2 ML vs Rule-Based Systems

- Imagine a rule-based system for a spam detection application

- Rule-based systems use a set of predefined/explicitly programmed rules to make decisions from data. This typically involves using if-else statements.

- Rule-based systems are inflexible

- Machine learning can be used to solve the problems with rule-based systems.

- With ML, we need to get the data, define the features, train and use the model for inference.

- Essentially, rule-based systems take in data and code and produce an outcome/prediction. Machine learning systems take in data and outcomes/target and produce a model.

## Supervised Machine Learning

- Supervised ML is a type of machine learning where the algorithm learns from labelled data to make predictions or decisions. Essentially, the algorithm learns the underlying mapping between input data and the target outputs based on the examples provided in the training dataset.

- Some applications of Supervised ML include:

  - **Classification**: assigning input data to discrete categories/classes or labels (e.g. spam detection, image recognition, sentiment analysis)
  - **Regression**: predicting continuous numeric values from input data (e.g house price prediction, stock price forecasting)
  - **Recommendation systems**: recommending content to users based on their preferences.

- In contrast to supervised ML, unsupervised ML deals with unlabelled data and aims to identify hidden patterns, grouping within the data. Some common unsupervised ML tasks are clustering and dimensionality reduction.

## 1.4 CRISP-DM: Machine Learning Process

- Cross Industry Standard for Data Mining is a methodology for organizing ML projects.

- It involves sequential processes from problem understanding to deployment

- Sequential process:

  - **Business understanding**: Involves identifying the problem, defining the aim and objectives, and the role of machine learning in the project.
  - **Data understanding**: Identify goof data sources, extract suitable and sufficient data for training
  - **Data preparation**: Transform the data into a form that can be used in the machine learning algorithm. This includes data wrangling, data cleaning, feature engineering etc.
  - **Modeling**: This involves model selection, hyperparameter tuning, model training, further feature engineering.
  - **Evaluation**: This involves assessing how well the model is performing.
  - **Deployment**: This involves deploying the model into production, proper monitoring practices that ensure quality, maintainability, and reliability.

- ML projects require many iterations to achieve the best results.

- We will use a spam detection example for illustrating the CRISP-DM process

## 1.5 Model Selection Process

- The datasets into subsets for: training, validation, and testing

- The performance of the trained model on the testing data is used to make a final selection of the model for deployment.

## 1.7 Introduction to NumPy

- Check Jupyter Notebook

## 1.8 Identity Matrix

- Matrix-Matrix Multiplication
- Matrix-Vector Multiplication
- Identity Matrices
  - The product of any matrix and an identity matrix is the same matrix
- Inverse of a Matrix
