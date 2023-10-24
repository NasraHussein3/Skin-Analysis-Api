import requests
import json

byebye = "💬 We're sorry to see you go. 👋  Have a great day!"

def show_skin_type():
    print()
    print('💟 Step 1: Choose your skin type')
    print(
        '💬 Whether you have dry skin, oily skin, acne-prone skin, or a combination of all three, we have something for you!')
    print('Skin Types:')
    skin_types = requests.get('http://127.0.0.1:5001/skintype').json()
    for idx, skin_type in enumerate(skin_types, start=1):
        print(f" 💫 {idx}: {skin_type}")

    choice = input("💬 Enter the number corresponding to your skin type (unknown: 0): ")

    if choice == '0':
        print()
        response = input("💟 Don't worry; become a member, and we'll give you a free skin test. (y/n)")
        if response == 'n':
            print(byebye)
        elif response == 'y':
            pass
    else:
        skin_type = skin_types[int(choice) - 1]
        daily_routine_by_skintype(skin_type)

def daily_routine_by_skintype(skintype):
    print()
    print('💟 Step 2: Build your routine')
    routine = requests.get(f'http://127.0.0.1:5001/daily-routine/{skintype}').json()
    print(f'Daily Routine for {skintype}:')
    for idx, step in enumerate(routine, start=1):
        if idx >= 2:  # Start from the third column
            print(f"💧{idx - 1}: {step}")

def add_new_member():
    print()
    print('💟 Step 3: Become a Member')
    print("💬 We'll share the latest skincare news and help you build your dream skin.")
    response = input("💬 Enter 'y' to continue or 'n' to exit: ")

    if response == 'n':
        print(byebye)
    else:
        FirstName = input("✏️ First Name: ")
        LastName = input("✏️ Last Name: ")
        Email = input("✏️ Email Address: ")
        SkinType = input("✏️ Skin Type: ")
        Age = int(input("✏️ Age: "))
        add_new_member_to_api(FirstName, LastName, Email, SkinType, Age)
        print("All steps have been completed. Thank you for choosing us!")


def add_new_member_to_api(FirstName, LastName, Email, SkinType, Age):
    data = {
        "FirstName": FirstName,
        "LastName": LastName,
        "Email": Email,
        "SkinType": SkinType,
        "Age": Age
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://127.0.0.1:5001/members', headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        print("Member added successfully.")
    else:
        print(f"Failed to add member: {response.json()}")

def delete_member(email):
    try:
        # Call the API to delete a member by email
        response = requests.delete(f'http://127.0.0.1:5001/members/{email}')
        if response.status_code == 200:
            print("Member deleted successfully.")
        else:
            print("Failed to delete member.")
    except Exception as e:
        print(f"Error: {str(e)}")

def run():
    print('☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️')
    print('Hello, welcome to ⭐Dreamderm ⭐')
    print('🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿')
    print()
    print('💬 We are skin experts. 🔍')
    response = input("💬 Let's start the skincare journey! (y/n): ")

    if response == 'n':
        print(byebye)
    elif response == 'y':
        show_skin_type()
        response = input("💬 Learn more about the secret of the skin? 📖 (y/n): ")
        if response == 'n':
            print(byebye)
        elif response == 'y':
            add_new_member()

    # After the user has completed the steps
    response = input("💬 Enter 0 if you have opted out, or 1 if you would like to withdraw your membership: ")
    if response == '0':
        print("💬 You have opted out. 👋 Have a great day!")
    elif response == '1':
        # Call the function to delete the member's account (you need to implement this function)
        email = input("❌ Enter your email to confirm membership withdrawal: ❌")
        delete_member(email)

if __name__ == '__main__':
    run()