import os
import sqlite3
from groq import Groq
import json  # Import to handle JSON responses

# Initialize the Groq client with the API key
client = Groq(api_key="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")

# Connect to the SQLite database
def connect_db(db_path):
    try:
        conn = sqlite3.connect(db_path)
        print("Database connection successful.")
        return conn
    except sqlite3.Error as e:
        print(f"Error during database connection: {e}")
        return None

# Function to execute a SQL query and fetch results
def execute_query(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"SQL execution error: {e}")
        return None

# Function to display the structure of tables in the database
def display_table_structure(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    table_info = {}
    
    if tables:
        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            table_info[table_name] = [(column[1], column[2]) for column in columns]  # Column name and type

    return table_info

# Main function to run the chatbot
def main():
    # Connect to the database
    db_path = 'chinook.db'  # Replace with your actual database path
    conn = connect_db(db_path)
    if not conn:
        return  # Exit if there's a connection error
    
    # Display the structure of the database
    table_info = display_table_structure(conn)
    
    # Prepare the system message content with table information
    system_content = "You are a helpful assistant that converts user input into SQL queries. "
    system_content += "You should always return the response as a JSON object in the format {'query': '<SQL_QUERY>'}. "
    system_content += "The following are the tables and their attributes in the database:\n"
    
    for table_name, columns in table_info.items():
        system_content += f"\nTable: {table_name}\n"
        for column_name, column_type in columns:
            system_content += f" - {column_name}: {column_type}\n"
    
    print("\nChatbot is running. Type your query (type 'exit' to quit):")
    
    while True:
        user_input = input("User: ")

        if user_input.lower() == 'exit':
            break

        try:
            # Send user input to the Groq API to convert it into an SQL query
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": system_content
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ],
                model="llama3-8b-8192",
                response_format={"type": "json_object"},
            )

            # Parse the response to extract the SQL query as a JSON object
            response_json = json.loads(chat_completion.choices[0].message.content)
            sql_query = response_json.get('query')

            print(f"Generated SQL Query: {sql_query}")

            # Execute the generated SQL query
            results = execute_query(conn, sql_query)

            if results:
                # Print the results dynamically
                print("Results:")
                for row in results:
                    print(row)
            else:
                print("No results found.")
        
        except sqlite3.Error as e:
            print(f"SQL Error: {e}")
        except json.JSONDecodeError as e:
            print(f"JSON decoding error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
