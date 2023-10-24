from flask import Flask, jsonify, request
from db_utils import get_skintype_list, get_daily_routine, add_member, delete_member_by_email

app = Flask(__name__)

# GETTING ALL SKIN TYPES
@app.route('/skintype')
def get_skintype():
    res = get_skintype_list()
    return jsonify(res)

# GETTING THE DAILY ROUTINE FOR A SPECIFIC SKIN TYPE
@app.route('/daily-routine/<skintype>')
def get_dailyroutine(skintype):
    res = get_daily_routine(skintype)
    return jsonify(res)

# ADDING A NEW MEMBER
@app.route('/members', methods=['POST'])
def new_member():
    data = request.json
    ID = data.get("ID")
    FirstName = data.get("FirstName")
    LastName = data.get("LastName")
    Email = data.get("Email")
    SkinType = data.get("SkinType")
    Age = data.get("Age")

    if not FirstName or not LastName or not Email or not SkinType or not Age:
        return jsonify({"error": "Missing required data"}), 400

    try:
        add_member(FirstName, LastName, Email, SkinType, Age)
        return jsonify({"message": "Member added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETING A MEMBER BASED ON EMAIL ADDRESS
@app.route('/members/<email>', methods=['DELETE'])
def delete_member(email):
    try:
        # Call a function to delete a member by email from db_utils.py
        delete_member_by_email(email)  # You need to implement this function in db_utils.py

        # Assuming delete_member_by_email returns a success message on successful deletion
        return jsonify({"message": "Member deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
