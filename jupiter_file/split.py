import pickle

# Load tokenized dataset
with open('tokenized_dataset.pkl', 'rb') as f:
    tokenized_dataset = pickle.load(f)

# Split into train and test
split_dataset = tokenized_dataset.train_test_split(test_size=0.2, seed=42)
train_data = split_dataset['train']
eval_data = split_dataset['test']

# Save splits
with open('train_data.pkl', 'wb') as f:
    pickle.dump(train_data, f)
with open('eval_data.pkl', 'wb') as f:
    pickle.dump(eval_data, f)
print('Train and eval splits saved to train_data.pkl and eval_data.pkl') 