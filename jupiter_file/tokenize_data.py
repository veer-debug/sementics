import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer
import pickle

# Load preprocessed data
input_path = 'preprocessed_data.csv'
df = pd.read_csv(input_path)

# Convert to Hugging Face dataset
dataset = Dataset.from_pandas(df)

# Load tokenizer
model_name = 'distilbert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(model_name)

def preprocess(example):
    return tokenizer(example['text'], truncation=True, padding='max_length')

tokenized_dataset = dataset.map(preprocess, batched=True)

# Save tokenized dataset
with open('tokenized_dataset.pkl', 'wb') as f:
    pickle.dump(tokenized_dataset, f)
print('Tokenized dataset saved to tokenized_dataset.pkl') 