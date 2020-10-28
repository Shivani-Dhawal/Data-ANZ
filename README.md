# Data Analytics at ANZ Virtual Internship

This is Repository for all the work included in "Data Analytics" track provided by ANZ on daily transactions data provided by the ANZ.

### Task-1 [Exploratory Data Analysis](https://github.com/Shivani-Dhawal/Data-ANZ/blob/main/ANZ%20task1.py)
Performed Exploratory data analysis on the given transaction data of 92 days from August'18 to October'18.The transaction data of 1 day was missing, so effective 91 days data was used for analysis.Used Pandas to segregate customer data by each month and used Matplotlib to visualise transaction volume and mean transaction amount each day. Also visualised mean customer balance and mean payment amount by age, with gender means included, for each month in data set.

### Task-2 [Predictive Analytics](https://github.com/Shivani-Dhawal/Data-ANZ/blob/main/ANZ%20Task2.py)
Used Pandas to evaluate mean customer annual salary and then grouped customer data by customer id and mean. Used Scikit-learn for machine learning algorithms in Python. Linear regression model - used card present flag, merchant code, balance, age and amount from grouped data set to predict annual salary, obtained test prediction accuracy of -0.32. Reverting back to original data set, created dummy variables for categorical variables including gender and age. Decision tree classifier and regression models - used modified data set to predict annual salary, obtained test scores of 0.76 and 0.67 respectively.
