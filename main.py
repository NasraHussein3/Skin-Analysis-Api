import requests

# Define the base URL for your Flask API
base_url = 'http://localhost:5000'  # Replace with the actual URL of your API


# Function to get skincare routine by skin type
def get_skincare_routine():
    skin_type = input("Enter your skin type: ")
    data = {"skin_type": skin_type}

    response = requests.post(f"{base_url}/skincare", json=data)

    if response.status_code == 200:
        result = response.json()
        print(f"Skin Type: {result['skin_type']}")
        print(f"Skincare Routine: {result['skincare_routine']}")
    else:
        print(f"Error: {response.json()['error']}")


# Function to list available skin types
def list_skin_types():
    response = requests.get(f"{base_url}/skin_types")

    if response.status_code == 200:
        result = response.json()
        print(result['message'])
        print(f"Available Skin Types: {', '.join(result['skin_types'])}")
    else:
        print(f"Error: {response.json()['message']}")


# Function to delete all skincare data
def delete_all_skincare_data():
    response = requests.delete(f"{base_url}/skincare_data")

    if response.status_code == 200:
        result = response.json()
        print(result['message'])
    else:
        print(f"Error: {response.json()['message']}")


if __name__ == '__main__':
    while True:
        print("\nOptions:")
        print("1. Get Skincare Routine by Skin Type")
        print("2. List Available Skin Types")
        print("3. Delete All Skincare Data")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            get_skincare_routine()
        elif choice == '2':
            list_skin_types()
        elif choice == '3':
            delete_all_skincare_data()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")