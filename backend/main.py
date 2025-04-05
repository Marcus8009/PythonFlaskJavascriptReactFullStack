import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import request, jsonify
from backend.config import app, db
from backend.models import Contact

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Contacts API"})

@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

@app.route('/create_contact', methods=['POST'])
def create_contact():
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    
    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include a first name, last name, and email."}),
            400,
        )
    
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message":str(e)}), 400
    return jsonify({"message": "User created!"}), 201

@app.route("/update_contact/<int:user_id>", methods=['PATCH'])
def update_contact(user_id):
    contact = Contact.query.get(user_id)
    
    if not contact:
        return jsonify({"message": "User not found!"}), 404
    
    try:
        data = request.json
        if not data:
            return jsonify({"message": "No update data provided"}), 400
        
        # Validate email if it's being updated
        if "email" in data and not data["email"]:
            return jsonify({"message": "Email cannot be empty"}), 400
            
        contact.first_name = data.get("firstName", contact.first_name)
        contact.last_name = data.get("lastName", contact.last_name)
        contact.email = data.get("email", contact.email)

        db.session.commit()
        return jsonify({
            "message": "User updated!",
            "contact": contact.to_json()
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Update failed: {str(e)}"}), 400

@app.route("/delete_contact/<int:user_id>", methods=['DELETE'])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found!"}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted!"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
