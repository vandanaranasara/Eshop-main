# 🛒 Eshop 
An online shopping platform developed using Django and Python, where users can browse products, add items to their cart, and securely place orders through an easy-to-use HTML frontend.

# 🛍️ Features 
### Feature 1 :- User Management
- Two types of users: Buyer and Seller
- User Registration, Login, and Logout
- Email Notifications for registration and order updates

### Feature 2: Seller Dashboard
- Add, Edit, and Delete Products
- View All Listed Products
- Manage Orders

### Feature 3: Buyer Dashboard
- Browse Products by category or search  
- View Product Details
- Add to Cart / Remove from Cart
- Place Orders

### Feature 4: Order & Shopping Cart Management
- Add Multiple Products to Cart
- Update Quantity or Remove Items
- View Order Status (Pending, Shipped, Delivered)

### Feature 5: Admin Dashboard
- Manage Buyers, Sellers, and Products
- Monitor Platform Activity and Reports


## 🚀 How to Run the Project

Follow these steps to set up and run the project on your local system:

### 1️⃣ Clone the Repository
- Clone the project from GitHub using:
 ```bash
https://github.com/vandanaranasara/Eshop-main.git
cd Eshop-main
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```
- Activate the Virtual Environment
```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a Superuser
```bash
python manage.py createsuperuser
```

Open your browser and go to:
- http://127.0.0.1:8000/
  
Admin panel:
- http://127.0.0.1:8000/admin/

## 🐳 Docker Setup

Follow these steps to set up and run the project on your local system:

### 1️⃣ Clone the Repository
- Clone the project from GitHub using:
 ```bash
https://github.com/vandanaranasara/Eshop-main.git
cd Eshop-main
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```
- Activate the Virtual Environment
```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Stop Containers (if running)
```bash
docker compose down
```
### 5️⃣ Build and Start Containers
```bash
docker compose up --build
```

### 6️⃣ Open the Website

Now open your browser and go to:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)


