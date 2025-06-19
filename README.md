# 🧰 Django Backend – Product Store API

This is the Django REST Framework backend for the React eCommerce frontend. It provides product, cart, wishlist, and authentication APIs.

## 🚀 Features

- JWT-based authentication (djoser or custom)
- Product CRUD
- Cart management API
- Wishlist API (Backend Sync)
- Django Admin for managing content

## 🛠️ Setup Instructions

1. Navigate to the backend folder:
   ```bash
   cd product-backend
Create and activate a virtual environment:


python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install requirements:


pip install -r requirements.txt
Run migrations:


python manage.py migrate
Start the server:


python manage.py runserver
Access API at: http://127.0.0.1:8000

🧪 API Endpoints
Method	Endpoint	Description
GET	/products/	List all products
POST	/cart/	Add to cart
GET	/wishlist/	Get wishlist
POST	/auth/jwt/create/	Login (get token)
POST	/auth/users/	Register



