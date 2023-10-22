# Crontab Decoder Tool

The Crontab Decoder Tool is a web application designed to assist users in understanding and interpreting crontab expressions. It provides a human-readable explanation for given crontab schedules, simplifying the task of cron job scheduling in Unix-like operating systems.

## Prerequisites

Ensure the following are installed on your system:

- Python 3
- pip (Python package installer)

## Setting Up & Running the Project

### 1. Clone the Repository

```bash
git clone [YOUR_REPOSITORY_LINK]
cd Crontab_Decode_Tool
```

### 2. Create & Activate a Virtual Environment

To avoid potential package conflicts, it's recommended to use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install django djangorestframework
```

### 4. Run Migrations (if any)

Apply database migrations with:

```bash
python3 manage.py migrate
```

### 5. Start the Server

```bash
python3 manage.py runserver
```

Now, open `http://localhost:8000/` in your web browser to use the Crontab Decoder Tool.

## Implementation Highlights

- **Django Backend**: Utilizes the Django web framework, ensuring a robust and scalable backend.
- **Django Rest Framework Integration**: Creates an API endpoint (`/decode/`) for frontend-backend interaction.
- **Decoding Logic**: Provides detailed explanations for crontab expressions, including special characters.
- **User Interface**: A straightforward UI built with HTML and JavaScript.
- **Data Validation**: Ensures valid crontab expressions and provides feedback on errors.

## Demonstrated Skills

This project showcases:

- Backend development using Django.
- API design with Django Rest Framework.
- Frontend integration using HTML and JavaScript.
- Data validation and error handling.
- Comprehensive documentation, as seen in this README.

