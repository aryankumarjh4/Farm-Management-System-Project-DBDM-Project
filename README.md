# 🌾 Farm-Management-System-Project-DBDM-Project

A **DBMS Mini Project** built using **Python Flask, MySQL, and Bootstrap**.  
The system allows farmers to register, add agricultural products, manage farming activities, and track trigger-based logs. Buyers can view available products, while admins can manage users and farmer details.  

---

## 📌 Features
- 👨‍🌾 **Farmer Registration** – add and manage farmer details  
- 🌱 **Farming Management** – add different types of farming categories  
- 🛒 **Agro Products Management** – farmers can add and showcase their products  
- 🔐 **User Authentication** – secure login and signup with session management  
- ⚡ **Database Triggers** – automatic logging for insert, update, and delete actions  
- 📊 **Centralized Data Storage** – managed with MySQL & SQLAlchemy ORM  
- 💻 **Responsive UI** – built using HTML, CSS, Bootstrap  

---

## 🛠️ Tech Stack
- **Frontend**: HTML, CSS, JavaScript, Bootstrap  
- **Backend**: Python Flask (with Flask-Login & SQLAlchemy)  
- **Database**: MySQL (via XAMPP / phpMyAdmin)  
- **Tools**: PyCharm / Sublime Text, Chrome  

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/farm-management-system.git
cd farm-management-system
```

### 2. Set up the Database
```sql
CREATE DATABASE farmers;
USE farmers;
SOURCE farm_management.sql;
```

### 3. Configure Flask
```python
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/farmers"
```

### 4. Install dependencies
```bash
pip install flask flask_sqlalchemy flask_login werkzeug
```

### 5. Run the project
```bash
python main.py
```

Now visit 👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.  

---

## 📂 Project Structure
```
├── main.py                 # Flask backend application
├── farm_management.sql     # Database schema, sample data & triggers
├── templates/              # HTML templates (Jinja2)
│   ├── index.html
│   ├── signup.html
│   ├── login.html
│   ├── farmer.html
│   ├── agroproducts.html
│   ├── triggers.html
│   └── ...
├── static/                 # CSS, JS, and images
├── README.md               # Documentation
```

---

## 📖 Sample Workflows
- **Signup/Login** → User creates an account and logs in  
- **Register Farmer** → Add farmer details with Aadhaar, contact, and farming type  
- **Add Agro Product** → Upload product details like name, description, and price  
- **Triggers Table** → Logs actions such as `Farmer Inserted`, `Farmer Updated`, `Farmer Deleted`  
- **View Details** → Admins can view farmers, farming types, products, and logs  

---

## 📸 Screenshots
- <img width="889" height="469" alt="image" src="https://github.com/user-attachments/assets/a13521c5-7d60-448c-99ea-c8334bf9d208" />

- <img width="902" height="479" alt="image" src="https://github.com/user-attachments/assets/c3aeb98c-0f55-42f9-9eb8-68fd51f89f36" />

- <img width="902" height="470" alt="image" src="https://github.com/user-attachments/assets/63c2ba82-91d5-4a98-9837-687bbb17fb6e" />

- <img width="908" height="481" alt="image" src="https://github.com/user-attachments/assets/baac0da1-a66f-4246-924e-70ef7c37dc0a" />

---

## 🚀 Future Enhancements
- Online payment integration  
- More advanced reporting & analytics  
- Enhanced GUI with React/Angular frontend  
- Cloud-based database deployment  

---

## 📜 License
This project is developed for **educational purposes**.  
Feel free to modify and use with attribution.  

