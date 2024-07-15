from cryptography.fernet import Fernet

# Generate a key and save it to a file
def generate_key(file_path):
    key = Fernet.generate_key()
    with open(file_path, 'wb') as key_file:
        key_file.write(key)

# Load the key from a file
def load_key(file_path):
    with open(file_path, 'rb') as key_file:
        return key_file.read()

# Encrypt a password
def encrypt_password(key, password):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

# Decrypt a password
def decrypt_password(key, encrypted_password):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

# Example usage
key_file = 'secret.key'
generate_key(key_file)
key = load_key(key_file)

password = 'my_secret_password'
encrypted_password = encrypt_password(key, password)
print(f"Encrypted Password: {encrypted_password}")

decrypted_password = decrypt_password(key, encrypted_password)
print(f"Decrypted Password: {decrypted_password}")
