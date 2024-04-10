# phase-4-week-1-flask-code-challenge

Flask Message Board is a simple web application built with Flask that allows users to create, read, update, and delete records.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Dependencies](#dependencies)
- [Author](#author)
- [License](#license)

## Features

- Create new record with a body and username.
- Retrieve all records.
- Update a record.
- Delete a record.

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:Brian-Mariga/phase-4-week-1-flask-code-challenge.git
   ```

2. Navigate to the project directory:

   ```bash
   cd phase-4-week-1-flask-code-challenge
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Ensure you have set up your database URI in config.py.

1. Run the Flask application:

   ```bash
   python app.py

   ```

2. Access the application<br>
   In your web browser access http://localhost:5555.

## API Endpoints

1. GET /restaurants: Retrieves all restaurants.
2. GET /restaurants/:id: Retrieves a specific restaurant by ID if it exists.
3. DELETE /restaurants/:id: Deletes a specific restaurant by ID if it exists.
4. GET /pizzas: Retrieves all the pizzas.
5. POST /restaurant_pizzas: Create a new RestaurantPizza that is associated with an existing Pizza and Restaurant.

## Dependencies

- Flask
- Flask-CORS
- Flask-Migrate
- SQLite

## Author

Brian James Mariga

## License

This project is licensed under the MIT License.
