# 🌐 URL Monitoring Service

A Flask-based backend application that continuously monitors website availability, tracks response times, logs monitoring history, sends email alerts when websites become unavailable, and secures APIs using JWT Authentication.

This project demonstrates how to build a production-style backend service using Flask, SQLAlchemy, APScheduler, JWT, and SQLite.

---

## ✨ Features

- Website uptime monitoring
- Response time tracking
- HTTP status code monitoring
- Automatic scheduled health checks
- Email notifications when a website goes down
- Monitoring history (logs)
- User Registration
- User Login
- JWT Authentication
- Protected REST APIs
- CRUD operations for monitors
- SQLite database with SQLAlchemy ORM
- Database migrations using Flask-Migrate

---

## 🛠 Tech Stack

### Backend

- Python 3
- Flask
- SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- Flask-Bcrypt

### Database

- SQLite

### Scheduler

- APScheduler

### Email

- SMTP (Gmail)

### API Testing

- Postman

### Version Control

- Git
- GitHub

---

## 📂 Project Structure

```text
url-monitor-service/
│
├── assets/
├── database/
├── migrations/
├── models/
│   ├── monitor.py
│   ├── monitor_log.py
│   └── user.py
│
├── routes/
│   ├── auth_routes.py
│   └── monitor_routes.py
│
├── scheduler/
│   └── job_scheduler.py
│
├── services/
│   ├── email_service.py
│   └── monitor_service.py
│
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🚀 Current Features

- User Authentication using JWT
- Website Monitoring
- Monitoring Logs
- Email Alerts
- Response Time Monitoring
- REST APIs
- Database Migrations


---

# 🏗️ System Architecture

```text
                           Client (Postman)
                                   │
                                   ▼
                          Flask REST API
                                   │
      ┌───────────────┬────────────┴────────────┬───────────────┐
      │               │                         │               │
      ▼               ▼                         ▼               ▼
 JWT Authentication  Monitor Service      Email Service     APScheduler
      │               │                         │               │
      └───────────────┴──────────────┬──────────┴───────────────┘
                                     │
                                     ▼
                             SQLAlchemy ORM
                                     │
                                     ▼
                              SQLite Database
```


---

# 📡 API Endpoints

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|---------------|
| POST | `/register` | Register a new user | ❌ |
| POST | `/login` | Login and receive JWT Token | ❌ |
| GET | `/me` | Get logged-in user details | ✅ |
| POST | `/monitors` | Create a new monitor | ✅ |
| GET | `/monitors` | Get all monitors | ✅ |
| GET | `/monitors/<id>` | Get monitor by ID | ✅ |
| PUT | `/monitors/<id>` | Update monitor | ✅ |
| DELETE | `/monitors/<id>` | Delete monitor | ✅ |
| GET | `/logs` | Get monitoring logs | ✅ |
| GET | `/run-check` | Trigger monitoring manually | ❌ |




---

# 📸 API Screenshots

## Register API

![Register API](assets/register-api.png)

---

## Login API

![Login API](assets/login-api.png)

---

## Get Current User

![Current User](assets/me-api.png)

---

## Get Monitors

![Monitors](assets/monitors-api.png)

---

## Monitoring Logs

![Logs](assets/logs-api.png)