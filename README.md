# Contact Management System

A full-stack contact management application built with Python Flask backend and React frontend.
I followed this tutorial : https://youtu.be/PppslXOR7TA?si=g8zblJhHTqcW1D83

## Project Structure

```
.
├── backend/
│   ├── __init__.py
│   ├── config.py        # Flask app configuration
│   ├── main.py         # Main application routes
│   ├── models.py       # Database models
│   └── requirements.txt # Python dependencies
└── frontend/
    ├── src/
    │   ├── App.jsx           # Main React component
    │   ├── ContactForm.jsx   # Contact creation/update form
    │   ├── ContactList.jsx   # Contacts display component
    │   ├── main.jsx         # React entry point
    │   └── *.css            # Styling files
    └── package.json         # Node.js dependencies
```

## Features

- Create new contacts with first name, last name, and email
- View all contacts in a tabular format
- Update existing contact information
- Delete contacts
- Responsive modal forms for create/update operations
- RESTful API backend with SQLite database
- Modern React frontend with hooks

## Setup

### Backend Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Run the Flask server:
```bash
python main.py
```
The backend will run on http://127.0.0.1:5000

### Frontend Setup

1. Install Node.js dependencies:
```bash
cd frontend
npm install
```

2. Start the development server:
```bash
npm run dev
```
The frontend will run on http://localhost:5173

## API Endpoints

- `GET /contacts` - Retrieve all contacts
- `POST /create_contact` - Create a new contact
- `PATCH /update_contact/<id>` - Update an existing contact
- `DELETE /delete_contact/<id>` - Delete a contact

## Technologies Used

- **Backend**:
  - Flask
  - SQLAlchemy
  - SQLite
  - Flask-CORS

- **Frontend**:
  - React
  - Vite
  - Modern JavaScript (ES6+)
  - CSS3

## Development

- Backend runs in debug mode for development
- Frontend includes hot module replacement (HMR)
- ESLint configuration for code quality
- Cross-Origin Resource Sharing (CORS) enabled

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
