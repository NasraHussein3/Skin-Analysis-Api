# Skin Care Analysis API

## Introduction

Welcome to the Skin Analysis API – your personal skincare companion, offering customized regimens tailored to your unique skin type. We base our recommendations on The Ordinary skincare products to help you achieve healthy and radiant skin.

**To see the API code/files, please click on the Master Branch of this repo**


In the development of this API, we used the following tools:

1. **Flask Web Framework:** We've implemented Flask, a web framework, to create the web application.

2. **Jsonify:** This library enables us to provide JSON responses, making it easy for users to understand and work with the data.

3. **Request:** The Request library allows us to handle incoming data, such as the JSON input provided by users.

## Endpoints

This API simplifies your skincare journey with four comprehensive endpoints:

### 1. Explore Available Skincare Data

- Endpoint: `/skincare`
- Description: Explore a dataset of skincare information, including detailed skincare routines and product recommendations. The information is tailored to specific skin types, which include:
  - Oily skin
  - Dry skin
  - Combination skin
  - Normal skin
  - Ageing skin
  - Acne-prone skin
  This endpoint offers insights into The Ordinary products.

### 2. Discover Your Ideal Routine

- Endpoint: `/skincare_routine`
- Description: Select your skin type from the following options:
  - Oily skin
  - Dry skin
  - Combination skin
  - Normal skin
  - Ageing skin
  - Acne-prone skin
  The API will provide a detailed skincare regimen, including cleansing, toning, serums, moisturizers, and UV protection, using premier products from The Ordinary.

### 3. List Available Skin Types

- Endpoint: `/skin_types`
- Description: View a comprehensive list of available skin types. This feature provides a reference to help you choose the skin type that best matches your needs, ensuring an accurate and tailored skincare routine.

### 4. Reset and Start Anew

- Endpoint: `/skincare_data`
- Description: Use this endpoint as a reset button to wipe out all existing skincare data. The API responds with a reassuring message: "All skincare data has been deleted."



# Skincare Database Access with Python

This Python script connects to a MySQL database and provides various functions to retrieve and manipulate data related to skincare information for users. It is designed to work with a skincare database named 'skincare' and uses the `mysql.connector` library for database connections. The script also defines a custom exception, `DbConnectionError`, to handle database connection errors.

## Database Connection

- The `_connect_to_db(db_name)` function establishes a connection to the MySQL database using credentials (user, password, and host) stored in a separate `config.py` file.

## Data Retrieval Functions

1. `get_skin_type(user)`: Retrieves a user's skin type from the database and prints the result.

2. `get_skin_routine(user)`: Retrieves a skincare routine recommendation for a user based on their skin type and prints the result.

3. `search_name(user, skincare)`: Searches for a user's skin type in the database and returns a list of skincare profiles matching the user's first name.

4. `get_all_skincare()`: Retrieves all skincare data from the database, including results, user information, and skin information, and prints the results.

5. `skin_profiles()`: Retrieves and prints combined information from the 'SkinInfo' and 'Results' tables, including skin info, recommended routines, and medication requirements.

## Data Deletion Function

- `delete_user_results(user)`: Deletes a user's skincare results from the 'Results' table and resets the user's data in the 'Users' table. This function can be used to remove a user's skincare information from the database.

## Execution

- The script executes the `get_all_skincare()` function when run as the main program. You can uncomment the line to `delete_user_results(user_to_delete)` to delete a specific user's data by providing their username.

Please ensure that you have the necessary MySQL credentials in the `config.py` file and that you've set up the 'skincare' database with the required tables and data before running this script.



## Get Started

To get started, check out the API documentation for each endpoint and enjoy a personalized skincare experience.


