from flask import Flask, request, jsonify
import google.generativeai as genai
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
# Set up Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# Configure your Google Generative AI API Key
genai.configure(api_key="AIzaSyDOwFHLJc8rNydOyakxTQAiXdLfsQ9PTxI")

# Simulated user database
users = []
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'fullname': self.fullname,
            'phone': self.phone,
            'email': self.email
        }

with app.app_context():
    db.create_all()

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    hashed_password = generate_password_hash(data['password'])
    new_user = User(
        fullname=data['fullname'],
        phone=data['phone'],
        email=data['email'],
        password=hashed_password
    )
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Phone or email already exists'}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'Invalid credentials'}), 401

# Define function to generate content
def generate_cahier_content(name, description):
    try:
        # Use the Generative Model to generate content
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Generate a detailed Cahier of Charge for {name}. Description: {description} as text not mark down"

        # Generate content using the new method
        response = model.generate_content(prompt)

        # Extract and return the generated content
        return response.text

    except AttributeError as e:
        return f"AttributeError: {e}"
    except Exception as e:
        return f"Error: {e}"


# Route for user signup
@app.route('/signup', methods=['POST'])
def signup():
    # Get user data from request
    data = request.get_json()
    fullname = data.get('fullname')
    phone = data.get('phone')
    email = data.get('email')
    password = data.get('password')

    # Validate input
    if not fullname or not phone or not email or not password:
        return jsonify({'message': 'All fields are required!'}), 400

    # Check if user already exists
    for user in users:
        if user['email'] == email:
            return jsonify({'message': 'User with this email already exists!'}), 400

    # Hash the password for security
    hashed_password = generate_password_hash(password)

    # Save user data to the simulated database
    user = {
        'fullname': fullname,
        'phone': phone,
        'email': email,
        'password': hashed_password
    }
    users.append(user)

    return jsonify({'message': 'User registered successfully!'}), 201

# # Route for user login
# @app.route('/login', methods=['POST'])
# def login():
#     # Get login data from request
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')

#     # Validate input
#     if not email or not password:
#         return jsonify({'message': 'Email and password are required!'}), 400

#     # Find user by email
#     user = next((user for user in users if user['email'] == email), None)
#     if not user:
#         return jsonify({'message': 'User not found!'}), 404

#     # Verify password
#     if not check_password_hash(user['password'], password):
#         return jsonify({'message': 'Invalid credentials!'}), 401

#     return jsonify({'message': f'Welcome, {user["fullname"]}!'}), 200

# Flask route to handle POST requests for generating Cahier
@app.route('/generate', methods=['POST'])
def generate_cahier():
    try:
        data = request.get_json()

        # Check if 'name' and 'description' are present in the request body
        if not data.get('name') or not data.get('description'):
            return jsonify({"status": "error", "message": "Both 'name' and 'description' are required"}), 400

        name = data.get("name")
        description = data.get("description")

        # Generate Cahier content using Google Generative AI
        content = generate_cahier_content(name, description)

        return jsonify({
            "status": "success",
            "message": f"Cahier de Charge created for {name}.",
            "content": content
        })

    except Exception as e:
        return jsonify({"status": "failure", "message": str(e)}), 500

# Start the Flask server
if __name__ == '__main__':
    app.run(port=8080, host="0.0.0.0")
