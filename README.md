# 🔐 File Integrity Checker Using SHA-256

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-black)
![Security](https://img.shields.io/badge/Concept-Cryptographic%20Hashing-green)
![Algorithm](https://img.shields.io/badge/Algorithm-SHA--256-orange)

## 📌 Project Overview

File Integrity Checker is a cybersecurity-based web application that helps users verify whether a file has been modified or tampered with.

The application uses the **SHA-256 cryptographic hashing algorithm** to generate a unique digital fingerprint of a file. During verification, the newly generated hash value is compared with the previously stored hash value to identify any changes.

If the hash values match, the file is considered authentic. If the values differ, the system detects that the file has been modified.

---

# 🎯 Objectives

- Understand the concept of cryptographic hashing
- Implement SHA-256 file hashing
- Detect unauthorized file modifications
- Build a simple cybersecurity application using Flask
- Provide a user-friendly web interface for file verification

---

# ✨ Features

✅ Generate SHA-256 hash for any uploaded file  
✅ Store generated hash information  
✅ Verify file integrity anytime  
✅ Detect file tampering or modification  
✅ Display current and stored hash values  
✅ Simple web-based interface  
✅ Fast and reliable verification process  

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Flask | Web application framework |
| HTML | Frontend structure |
| CSS | User interface styling |
| SHA-256 | Cryptographic hashing algorithm |
| Kali Linux | Development environment |

---

# 📂 Project Structure

```
FileIntegrityChecker-Web
│
├── app.py                 # Flask application
├── generate.py            # SHA-256 hash generation module
├── verify.py              # File verification module
├── hash_utils.py          # Hash calculation functions
├── requirements.txt       # Required Python packages
├── README.md              # Project documentation
│
├── templates
│   └── index.html         # Web interface
│
├── static
│   └── style.css          # Styling file
│
├── uploads                # Uploaded files
│
└── hashes                 # Stored hash files
```

---

# ⚙️ Installation and Setup

## 1. Clone the Repository

```bash
git clone <repository-url>
```

## 2. Navigate to Project Directory

```bash
cd FileIntegrityChecker-Web
```

## 3. Install Required Packages

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the Flask server:

```bash
python app.py
```

The application will run at:

```
http://127.0.0.1:5000
```

Open the URL in your browser.

---

# 🔄 Working Principle

```
              User
                |
                |
          Upload File
                |
                |
        Flask Web Application
                |
        -------------------
        |                 |
        |                 |
 Generate SHA-256     Verify SHA-256
        |                 |
        |                 |
 Store Hash File    Compare Hash Values
                          |
              ---------------------
              |                   |
           Match              Different
              |                   |
              |                   |
    File Integrity OK     File Modified
```

---

# 🧪 Testing

## Test Case 1: Generate Hash

Input:
```
Original file
```

Output:

```
SHA-256 Hash Generated Successfully
```

---

## Test Case 2: Verify Original File

Input:

```
Same file without changes
```

Output:

```
File Integrity Verified!
```

---

## Test Case 3: Modified File Detection

Input:

```
Modified file
```

Output:

```
Integrity Failed / File Modified
```

---

# 📸 Screenshots

## 1. Application Home Page

_Add screenshot here_

Example:

```
screenshots/home_page.png
```

![Home Page](screenshots/home_page.png)


---

## 2. SHA-256 Hash Generation

_Add screenshot showing generated hash result_

Example:

```
screenshots/hash_generation.png
```

![Hash Generation](screenshots/hash_generation.png)


---

## 3. Successful File Verification

_Add screenshot showing matching hashes_

Example:

```
screenshots/integrity_verified.png
```

![Integrity Verified](screenshots/integrity_verified.png)


---

## 4. File Modification Detection

_Add screenshot showing modified file detection_

Example:

```
screenshots/file_modified.png
```

![File Modified](screenshots/file_modified.png)


---

# 🔒 Security Concept

This project demonstrates:

- Cryptographic hashing
- Data integrity verification
- SHA-256 algorithm usage
- File tampering detection

SHA-256 generates a fixed-length hash value. Even a small change in file content produces a completely different hash, making unauthorized modifications easy to detect.

---

# 🚀 Future Enhancements

Future improvements that can be added:

- Multiple file integrity checking
- Automatic file monitoring
- Database-based hash history
- Email alerts for modifications
- Cloud storage integration
- User authentication system

---

# 📚 Learning Outcomes

Through this project, the following concepts were learned:

- Python file handling
- Flask web development
- Cryptographic hashing
- Cybersecurity fundamentals
- Web application development

---

# 👨‍💻 Author

Syed Atif Ali
Shaik Zeeshan Ali

B.E. Information Technology

---

# 📄 License

This project is developed for educational and internship purposes.
