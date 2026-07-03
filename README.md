# 🧺 Laundry Order Management System 

A lightweight full-stack system to manage dry cleaning orders with a clean, modern UI and structured backend.

---

## 🚀 Overview

This project allows a laundry store to:

* Create and manage customer orders
* Track order status
* Calculate billing automatically
* View real-time dashboard insights

Built with an **AI-first development approach**, leveraging tools like ChatGPT and Claude for faster iteration and smarter design decisions.

---

## 🛠️ Tech Stack

**Frontend**

* HTML, CSS, JavaScript (no framework)
* Modern UI with cards, dashboard, and interactive elements

**Backend**

* Python (Flask)
* REST APIs

**Database**

* MySQL

---

## 📦 Features Implemented

### 👤 Customer

* Place order using visual garment selection (no typing-heavy UI)
* Dynamic price calculation
* View own orders using phone number
* Clean receipt page after placing order

### 🏪 Store Owner

* View all orders in table format
* Filter by status and search by name/phone
* Update order status (RECEIVED → PROCESSING → READY → DELIVERED)
* Dashboard showing:

  * Total orders
  * Total revenue
  * Orders by status

---

## 🎯 System Architecture

Frontend (HTML/JS)
⬇
REST API Calls (Fetch)
⬇
Flask Backend
⬇
MySQL Database

* Frontend handles UI & user interaction
* Backend handles business logic & validation
* Database stores persistent order data

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Manyaaggarwal10/laundry-order-management-system.git
cd laundry-system
```

### 2. Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 3. Configure Database

* Create MySQL database
* Update credentials in `db_config.py`

### 4. Run Backend

```bash
python run.py
```

Backend runs at:

```
http://127.0.0.1:5000
```

### 5. Run Frontend

* Open `index.html` in browser

---

## 🔌 API Endpoints

| Method | Endpoint            | Description         |
| ------ | ------------------- | ------------------- |
| POST   | /orders             | Create new order    |
| GET    | /orders             | Get all orders      |
| GET    | /orders?phone=      | Get customer orders |
| PUT    | /orders/{id}/status | Update order status |
| GET    | /dashboard          | Get analytics       |

---

## 🤖 AI Usage Report 

### Tools Used

* ChatGPT → Backend logic, debugging, architecture
* Claude → Frontend UI generation and styling

---

### Example Prompts

**1. Backend API Design**

> “Create Flask APIs for order management with status tracking and billing”

**2. Frontend UI**

> “Build a professional HTML frontend with customer and store owner roles, using cards and visual garment selection”

**3. Debugging**

> “Fix Flask error: duplicate endpoint function”
> “Why is frontend not connecting to backend?”

---

### Where AI Helped

* Initial project structure
* API design and routes
* Frontend UI generation
* Debugging integration issues

---

### Where AI Was Wrong 

* Mismatch between frontend (`items`) and backend (`garments`)
* Duplicate route causing Flask crash
* Incorrect UI navigation logic (role switching)
* Incorrect assumptions about DOM structure

---

### What I Improved

* Fixed API contract mismatches
* Corrected data structures across frontend/backend
* Implemented proper role-based UI flow
* Built a separate receipt page for better UX
* Improved dashboard integration with fallback handling

---

## ⚖️ Tradeoffs

### What I Skipped

* Authentication system (login/signup)
* Deployment (local only)
* Advanced database optimization

### Why

* Focused on core functionality within 72-hour limit
* Prioritized UX and clean architecture over complexity

---

## 🚀 Future Improvements

* Add authentication (JWT / session-based)
* Deploy using Render / Railway / AWS
* Add notifications (SMS/email)
* Add estimated delivery time
* Convert frontend to React for scalability

---

## Deployment Link
https://laundry-order-management-system-b68h.onrender.com/

---

## 🎥 Demo

<img width="1915" height="877" alt="image" src="https://github.com/user-attachments/assets/b37ec032-18d9-4a2e-81b9-bb1a41eb078d" />

<img width="1889" height="865" alt="image" src="https://github.com/user-attachments/assets/7e46e352-623a-4675-bcdf-3276a9491c74" />

<img width="1906" height="864" alt="image" src="https://github.com/user-attachments/assets/64e12ad6-9657-4a99-b959-c7e996d1ca1e" />


---

## 💡 Key Learning

> “AI accelerates development, but understanding and debugging its output is what makes a strong engineer.”

---

## 🙌 Final Note

This project demonstrates:

* Full-stack development
* API design
* UI/UX thinking
* AI-assisted engineering workflow

---

✨ Built with an AI-first mindset
