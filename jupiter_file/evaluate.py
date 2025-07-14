import pickle
import numpy as np
from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments
from sklearn.metrics import classification_report, confusion_matrix

# Load eval data
with open('eval_data.pkl', 'rb') as f:
    eval_data = pickle.load(f)

# Load label mapping
with open('label_mapping.pkl', 'rb') as f:
    label_mapping = pickle.load(f)

# Load model
model = AutoModelForSequenceClassification.from_pretrained('model/')

# Dummy training args for Trainer
training_args = TrainingArguments(output_dir='./results', per_device_eval_batch_size=8)

# Trainer
trainer = Trainer(model=model, args=training_args)

# Evaluate
predictions = trainer.predict(eval_data)
y_true = predictions.label_ids
y_pred = np.argmax(predictions.predictions, axis=1)

print('Accuracy:', np.mean(y_true == y_pred))
print('Unique y_true:', np.unique(y_true))
print('Unique y_pred:', np.unique(y_pred))
print('Label mapping:', label_mapping)

# Ensure target_names matches the unique labels in y_true and are strings
unique_labels = sorted(np.unique(y_true))
target_names = [str(label_mapping[i]) for i in unique_labels]

print(classification_report(y_true, y_pred, target_names=target_names))
print('Confusion Matrix:\n', confusion_matrix(y_true, y_pred)) 