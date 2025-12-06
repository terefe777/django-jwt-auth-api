# 🔐 Django JWT Authentication API  
A production-ready authentication system built with **Django**, **Django REST Framework**, **JWT**, **PostgreSQL**, and **Docker**.  
This project includes user registration, login, logout, profile management, token refresh, token blacklist, and full Swagger documentation.

---

## ⚡ Tech Stack

- **Python 3.11**
- **Django 4+**
- **Django REST Framework**
- **SimpleJWT (Access + Refresh Token)**
- **PostgreSQL**
- **Docker & Docker Compose**
- **drf-spectacular (Swagger UI)**

---

## 🌟 Features

### 🔑 Authentication
- User registration  
- JWT login (access + refresh token)  
- Token refresh endpoint  
- Logout with token blacklist  
- Profile endpoint (view + update)  
- Custom User model  

### 🛡 Security
- Password hashing  
- Token rotation support  
- Refresh token blacklist  
- JWT expiration (configurable)  
- Environment variable configuration  

### 🗄 Database
- PostgreSQL via Docker  
- Persistent volume storage  
- Clean ORM models  

### 📦 Developer Tools
- Dockerized development  
- Automatic Swagger docs  
- REST API structure  
- Requirements file  
- Clean and scalable project layout  

---

## 📂 Project Structure

django-jwt-auth-api/
│
├── accounts/ # Authentication app
│ ├── models.py # Custom User model
│ ├── serializers.py # Register, profile serializers
│ ├── views.py # Auth views
│ └── urls.py # Routes
│
├── config/ # Project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md


---

## 🧰 Environment Variables

Create a `.env` file in the project root:

```env
DJANGO_SECRET_KEY=change_me_to_something_secure
DJANGO_DEBUG=True

POSTGRES_DB=auth_db
POSTGRES_USER=auth_user
POSTGRES_PASSWORD=strongpassword123
POSTGRES_HOST=db
POSTGRES_PORT=5432

🐳 Running with Docker 

1️⃣ Build and start containers

docker compose up --build -d

2️⃣ Apply migrations

docker compose exec web python manage.py migrate

3️⃣ Create superuser

docker compose exec web python manage.py createsuperuser

▶️ Running Without Docker

1️⃣ Create virtual environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Apply migrations

python manage.py migrate

4️⃣ Run server

python manage.py runserver
