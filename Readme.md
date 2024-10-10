Text-to-SQL Query Chatbot
This repository contains a chatbot that converts natural language queries into SQL queries and executes them against a SQLite database. The project leverages the Groq API for natural language processing.
Features
- Converts user input in plain English to SQL queries.
- Executes the generated SQL queries on an SQLite database.
- Returns results from the database and displays them in a structured format.
Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
Prerequisites
Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- SQLite installed on your machine (optional if you have a pre-existing SQLite database)
- Groq API key for accessing the API
- A valid SQLite database (chinook.db in this example)
Installation
1. Clone the repository:

```bash
git clone https://github.com/your-username/text-to-sql-chatbot.git
cd text-to-sql-chatbot
```

2. Create and activate a virtual environment:

On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```
Environment Setup
1. Groq API Key:

You will need a Groq API key to communicate with the Groq platform.

- Sign up at Groq.com.
- Generate an API key.
- Create a .env file in the root directory of the project and add your API key:
```bash
touch .env
```

In the .env file, add:
```
GROQ_API_KEY=your_groq_api_key_here
```

2. SQLite Database:

Make sure you have the correct SQLite database (chinook.db used in this example) in the project root or modify the path in main() to point to your own database.
Usage
1. Running the Chatbot:

After setting up the environment, you can run the chatbot:
```bash
python main.py
```

2. Interacting with the Chatbot:

The chatbot will prompt you to type a query.
Example:
```
User: How many tracks of the genre ‘Metal’ exist?
```

To quit, type `exit`.
Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Push to your branch and submit a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.
