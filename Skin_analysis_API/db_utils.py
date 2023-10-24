import mysql.connector
from config import USER, PASSWORD, HOST

class DbConnectionError(Exception):
    pass

def get_skintype_list():
    try:
        # Establish a connection to the MySQL database
        db_connection = mysql.connector.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            database="skincareme"
        )
        cursor = db_connection.cursor()

        # Execute a query to fetch all skin types from the 'SkinType' column
        cursor.execute("SELECT DISTINCT SkinType FROM dailyroutine")
        skintypes = [row[0] for row in cursor.fetchall()]

        return skintypes

    except mysql.connector.Error as err:
        raise DbConnectionError(f"Failed to read data from DB: {err}")

    finally:
        if 'db_connection' in locals():
            db_connection.close()
            print("DB connection is closed")

def get_daily_routine(skintype):
    try:
        db_connection = mysql.connector.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            database="skincareme"
        )
        cursor = db_connection.cursor()

        # Execute a query to fetch the daily routine based on the skin type
        cursor.execute("SELECT * FROM dailyroutine WHERE SkinType = %s", (skintype,))
        daily_routine = cursor.fetchone()

        return daily_routine

    except mysql.connector.Error as err:
        raise DbConnectionError(f"Failed to read data from DB: {err}")

    finally:
        if 'db_connection' in locals():
            db_connection.close()
            print("DB connection is closed")

def add_member(FirstName, LastName, Email, SkinType, Age):
    try:
        db_connection = mysql.connector.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            database="skincareme"
        )
        cursor = db_connection.cursor()

        # Remove the "ID" field from the insert query since it's auto-incremented
        insert_query = "INSERT INTO members (FirstName, LastName, Email, SkinType, Age) VALUES (%s, %s, %s, %s, %s)"
        data_to_insert = (FirstName, LastName, Email, SkinType, Age)
        cursor.execute(insert_query, data_to_insert)
        db_connection.commit()

    except mysql.connector.Error as err:
        raise DbConnectionError(f"Failed to write data to DB: {err}")

    finally:
        if 'db_connection' in locals():
            db_connection.close()
            print("DB connection is closed")
def delete_member_by_email(email):
    try:
        # Establish a database connection
        db_connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database="skincareme"
        )

        # Create a cursor object to execute SQL queries
        cursor = db_connection.cursor()

        # Define the SQL query to delete a member by email
        delete_query = "DELETE FROM members WHERE Email = %s"
        cursor.execute(delete_query, (email,))

        # Commit the changes and close the cursor and connection
        db_connection.commit()
        cursor.close()
        db_connection.close()

    except Exception as e:
        raise DbConnectionError("Failed to delete member")

    return "Member deleted successfully"

if __name__ == '__main__':
    # Test the functions
    skintypes = get_skintype_list()
    print("Skin Types:", skintypes)

    skin_type = "Oily skin"
    daily_routine = get_daily_routine(skin_type)
    print(f"Daily Routine for {skin_type}:", daily_routine)

    add_member("Test", "Test", "test@email.com", "Oily skin", 100)
    print("Member added successfully")

    delete_member_by_email('bb')