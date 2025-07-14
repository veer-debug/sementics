import pickle
from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments

# Load train data
with open('train_data.pkl', 'rb') as f:
    train_data = pickle.load(f)

# Model setup
model_name = 'distilbert-base-uncased'
num_labels = len(set(train_data['label']))
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=num_labels)

# Training arguments (no evaluation_strategy)
training_args = TrainingArguments(
    output_dir='./results',
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
)

# Train
trainer.train()

# Save model
model.save_pretrained('model/')
print('Model saved to model/') 