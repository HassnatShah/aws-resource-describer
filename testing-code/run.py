# from app import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)

# import logging
# from app import create_app

# # Create the Flask app
# app = create_app()

# # Set up logging
# logging.basicConfig(level=logging.INFO)  # Set to DEBUG for more verbose output
# logger = logging.getLogger(__name__)

# @app.before_request
# def log_request_info():
#     logger.info(f"Request Path: {request.path}")
#     logger.info(f"Request Method: {request.method}")

# @app.after_request
# def log_response_info(response):
#     logger.info(f"Response Status: {response.status}")
#     return response

# if __name__ == '__main__':
#     app.run(debug=True)

import logging
from flask import Flask, request
from app import create_app

# Create the Flask app
app = create_app()

# Set up logging
logging.basicConfig(level=logging.INFO)  # Set to DEBUG for more verbose output
logger = logging.getLogger(__name__)

@app.before_request
def log_request_info():
    logger.info(f"Request Path: {request.path}")
    logger.info(f"Request Method: {request.method}")

@app.after_request
def log_response_info(response):
    logger.info(f"Response Status: {response.status}")
    return response

if __name__ == '__main__':
    app.run(debug=True)
