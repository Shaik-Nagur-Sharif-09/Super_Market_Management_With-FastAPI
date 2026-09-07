# 🛒 Supermarket Management System using FastAPI

**Course Project:** Web API & Data Structures  
**Author:** Shaik Nagur Sharif  
**Tech Stack:** Python, FastAPI, Uvicorn, Tuples  

---

## 📌 Project Overview
This project is a simple RESTful Web API built using **FastAPI** to manage a supermarket's inventory. 

Instead of using a traditional database, this application uses **Python Tuples** as an in-memory data store to perform basic CRUD operations (Create, Read, Update, Delete). Since tuples are **immutable** in Python, modifications are handled by converting tuples to lists temporarily and converting them back to tuples.

---

## 🎯 Objectives
- Build a REST API using FastAPI framework.
- Understand how data immutability works with Python Tuples.
- Perform CRUD operations via HTTP methods (`GET`, `POST`, `PUT`, `DELETE`).
- Test API endpoints using Swagger UI documentation.

---

## 📂 Data Structure Used
The initial dataset uses three parallel tuples:
- `products`: Names of supermarket items.
- `prices`: Cost of each item.
- `stock`: Available quantity.

---

## 🛠️ Requirements & Installation

### 1. Install Required Packages
Open your terminal/command prompt and run:
```bash
pip install fastapi uvicorn pydantic
