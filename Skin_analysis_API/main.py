import requests
import json

def get_availability_by_date(date):
    result = requests.get(
        'http://127.0.0.1:5001/availability/{}'.format(date),
        headers={'content-type': 'application/json'}
    )
    return result.json()

def add_new_member(name, email, sink_info):

    member = {
         "name": name,
         "email": email,
         "skin_info": skin_type
    }

    result = requests.put(
        'http://127.0.0.1:5001/booking',
        headers={'content-type': 'application/json'},
        data=json.dumps(booking)
    )

    return result.json()


def display_availability(records):
    # Print the names of the columns.
    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} ".format(
        'NAME', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18'))
    print('-' * 105)

    # print each data item.
    for item in records:
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} ".format(
            item['name'], item['12-13'], item['13-14'], item['14-15'], item['15-16'], item['16-17'], item['17-18']
        ))


def run():
    print('☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️')
    print('Hello, welcome to ⭐Dreamderm ⭐')
    print('🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿')
    print()
    list_skin_types()
    print()
    skin_type = input('💟Choose your skin type. '
                 'Whether you have dry skin, oily skin, acne prone skin or a combination of all three, we have something for you！')

    get_skincare_routine(skin_type)
    print('####### AVAILABILITY #######')
    print()
    display_availability(slots)
    print()
    place_booking = input('Would you like to book an appointment (y/n)?  ')

    book = place_booking == 'y'

    if book:
        cust = input('Enter your name: ')
        stylist = input('Choose stylist (Peter, Maddie, Dominic): ')
        time = input('Choose time based on availability (e.g 15-16): ')
        add_new_booking(date, stylist, time, cust)
        print("Booking is Successful")
        print()
        slots = get_availability_by_date(date)
        display_availability(slots)

    print()
    print('See you soon!')




if __name__ == '__main__':
    run()