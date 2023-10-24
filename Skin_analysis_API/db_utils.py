# Import modules and credentials
import mysql.connector
from config import USER, PASSWORD, HOST

# This is a custom exception class that is raised if there is an issue with the database
class DbConnectionError(Exception):
    pass

# Created a function to establish a connection to the database using credentials from config.py
def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx

# Have created 6 Functions including a delete function.
# Each funtion retrieves information for the user from the skincare database using a SQL query and prints the results
def get_skin_type(user):
    try:
        db_name = 'skincare'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: {}\n".format(db_name))

        query = """SELECT Skin_info FROM SkinInfo WHERE SkinInfoID IN(
            SELECT SkinInfoID FROM Users WHERE FirstName = '{}')""".format(user)

        cur.execute(query)
        result = cur.fetchall()
        skin_type = result

        for i in result:
            print(i)
        cur.close()

    # Using mysql exception to make a more specific exception to help with troubleshooting issues
    except mysql.connector.Error as e:
        raise DbConnectionError("Failed to connect to DB: {e}")

    else:
        if db_connection:
            db_connection.close()
            print('\nDB connection is closed\n')


def get_skin_routine(user):
    try:
        db_name = 'skincare'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: {}\n".format(db_name))

        query = """ SELECT Skincare_routine FROM Results WHERE ResultsID IN(
        SELECT ResultsID FROM Users WHERE UserID In(
        SELECT UserID FROM UserInfo WHERE Skin_type = '{}'))""".format(user)

        cur.execute(query)
        result = cur.fetchall()
        skin_type = result

        for i in result:
            print(i)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to connect to DB")
    else:
        if db_connection:
            db_connection.close()
            print('\nDB connection is closed\n')

            return result


def search_name(user, skincare):
    try:
        db_name = 'skincare'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: {}\n".format(db_name))

        query = """SELECT Skin_type FROM SkinInfo WHERE UserID IN(
        SELECT UserID FROM Users WHERE FirstName = '{}')""".format(user)

        cur.execute(query)
        result = cur.fetchall()
        skin_type = result

        for i in result:
            print(i)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to connect to DB")
    else:
        if db_connection:
            db_connection.close()
            print('\nDB connection is closed\n')

    return [element for element in skincare if element['FirstName'] == user]


def get_all_skincare():
    try:
        db_name = 'skincare'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: {}\n".format(db_name))

        query = """
        SELECT * FROM Results;
        SELECT * FROM Users;
        SELECT * FROM SkinInfo;
        """

        cur.execute(query)
        result = cur.fetchall()
        skin_type = result

        for i in result:
            print(i)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to connect to DB")
    else:
        if db_connection:
            db_connection.close()
            print('\nDB connection is closed\n')

            return result


def skin_profiles():
    try:
        db_name = 'skincare'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: {}\n".format(db_name))

        query = """
        SELECT *
        SkinInfo.Skin_Info AS "Skin Info",
        Results.Recommended_products AS "Recommended Routine",
        SkinInfo.Medication AS "Medication Required"
        FROM
        SkinInfo
        INNER JOIN
        Results ON SkinInfo.ResultsID = Results.ResultsID;
        """

        cur.execute(query)
        result = cur.fetchall()

        # iterate over the result and print info from each row
        for row in result:
            # prints the 1st element (index 0) in each row related to skin info.
            print("Skin Info:", row[0])
            # prints 2nd element (index 1) in each row related to a recommended skincare routine.
            print("Recommended Routine:", row[1])
            # prints 3rd element (index 2) related to medication requirements.
            print("Medication Required:", row[2])

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to connect to DB")
    else:
        if db_connection:
            db_connection.close()
            print('\nDB connection is closed\n')

            return result


def delete_user_results(user):
    try:
        db_name = 'skincare'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: {}\n".format(db_name))

        # delete the user's results from the results table
        delete_results_query = ("DELETE FROM Results WHERE Skin_info_ID IN (SELECT SkinInfoID "
                                "FROM SkinInfo WHERE Skin_info = %s")
        cur.execute(delete_results_query, (user,))

        # Reset the user's data in the Users table
        reset_user_query = "UPDATE Users SET ResultsID = NULL, SkinInfoID = NULL WHERE FirstName = %s"
        cur.execute(reset_user_query, (user,))

        # commit the changes
        db_connection.commit()
        print("Deleted results for {user} and reset the user data.")

    except Exception:
        raise DbConnectionError("Failed to connect to DB")
    else:
        if db_connection:
            db_connection.close()
            print('\nDB connection is closed\n')


if __name__ == '__main__':
    get_all_skincare()
    # user_to_delete = "user name"
    # delete_user_results(user_to_delete)