# Personal Finance System

A beginner-friendly Python project to manage personal income and expenses using Object-Oriented Programming (OOP), CRUD operations, JSON file storage, the `os` module, and exception handling.

## Features

- Add income or expense transactions
- View all transactions
- Update transaction details
- Delete transactions
- Generate a simple finance report
- Store data persistently in a JSON file

## Technologies Used

- Python
- OOP (Classes and Objects)
- JSON for data storage
- `os` module for file and folder management
- Exception handling for safe input and file operations

## Project Structure

```text
Personal-Finance-System/
├── day18.py
├── finance_data/
│   └── transaction.json
└── day18.md
```

## How to Run

1. Save the code in a file named `main.py`.
2. Open a terminal in the project folder.
3. Run the program:

```bash
python main.py
```

## Menu Options

1. Add Transaction
2. View Transactions
3. Update Transaction
4. Delete Transaction
5. Generate Report
6. Exit

## Example JSON Data

```json
[
    {
        "id": 1,
        "type": "expense",
        "amount": 250.0,
        "category": "Food",
        "description": "Lunch"
    }
]
```

## Concepts Practiced

- **OOP**: `Transaction` and `PersonalFinanceSystem` classes.
- **CRUD**:
  - Create → Add transaction
  - Read → View transactions
  - Update → Modify transaction
  - Delete → Remove transaction
- **JSON Handling**: Save and load data from `transactions.json`.
- **OS Module**: Create folders and check file paths.
- **Exception Handling**: Handle invalid input and file-related errors.

## Future Improvements

- Add monthly budget tracking
- Search transactions by category or date
- Generate charts and graphs
- Store data in PostgreSQL instead of JSON

## Author

Built by **Shruti Tiwari** as a Python backend learning project.