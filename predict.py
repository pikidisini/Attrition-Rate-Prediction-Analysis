import pandas as pd
import joblib

# Load pipeline
model_pipeline = joblib.load('model_pipeline.pkl')

# Load data
df_unlabeled = pd.read_csv('unlabeled_data.csv')

# Drop kolom yang tidak relevan
df_unlabeled = df_unlabeled.drop(columns=['EmployeeCount', 'Over18', 'StandardHours', 'EmployeeId'], errors='ignore')

# Prediksi langsung
predictions = model_pipeline.predict(df_unlabeled)

# Simpan hasil
df_unlabeled['Attrition_Prediction'] = predictions
df_unlabeled.to_csv('predicted_attrition.csv', index=False)

print("Prediksi selesai. Hasil disimpan ke predicted_attrition.csv")