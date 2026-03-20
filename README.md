# 📸 SaminGram – Instagram Clone (Django)

SaminGram is a full-stack Instagram-like web application built using Django. It allows users to create accounts, share posts, follow others, like posts, and interact through 
comments—replicating core social media functionality.

---

## 🚀 Features

### 👤 Authentication

* User registration and login system
* Secure password handling
* Logout functionality
* Auto profile creation using signals

### 🏠 Feed

* View posts from users
* Like/unlike posts (AJAX-based)
* Real-time like count update

### 📸 Posts

* Create posts with images and captions
* Edit and delete your own posts
* View detailed post page

### 💬 Comments

* Add comments to posts
* View comments on feed and post detail page

### 👥 Follow System

* Follow / Unfollow users
* Followers & Following count
* Real-time follow toggle (AJAX)

### 🔍 Search

* Search users by username or full name

### 👤 Profile

* View your profile and others’ profiles
* Edit profile (bio, profile picture, DOB, name)
* Grid view of posts (Instagram-style)

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap 5
* **Database:** SQLite (default)
* **Other:** JavaScript (AJAX), Django ORM


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/samingram.git
cd samingram
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the server

```bash
python manage.py runserver
```

### 6️⃣ Open in browser

```
http://127.0.0.1:8000/
```

---

## 🔐 Important Notes

* Only logged-in users can access the feed
* Media files are stored locally (`/media`)
* DEBUG mode is enabled (disable for production)

---

## 📸 Screenshots (Optional)

> Add screenshots here for better presentation
> (Feed, Profile, Post Detail, etc.)

---

## 🚧 Future Improvements

* 🔔 Notifications (likes, follows)
* 📱 Responsive mobile UI improvements
* 🌙 Dark mode
* 🔄 Infinite scrolling
* 🧠 AI features (caption generation, moderation)
* 🌐 Deployment (Render / AWS / VPS)

---

## 👨‍💻 Author

**Samin Shrestha**

* Django Developer
* Computer Engineering Student
* Interested in Web Development & AI/ML

---

## ⭐ Contribute

Feel free to fork this repo and submit pull requests!

---

## 📜 License

This project is for educational purposes.
