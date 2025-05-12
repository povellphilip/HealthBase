# HealthBase - Hospital Database Management System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)
![Terminal](https://img.shields.io/badge/Platform-Terminal%20based-green)

A terminal-based hospital management system with role-based access (Doctor, Patient, Administrator) built with Python and MySQL.

## 🏥 Features

### Role-Based Access
- **Doctors**: View/update/delete patient records
- **Patients**: Register and print medical receipts
- **Administrators**: Manage doctor accounts and passwords

### Core Functionalities
- Patient registration with auto-generated token numbers
- Medical record management (CRUD operations)
- CSV receipt generation for patients
- Secure password management for doctors

## ⚙️ Technical Stack

| Component       | Technology Used           |
|-----------------|---------------------------|
| Database       | MySQL 8.0                 |
| Backend        | Python 3.x                |
| Key Libraries  | `mysql-connector`, `tabulate`, `csv` |
| UI             | Terminal-based interactive menus |

## 🚀 Installation

1. **Prerequisites**:
   - Python 3.x
   - MySQL Server
   - `mysql-connector-python` library

2. **Setup**:
   ```bash
   pip install mysql-connector-python tabulate
