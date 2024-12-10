## Django Project Setup Guide


### 1. Clone the Repository

```bash
git clone https://github.com/ordenmeny/cringesite_1week.git
cd cringesite_1week
```

### 2. Set Up a Virtual Environment
```bash 
python -m venv venv
```
Windows:
```bash
venv\Scripts\activate
```


macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r req.txt
```

### 4. Configure the Database
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Start the Development Server
```bash
python manage.py runserver
```

The project will be accessible at:
http://127.0.0.1:8000/

### 6. Using the API (basic functionality)
Available Endpoints:
1) Create a Joke \
URL: /api/create-joke/ \
Method: POST \
Body (JSON):
    ```bash
    {
        "topic_input": "Example joke topic"
    } 
    ```
2) List All Jokes \
URL: /api/list-jokes/ \
Method: GET \
Description: list of all jokes.
3) Retrieve or Delete a Joke by ID \
URL: /api/retrieve/\<int:pk>/ \
Methods: \
GET: Retrieve details of a specific joke by ID. \
DELETE: Delete a specific joke by ID. \
Description: Use \<int:pk> to specify the joke's unique ID.

---


## API for authentication
#### URL Prefix
`api-auth/`


### 1. Authorization

**Endpoint:**  
`POST /auth/token/login/`

**Request Parameters:**  
- `username=<username>`  
- `password=<password>`

**Description:**  
Retrieve a token. The token should be saved on the client side.

---

### 2. Create a new user

**Endpoint:**  
`POST /auth/users/`

**Request Parameters:**  
- `username=<username>`  
- `password=<password>`
- `email=<email>`

---

### 3. Retrieve All Users 
(for admin only)

**Endpoint:**  
`GET /auth/users/`

**Headers:**  
`Authorization: Token <token>`

---

### 4. Retrieve Current User

**Endpoint:**  
`GET /auth/users/me/`

**Headers:**  
`Authorization: Token <token>`


