# Django Rest Test with React - ASEE
    
## Steps for Running Project

### Requirements

- **Python 3.9+**
- **Node.js 18+**
- **npm**
- **git**

### Clone the repository:

```bash
git clone https://github.com/aseedev/django-react-test.git
cd django-react-test
```

## Backend

### 1. Go to the root folder and perform the following commands:

`cd backend/`

### 2. Create and activate the virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
python manage.py migrate
python manage.py runserver
```

## Frontend

```bash
cd ../frontend
```

### 1. Installing packages

```bash
npm install
```

### 2. Run the application

```bash
npm run dev
```

> Make sure both frontend and backend are running.


## Assignment Instructions

You should implement the following tasks in this project:

1. **Create a Note model** in the Django backend with the following fields:
   - `title` (string, max 200 characters)
   - `content` (text)
   - `created_at` (datetime, auto created)

2. **Create a Django REST Framework (DRF) API** to perform CRUD operations for the Note model:
   - List all notes
   - Retrieve a specific note
   - Create a new note
   - Update a note
   - Delete a note

3. **Connect the API to the React frontend**:
   - Create a React component to **list all notes** from the API.
   - Create a React component to **view the details of a single note**.
   - Implement a **Delete button** in the detail view to remove the selected note via API.

4. **Setup React Router** to navigate between:
   - `/` (Notes list page)
   - `/notes/:id` (Note detail page)

5. Ensure both frontend and backend servers are running properly and connected via API.

6. Organize your code cleanly and follow best practices for both Django and React.

7. (Optional) Update the project README with any setup notes or instructions you feel are necessary.

---

**Goal:**  
Demonstrate your ability to integrate Django REST API with a React frontend using modern development practices.

