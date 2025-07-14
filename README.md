# Sentiment Analysis

A RESTful API built with Flask-RestX for sentiment analysis.

## Features

- Flask-RestX API with versioning (v1)
- Environment-based configuration

## Prerequisites

- Python 3.12+
- pip

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd AI_Agent_WebApi
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── resources/
├── logs/
├── tests/
├── .env
├── main.py
├── requirements.txt
```

## Running the Application

1. Start the Flask development server:
```bash
flask run
```

2. Access the API documentation at:
```
http://localhost:5000/api/v1/
```

## Project setup
 in this you she .ipynb file run it and you get Model folder and label_mapping.pkl file add this file and folder in api/v1/models

## Logging

The application uses a structured logging system with the following features:
- Console logging for development
- Separate info and error log files with daily rotation
- 15-day retention period for logs
- Request ID tracking for each API call
- Log files stored in the `logs` directory

### Log Files
- `logs/log_info.log`: Contains all INFO level and above logs
- `logs/log_error.log`: Contains only ERROR level logs

Log files are automatically rotated at midnight and kept for 15 days.

### Log Format
Each log entry includes:
- Timestamp
- Logger name
- Log level
- Request ID (for tracking requests across log entries)
- Message

## Development

The project uses:
- Flask-RestX for API development
- pytest for testing

## License

This project is licensed under the MIT License.