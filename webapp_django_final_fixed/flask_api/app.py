from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
import logging
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Django server URL
DJANGO_BASE_URL = "http://localhost:8000"

# Set up logger
logger = logging.getLogger(__name__)

# For debugging
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/api/hostels', methods=['GET'])
def get_hostels():
    """
    Fetch all hostels from Django API
    """
    try:
        response = requests.get(f"{DJANGO_BASE_URL}/api/hostels/")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/hostels/<int:hostel_id>', methods=['GET'])
def get_hostel_detail(hostel_id):
    """
    Fetch detailed information about a specific hostel
    """
    try:
        response = requests.get(f"{DJANGO_BASE_URL}/api/hostels/{hostel_id}/")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/reviews', methods=['POST'])
def add_review():
    """
    Add a new review for a hostel
    """
    data = request.json
    try:
        # This would typically include authentication
        response = requests.post(
            f"{DJANGO_BASE_URL}/api/hostels/{data['hostel_id']}/review/",
            json=data
        )
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """Create a new booking via Django API"""
    try:
        # Get booking data from request
        booking_data = request.get_json()
        
        # Forward the request to Django
        response = requests.post(
            f'{DJANGO_BASE_URL}/api/bookings/',
            json=booking_data,
            headers={'Content-Type': 'application/json'}
        )
        
        # Return Django's response
        return jsonify(response.json()), response.status_code
        
    except Exception as e:
        print(f"Error in create_booking: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
