from flask import Flask
from flask_restx import Api
from flask_log_request_id import RequestID
import yaml
import logging.config
import os

def setup_logging(app):
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
    os.makedirs(log_dir, exist_ok=True)
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logging.yaml')
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            logging.config.dictConfig(config)

def create_app():
    app = Flask(__name__)
    setup_logging(app)
    logger = logging.getLogger('flask_restx_api')
    RequestID(app)
    api = Api(
        app,
        version='1.0',
        title='Sentiment Analysis',
        description='A RESTful API for sentiment analysis operations',
        doc='/',
        prefix='/api/v1'
    )
    from .api.v1.resources.sentiment import api as sentiment_ns
    api.add_namespace(sentiment_ns, path='/sentiment')
    logger.info('Application started successfully')
    return app