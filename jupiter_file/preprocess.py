import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load data
input_path = 'sample_data1.csv'
df = pd.read_csv(input_path)
df.columns = ['text', 'label']  # Ensure correct column names
df.dropna(inplace=True)

# Encode labels
label_encoder = LabelEncoder()
df['label'] = label_encoder.fit_transform(df['label'])

# Save label mapping for later use
import pickle
with open('label_mapping.pkl', 'wb') as f:
    pickle.dump(dict(zip(range(len(label_encoder.classes_)), label_encoder.classes_)), f)

# Save preprocessed data
output_path = 'preprocessed_data.csv'
df.to_csv(output_path, index=False)
print(f'Preprocessed data saved to {output_path}') 