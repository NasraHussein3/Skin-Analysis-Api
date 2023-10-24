![Local Image](./dream-cover.jpg)

Welcome to the **Dream** team's README! We are a group of six enthusiastic girls who are passionate about learning and sharing knowledge in the world of coding.

## Meet the Team

- **Name**
  - :octocat: **GitHub:** [GitHub Profile](URL)
  - :thought_balloon: **Why I'm doing the course:** *I believe...*
  - :star2: **Favorite Topic:** ***example*** - *Reason*
  - :plate_with_cutlery: **Favorite Food:** 

- **Nasra Hussein**
  - :octocat: **GitHub:** [@NasraHussein3](https://github.com/NasraHussein3)
  - :thought_balloon: **Why I'm doing the course:** *I love everything Front-end web development and I know CFG will help me excelle in this*
  - :star2: **Favorite Topic:** ***Javascript*** 
  - :plate_with_cutlery: **Favorite Food:** *Concrete cake with custard*

- **Name**
  - :octocat: **GitHub:** [Mimi Brown](https://github.com/MimiCode21)
  - :thought_balloon: **Why I'm doing the course:** I wanted a career change and was introduced to cfg and thought it was such an amazing opportunity and the rest is history.
  - :star2: **Favorite Topic:My favourite topic is web development. -  love the creative aspect of building a website and seeing all that code coming to life in front of your eyes.
  - :plate_with_cutlery: **Favorite Food: Caribbean, specifically Jamaican it’s just unmatched 😋

- **Name**
  - :octocat: **GitHub:** [GitHub Profile](URL)
  - :thought_balloon: **Why I'm doing the course:** *...*
  - :star2: **Favorite Topic:** ***example*** - *Reason*
  - :plate_with_cutlery: **Favorite Food:** 

- **Name**
  - :octocat: **GitHub:** [GitHub Profile](URL)
  - :thought_balloon: **Why I'm doing the course:** *I believe...*
  - :star2: **Favorite Topic:** ***example*** - *Reason*
  - :plate_with_cutlery: **Favorite Food:**

- **Remi - Rongrong**
  - :octocat: **GitHub:** [@sherlkk](https://github.com/sherlkk)
  - :thought_balloon: **Why I'm doing the course:** *I believe that in our rapidly advancing digital world, coding is the key to unlocking limitless opportunities for problem-solving, creativity, and making a positive impact on society.*
  - :star2: **Favorite Topic:** ***Machine Learning*** - *I love exploring the endless possibilities.*
  - :plate_with_cutlery: **Favorite Food:** *Potato* :potato: *Ice Cream* :ice_cream: *Chips* :fries: *Popcorn* :popcorn:

## Our Focus

As a team, we are dedicated to becoming full-stack developers. Our journey encompasses both front-end and back-end development, and we aim to create complete, user-friendly web applications.

## Our Slogan

***"Coding Dreams into Reality"***

We are not just dreamers; we are doers. Together, we transform our coding dreams into reality!


# Connecting API to Database

## This code connects to the MySQL database called Skincare. It performs various database operations, and defines several functions for querying, managing and deleting data. 

## Here we will break down what is happening through the code.

### First we import mysql.connector which is a module and is used to interact with the MySQL database ‘Skincare’.

### Next we put from config import USER, PASSWORD, HOST: which imports the USER, PASSWORD, and HOST constants from the config.py module, which contain the database credentials.

### class DbConnectionError(Exception): is used as it can be raised if there is an issue connecting to the database.

### _connect_to_db(db_name): Our first function connects us to the database. It takes the database name as an argument and establishes a connection to the MySQL database using the credentials imported from config. It then returns the database connection object.

### get_skin_type(user): This function retrieves the skin type information for a user with the given first name. It first connects to the database using _connect_to_db. Then, it constructs and executes a SQL query to fetch the skin type based on the user's first name. It prints the results and closes the cursor and database connection.

### get_skin_routine(user): This function retrieves the skincare routine for a user based on their skin type. It constructs a SQL query and prints the results.

### search_name(user, skincare): This function retrieves the skin type information from the database and filters a list of skincare information by matching the user's first name and returns the filtered results.

### get_all_skincare(): This function connects to the database, executes a multi-statement SQL query to fetch data from multiple tables (Results, Users, SkinInfo), and prints the results.

### skin_profiles(): This function retrieves skin information by performing an SQL INNER JOIN operation between the SkinInfo and Results tables. It then prints the results, including skin info, recommended routine, and medication required.

### delete_user_reesults(user): This function deletes a user's results from the "SkinInfo” table and reset the user's data in the "Users" table.

### if __name__ == '__main__':: This is the starting point of the script when it's executed as the main program.

### get_all_skincare(): When the script is run, it calls the get_all_skincare function, which retrieves and prints data from the database.


# Main.py

## The main.py interacts with the client side API for skincare-related data. It provides a command-line interface for users to perform the following actions:

### get_skincare_routine(): This function allows the user to retrieve a skincare routine by providing their skin type as input. The script sends a POST request to the specified API endpoint (/skincare/skincare) with the user's input, and if the response status code is 200 (OK), it prints the skin type and skincare routine.

### list_skin_types(): This function lists available skin types. It sends a GET request to the /skin_types endpoint, and if the response status code is 200, it prints the available skin types.

### delete_all_skincare_data(): This function is used to delete all skincare data. It sends a DELETE request to the /skincare_data endpoint. If the response status code is 200, it confirms that all skincare data has been deleted.

### The script runs in a loop, displaying a menu of options for the user. The user can select an option by entering the corresponding number. The available options are to get a skincare routine, list available skin types, delete all skincare data, or exit the script.

### The script relies on the requests library to make HTTP requests to the Flask API. It interacts with the API by sending different types of requests (POST, GET, DELETE) to specific endpoints, and it processes the API responses accordingly.

### This shows how to interact with the skincare API and perform essential actions related to skincare data management.


