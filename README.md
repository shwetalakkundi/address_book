Address Book Application
========================

Overview
--------

This project is a sophisticated **Address Book API** built using **FastAPI**. The application demonstrates an MVC (Model-View-Controller) architecture and uses **SQLite** as the database.

### Features

-   **CRUD Operations**: Full CRUD functionality for managing addresses.
-   **Distance Calculation**: Retrieve addresses within a specified distance from given coordinates.
-   **Data Validation**: Input data validation using **Pydantic** models.

Project Structure
-----------------

The project follows the MVC architecture



`address_book/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── views.py
│   ├── controllers.py
│   ├── database.py
│   ├── schemas.py
│   ├── utils.py
│   ├── logging_config.py
│   └── config.py
│
├── requirements.txt
└── README.md`


Setup and Installation
----------------------

### Prerequisites

-   Python 3.7+
-   Virtual Environment (recommended)

### Installation

1.  **Clone the Repository**

    `git clone [<repository-url>](https://github.com/shwetalakkundi/address_book.git)
    cd address_book`

2.  **Set up a Virtual Environment**

    `python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate``

3.  **Install Dependencies**

    `pip install -r requirements.txt`

4.  **Initialize the Database**

    Run the following command to set up the SQLite database:


    `python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"`

### Running the Application

1.  **Start the FastAPI Server**

    Use `uvicorn` to start the server:

    `uvicorn app.main:app --reload`

2.  **Access the API Documentation**

    Visit http://localhost:8000/docs to access the interactive Swagger UI.


### Usage

#### Create an Address

-   **Endpoint**: `POST /addresses/`

-   **Request Body**:

    `{
      "street": "123 Main St",
      "city": "Anytown",
      "state": "CA",
      "zipcode": "12345",
      "latitude": 37.7749,
      "longitude": -122.4194
    }`

#### Retrieve an Address

-   **Endpoint**: `GET /addresses/{address_id}`

#### Update an Address

-   **Endpoint**: `PUT /addresses/{address_id}`
-   **Request Body**: Same as create

#### Delete an Address

-   **Endpoint**: `DELETE /addresses/{address_id}`

#### Get Addresses Within Distance

-   **Endpoint**: `GET /addresses/`
-   **Query Parameters**: `lat`, `lon`, `distance`
