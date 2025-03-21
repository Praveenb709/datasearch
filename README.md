# FastAPI BigQuery App

This project is a FastAPI application that interacts with Google BigQuery to fetch records based on user-defined criteria. It accepts four input variables: District, Mandal, and two additional variable names and values, executes a SELECT query, and returns the results.

## Project Structure

```
fastapi-bigquery-app
├── src
│   ├── main.py                # Entry point of the FastAPI application
│   ├── models.py              # Data models for input validation
│   ├── services
│   │   └── bigquery_service.py # Logic for interacting with Google BigQuery
│   └── types
│       └── __init__.py        # Placeholder for custom types or interfaces
├── requirements.txt           # Project dependencies
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd fastapi-bigquery-app
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the FastAPI application:**
   ```bash
   uvicorn src.main:app --reload
   uvicorn fastapi-bigquery-app.src.main:app --reload
   
   ```

2. **Send a POST request to the endpoint:**
   Use a tool like Postman or curl to send a request to the `/your-endpoint` with the following JSON body:
   ```json
   {
       "District": "your_district_value",
       "Mandal": "your_mandal_value",
       "additional_variable_1": "value_1",
       "additional_variable_2": "value_2"
   }
   ```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.