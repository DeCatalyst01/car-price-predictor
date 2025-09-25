from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model and feature names (make sure model_features.pkl has the full feature columns list)
model = joblib.load('car_price_model.pkl')
feature_names = joblib.load('model_features.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect raw inputs from form (change field names if needed)
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Owner = int(request.form['Owner'])
        Age = int(request.form['Age'])
        Fuel_Type = request.form['Fuel_Type']          # Expected: 'Diesel' or 'Petrol' or 'CNG'
        Seller_Type = request.form['Seller_Type']      # Expected: 'Individual' or 'Dealer'
        Transmission = request.form['Transmission']    # Expected: 'Manual' or 'Automatic'

        # Prepare user_input dict in the encoded form your model expects
        user_input = {
            'Present_Price': Present_Price,
            'Kms_Driven': Kms_Driven,
            'Owner': Owner,
            'Age': Age,
            'Fuel_Type_Diesel': 1 if Fuel_Type == 'Diesel' else 0,
            'Fuel_Type_Petrol': 1 if Fuel_Type == 'Petrol' else 0,
            'Fuel_Type_CNG': 1 if Fuel_Type == 'CNG' else 0,
            'Seller_Type_Individual': 1 if Seller_Type == 'Individual' else 0,
            # If your model has 'Seller_Type_Dealer', it will be zero automatically
            'Transmission_Manual': 1 if Transmission == 'Manual' else 0,
            # If 'Transmission_Automatic' exists in features, it will be zero automatically
        }

        # Create zero-filled DataFrame with all features your model expects
        input_df = pd.DataFrame([np.zeros(len(feature_names))], columns=feature_names)

        # Fill input_df with values from user_input
        for key, value in user_input.items():
            if key in input_df.columns:
                input_df.at[0, key] = value

        # Predict
        predicted_lakhs = model.predict(input_df)[0]

        # Currency conversions
        inr_amount = predicted_lakhs * 100_000          # 1 Lakh = ₹100,000
        usd_amount = inr_amount / 83                    # INR to USD conversion rate approx
        ngn_amount = usd_amount * 1500                  # USD to NGN conversion approx

        # Format large numbers with commas
        predicted_lakhs_fmt = f"{predicted_lakhs:,.2f}"
        usd_amount_fmt = f"{usd_amount:,.2f}"
        ngn_amount_fmt = f"{ngn_amount:,.2f}"

        return render_template('result.html',
                               predicted_lakhs=predicted_lakhs_fmt,
                               usd=usd_amount_fmt,
                               ngn=ngn_amount_fmt)
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)