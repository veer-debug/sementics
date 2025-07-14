from flask_restx import Resource, Namespace, fields
from flask import request
from app.api.v1.models.sentiments_function import predict

api = Namespace('sentiment', description='Sentiment analysis operations')

sentiment_input = api.model('SentimentInput', {
    'text': fields.String(required=True, description='Input text to analyze')
})

sentiment_output = api.model('SentimentOutput', {
    'result': fields.String(description='Sentiment result'),
    'confidence': fields.Float(description='Confidence score')
})



@api.route('/test')
class SentimentTest(Resource):
    @api.expect(sentiment_input)
    @api.marshal_with(sentiment_output)
    def post(self):
        """Analyze sentiment of input text"""
        data = request.json
        text = data.get('text', '')

        response = predict(text)
        result = response['label']
        print(f"Result: {result}")

        confidence = response['score']
        if result == 0:
            result = 'Positive'
        elif result == 1:
            result = 'Neutral / Formal'
        elif result == 2:
            result = 'Positive Feedback' 
        elif result == 3:
            result = 'Negative / No Sentiment'
        else:
            result = 'unknown'
       
        return {'result': result, 'confidence': confidence}