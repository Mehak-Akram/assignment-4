import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def login(email: str, password_to_check: str, stored_logins: dict) -> bool:

    hashed_password = hash_password(password_to_check)
    
    return stored_logins.get(email) == hashed_password

stored_logins = {
    "user@example.com": hash_password("securepassword"),
    "abc@domain.com": hash_password("mypassword123")
}

print(login("user@example.com", "securepassword", stored_logins))  
print(login("abc@domain.com", "wrongpassword", stored_logins))  
