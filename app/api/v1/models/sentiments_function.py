import pickle
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Load label mapping
with open('app/api/v1/models/label_mapping.pkl', 'rb') as f:
    label_mapping = pickle.load(f)

# Load model and tokenizer
model_name = 'distilbert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained('app/api/v1/models/model/')

# Build pipeline
sentiment_pipe = pipeline('text-classification', model=model, tokenizer=tokenizer)

def predict(text):
    result = sentiment_pipe(text)[0]
    label_index = int(result['label'].split('_')[-1])
    label_name = label_mapping[label_index]
    return {
        'label': label_name,
        'score': result['score']
    }

# # Example usage
# if __name__ == '__main__':
#     print(predict('what the hell')) 