from google.cloud import bigquery
from typing import Any, List, Dict
import os

# Set the path to the service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/dev/Documents/Data_search/datasearch/sucharith-project1-60513598121e.json"

def fetch_records(
    district: str,
    mandal: str,
    additional_var1_name: str,
    additional_var1_value: Any,
) -> List[Dict[str, Any]]:
    print("Function Arguments:")
    print("District:", district)
    print("Mandal:", mandal)
    print("Additional Var1 Name:", additional_var1_name)
    print("Additional Var1 Value:", additional_var1_value)
    

    # Initialize BigQuery client using the service account
    client = bigquery.Client()

    # Define the query with values directly substituted
    query = f"""
    SELECT *
    FROM `sucharith-project1.Datasearch.data`
    WHERE District = "{district}"
        AND `Mandal Name` = "{mandal}"
        AND `{additional_var1_name}` = "{additional_var1_value}"
    """
    print("Query:", query)

    # Execute the query
    query_job = client.query(query)
    results = query_job.result()

    # Convert the results to a list of dictionaries
    response = [dict(row) for row in results]

    return response