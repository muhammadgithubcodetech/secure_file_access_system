# Secure File Access System

This is a Python-based simulation of an operating system-style secure file access system. It was designed to demonstrate key cybersecurity and OS-level principles such as user authentication, role-based access control, secure file handling, logging, and file-level encryption.

Built with a focus on **learning and simulation**, this project offers a safe, GUI-based environment to explore how secure file systems operate — and how they might be attacked or protected.

---

## 🔐 Features

- **User Authentication**
  - Login and registration system with SHA-256 password hashing
  - User roles: Admin and Standard User

- **Access Control**
  - Role-based file permissions
  - File access limited by user ownership and role

- **File Operations**
  - File creation, viewing, deletion
  - XOR-based encryption for confidentiality
  - Automatic file directory setup

- **Logging**
  - All user actions are timestamped and logged
  - Admin can view and clear logs

- **GUI (Tkinter)**
  - Simple desktop interface to manage all actions
  - No terminal commands required

---

## 🗂 Project Structure

```
secure_file_access_system/
├── src/
│   ├── gui.py           # GUI logic using tkinter
│   ├── auth.py          # User authentication system
│   ├── files.py         # File access, encryption, permission checks
│   ├── encryption.py    # XOR encryption/decryption logic
│   └── logs.py          # Action logging system
├── data/                # File storage directory (auto-created)
├── output/              # Generated logs and user data (optional)
├── docs/                # (Optional) Reports, diagrams, presentations
└── README.md            # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/secure-file-access-system.git
cd secure-file-access-system
```

### 2. Run the Project

Make sure you're inside the `src/` directory:

```bash
cd src
python gui.py
```

If your system uses `python3`:

```bash
python3 gui.py
```

> The GUI should launch automatically. All necessary folders and files will be created at runtime.

---

## 🛠 Dependencies

No third-party libraries required — everything uses Python’s standard library:

- `tkinter` – GUI
- `hashlib` – Password hashing
- `json` – User storage
- `os`, `datetime`, `getpass`, etc.

---

## ⚙️ Configuration

You can change the default data directory:

- By default, encrypted files are saved in a `data/` folder.
- To change this, edit the `DATA_FOLDER` variable in `files.py`.

---

## 📌 Notes

- This project is **for educational and simulation purposes** only.
- User credentials and logs are stored in plain JSON and text files.
- The encryption method (XOR) is intentionally simple for learning purposes.
- Logs and user data are auto-generated during usage.

---

## 🧠 Learning Objectives

This project is part of a broader personal learning path focused on:

- Understanding OS-level access control concepts
- Simulating real-world file system security problems
- Practicing secure coding and interface design
- Building tools as a future penetration tester and cybersecurity specialist

---

## 📜 License

This project is open for educational use. Add a license (e.g. MIT) if you wish to share or reuse more broadly.

---

## 👤 Author

**Muhammad Shah**  
Cybersecurity undergrad | Aspiring pentester & researcher  
GitHub: [muhammadgithubcodetech](https://github.com/muhammadgithubcodetech)