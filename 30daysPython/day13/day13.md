#  Day 13 - Password Vault (Hashing + File Security)

##  Overview

Password Vault is a secure Python application that stores account credentials using SHA-256 hashing.

Instead of saving passwords as plain text, the application converts every password into a secure hash before storing it.

This demonstrates one of the most important security practices used in backend development.

---

##  Features

- Add new website accounts
- Store username/email
- Secure password hashing using SHA-256
- Verify passwords
- Delete accounts
- JSON-based storage
- Persistent file saving

---

##  Technologies Used

- Python
- hashlib
- json
- os

---


---

##  How to Run

```bash
python vault.py
```

---

## Sample Menu

```
===== PASSWORD VAULT =====

1. Add Account
2. View Accounts
3. Verify Password
4. Delete Account
5. Exit
```

---

## Concepts Learned

- Cryptographic Hashing
- SHA-256
- File Handling
- JSON Storage
- Dictionaries
- Functions
- Security Basics
- Persistent Data Storage

---

## Future Improvements

- Master Password Authentication
- Password Generator
- AES Encryption
- Hidden Password Input (`getpass`)
- Search Accounts
- Update Credentials
- Export/Import Vault