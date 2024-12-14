# Flask Application with Google Generative AI 
 
## Overview 
This is a Flask-based web application that incorporates Google Generative AI to create a "Cahier de Charge" (specification document) based on user inputs. The application includes user authentication (sign-up and login) with password hashing and a simple SQLite database for data storage. 
 
## Features 
- User registration and authentication (sign-up and login). 
- Integration with Google Generative AI to generate detailed "Cahier de Charge." 
- Password security with hashing. 
- SQLite database integration. 
 
## Requirements 
To run this application, ensure you have the following: 
 
- Python 3.7+ 
- Flask 
- Flask-SQLAlchemy 
- Werkzeug 
- Google Generative AI Python library 
 
## Setup Instructions 
 
1. Clone the Repository 
   bash 
   git clone <repository-url> 
   cd <repository-directory> 
    
 
2. Install Dependencies 
   Create a virtual environment and install the required Python packages: 
   bash 
   python3 -m venv venv 
   source venv/bin/activate # On Windows, use `venv\Scripts\activate` 
   pip install -r requirements.txt 
    
 
3. Set Up the Database 
   Initialize the SQLite database: 
   bash 
   flask shell 
   >>> from app import db 
   >>> db.create_all() 
   >>> exit() 
    
 
4. Set Google Generative AI API Key 
   Replace your-api-key in the genai.configure() line with your actual Google Generative AI API key: 
   python 
   genai.configure(api_key="your-api-key") 
    
 
5. Run the Application 
   Start the Flask development server: 
   bash 
   python app.py 
    
   The app will run at http://0.0.0.0:8080. 
 
## API Endpoints 
 
### 1. User Sign-Up 
   Endpoint: /signup   
   Method: POST   
   Request Body: 
   json 
   { 
     "fullname": "John Doe", 
     "phone": "123456789", 
     "email": "john@example.com", 
     "password": "password123" 
   } 
    
   Response: 
   json 
   { 
     "message": "User registered successfully!" 
   } 
    
 
### 2. User Login 
   Endpoint: /login   
   Method: POST   
   Request Body: 
   json 
   { 
     "email": "john@example.com", 
     "password": "password123" 
   } 
    
   Response: 
   json 
   { 
     "id": 1, 
     "fullname": "John Doe", 
     "phone": "123456789", 
     "email": "john@example.com" 
   } 
    
 
### 3. Generate Cahier de Charge 
   Endpoint: /generate   
   Method: POST   
   Request Body: 
   json 
   { 
     "name": "E-commerce Website", 
     "description": "A platform to buy and sell products online." 
   } 
    
   Response: 
   json 
   { 
     "status": "success", 
     "message": "Cahier de Charge created for E-commerce Website.", 
     "content": "Generated Cahier de Charge content here..." 
   } 
    
 
## Testing with Postman 
To test the API endpoints using Postman: 
 
1. Install Postman 
   Download and install Postman from https://www.postman.com/downloads/. 
 
2. Set Up API Requests 
   - Create a new request in Postman. 
   - For the Sign-Up endpoint: 
     - Set the method to POST. 
     - Use the URL: http://0.0.0.0:8080/signup. 
     - In the Body tab, select raw and set the format to JSON. 
     - Provide the user data as JSON. 
   - For the Login endpoint: 
     - Set the method to POST. 
     - Use the URL: http://0.0.0.0:8080/login. 
     - Provide the login credentials as JSON in the body. 
   - For the Generate Cahier de Charge endpoint: 
     - Set the method to POST. 
     - Use the URL: http://0.0.0.0:8080/generate. 
     - Provide the name and description as JSON in the body. 
 
3. Send Requests 
   - Click the Send button to execute the requests. 
   - View the response data in the Postman interface. 
 
