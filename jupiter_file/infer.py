import pickle
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Load label mapping
with open('label_mapping.pkl', 'rb') as f:
    label_mapping = pickle.load(f)

# Load model and tokenizer
model_name = 'distilbert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained('model/')

# Build pipeline
sentiment_pipe = pipeline('text-classification', model=model, tokenizer=tokenizer)

def predict_sentiment(text):
    result = sentiment_pipe(text)[0]
    label_index = int(result['label'].split('_')[-1])
    label_name = label_mapping[label_index]
    return f'Predicted Sentiment: {label_name} (Confidence: {result["score"]:.2f})'

# Example usage
if __name__ == '__main__':
    print(predict_sentiment('what the hell')) 