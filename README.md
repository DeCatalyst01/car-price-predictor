# car-price-predictor
 Car Price Prediction (Machine Learning Project)  This project predicts the selling price of cars based on their features (fuel type, number of doors, horsepower, etc.).   It was built as a Machine Learning regression project using Python, with Exploratory Data Analysis (EDA) and multiple models tested. 
 
## 📊 Project Workflow

1. *Data Exploration & Cleaning*
   - Analyzed missing values and distributions
   - Visualized categorical & numerical features (pie charts, bar plots, line plots)
   - Performed bivariate & multivariate analysis

2. *Feature Engineering*
   - Encoded categorical variables
   - Scaled numerical values
   - Prepared features for regression models

3. *Model Training*
   Models tested:
   - Linear Regression
   - Multiple Linear Regression
   - Lasso Regression
   - Ridge Regression
   - ElasticNet Regression

4. *Model Evaluation*
   - Compared models using metrics such as:
     - F1 score
     - Mean Absolute Error (MAE)    
     - Root Mean Squared Error (RMSE)  
     - R² Score  
   - Selected the *best-performing model* for deployment
  
5. *Model Saving*
   - Final model was exported as a .pkl file using joblib.

 ## Repository Structure 
 car-price-prediction/ 
 
 | -- README.md # Project documentation 
 
 | -- requirements.txt # Dependencies
 
 | -- car_price_prediction.ipynb # Main notebook (EDA + model training)
 
 | -- model.pkl  # Trained ML model 
 
 | -- data/ # Data (car_data.csv inside)

 ## Installation & Usage
 1. Clone repo:
    ```bash
    git clone
    https://github.com/DeCatalyst01/car-price-predictor.git
    cd car-price-prediction
    git clone

 2. Create virtual environment & install dependencies:
    pip install -r requirements.txt

3. Open Jupyter Notebook:
   jupyter notebook
   car_price_prediction.ipynb

## Author & Contact
**Dutinaolom Ebi Egoro**
📧 egorodutina@gmail.com  
📍 Lagos, Nigeria  
[LinkedIn] https://www.linkedin.com/in/dutinaolom-egoro-011056122?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