## Project Structure 
```plaintext 
. 
├── app.py                 # Main application file 
├── requirements.txt       # Python dependencies 
├── users.db               # SQLite
# Flask Application with Google Generative AI 
 
## Overview 
This is a Flask-based web application that incorporates Google Generative AI to create a "Cahier de Charge" (specification document) based on user inputs. The application includes user authentication (sign-up and login) with password hashing and a simple SQLite database for data storage. 
 
## Features 
- User registration and authentication (sign-up and login). 
- Integration with Google Generative AI to generate detailed "Cahier de Charge." 
- Password security with hashing. 
- SQLite database integration. 
 
## Requirements 
To run this application, ensure you have the following: 
 
- Python 3.7+ 
- Flask 
- Flask-SQLAlchemy 
- Werkzeug 
- Google Generative AI Python library 
 
## Setup Instructions 
 
1. Clone the Repository 
   bash 
   git clone <repository-url> 
   cd <repository-directory> 
    
 
2. Install Dependencies 
   Create a virtual environment and install the required Python packages: 
   bash 
   python3 -m venv venv 
   source venv/bin/activate # On Windows, use `venv\Scripts\activate` 
   pip install -r requirements.txt 
    
 
3. Set Up the Database 
   Initialize the SQLite database: 
   bash 
   flask shell 
   >>> from app import db 
   >>> db.create_all() 
   >>> exit() 
    
 
4. Set Google Generative AI API Key 
   Replace your-api-key in the genai.configure() line with your actual Google Generative AI API key: 
   python 
   genai.configure(api_key="your-api-key") 
    
 
5. Run the Application 
   Start the Flask development server: 
   bash 
   python app.py 
    
   The app will run at http://0.0.0.0:8080. 
 
## API Endpoints 
 
### 1. User Sign-Up 
   Endpoint: /signup   
   Method: POST   
   Request Body: 
   json 
   { 
     "fullname": "John Doe", 
     "phone": "123456789", 
     "email": "john@example.com", 
     "password": "password123" 
   } 
    
   Response: 
   json 
   { 
     "message": "User registered successfully!" 
   } 
    
 
### 2. User Login 
   Endpoint: /login   
   Method: POST   
   Request Body: 
   json 
   { 
     "email": "john@example.com", 
     "password": "password123" 
   } 
    
   Response: 
   json 
   { 
     "id": 1, 
     "fullname": "John Doe", 
     "phone": "123456789", 
     "email": "john@example.com" 
   } 
    
 
### 3. Generate Cahier de Charge 
   Endpoint: /generate   
   Method: POST   
   Request Body: 
   json 
   { 
     "name": "E-commerce Website", 
     "description": "A platform to buy and sell products online." 
   } 
    
   Response: 
   json 
   { 
     "status": "success", 
     "message": "Cahier de Charge created for E-commerce Website.", 
     "content": "Generated Cahier de Charge content here..." 
   } 
    
 
## Testing with Postman 
To test the API endpoints using Postman: 
 
1. Install Postman 
   Download and install Postman from https://www.postman.com/downloads/. 
 
2. Set Up API Requests 
   - Create a new request in Postman. 
   - For the Sign-Up endpoint: 
     - Set the method to POST. 
     - Use the URL: http://0.0.0.0:8080/signup. 
     - In the Body tab, select raw and set the format to JSON. 
     - Provide the user data as JSON. 
   - For the Login endpoint: 
     - Set the method to POST. 
     - Use the URL: http://0.0.0.0:8080/login. 
     - Provide the login credentials as JSON in the body. 
   - For the Generate Cahier de Charge endpoint: 
     - Set the method to POST. 
     - Use the URL: http://0.0.0.0:8080/generate. 
     - Provide the name and description as JSON in the body. 
 
3. Send Requests 
   - Click the Send button to execute the requests. 
   - View the response data in the Postman interface. 
 
## Project Structure 
```plaintext 
. 
├── app.py                 # Main application file 
├── requirements.txt       # Python dependencies 
├── users.db               # SQLite
