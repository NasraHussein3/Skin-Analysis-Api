from flask import Flask, jsonify, request
import skincare_data
from skincare_data import skincare_data

app = Flask(__name__)

# HERE BELOW ARE THE API END POINTS FOR THE SKIN ANALYSIS API
#First end point gets all skincare data

@app.route('/skincare')
def get_skincare():
    return jsonify(skincare_data)

#Second end point is to select skin type and receive skincare routine using API POST method

@app.route('/skincare', methods=['POST'])
def get_skincare_routine():
    data = request.get_json() # This part extracts the JSON data from the incoming POST request(user input)
    skin_type = data.get("skin_type")  # This part always makes sure there is an input from the user
    if skin_type in skincare_data:
        routine = skincare_data.get(skin_type) # This looks up the skin care routine from the skincare dictionary associated with the skin type
        return jsonify({"skin_type": skin_type, "skincare_routine": routine}) # This gives the user a JSON response which shows them the skin routine for their selected skin type.
    else:
        return jsonify({"error": "Invalid Skin type. Please Choose from the available options "}), 400
# Even through users will only have option of 6 skin types; basic error handling is good to have in an API


# Third Endpoint is to list all available skin types using API GET method
# We need to check if there are any skin types available and dict isnt empty then we produce a message that states whats available
# The available skin types are joined into a comma-separated string
# If the list is empty then we get another message.
@app.route('/skin_types', methods=['GET'])
def list_skin_types():
    skin_types = list(skincare_data.keys())
    if skin_types:
        message = "Available skin types are: " + ", ".join(skin_types)
        return jsonify({"message": message, "skin_types": skin_types})
    else:
        return jsonify({"message": "No skin types available"})


# Fourth Endpoint deletes all skincare data using the DELETE method
# Here we use the keyword Global, so we can access skincare_data outside of this function and able to delete data.
# the {} indicates the dictionary has been emptied out
# the result will be the Key Message with Value All Skincare data has been deleted.
@app.route('/skincare_data', methods=['DELETE'])
def delete_all_skincare_data():
    global skincare_data
    skincare_data = {}
    return jsonify({"message": "All skincare data has been deleted"})


if __name__ == "__main__":
    app.run(debug=True)

