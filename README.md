# Cryptography

## Description

This project demonstrates simple encryption and decryption using a Caesar cipher.
It includes functions to encrypt and decrypt text based on a key.

## Setup

1. Create a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  
    # On Windows use `.venv\Scripts\activate`
    ```

2. Install requirements:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

- `encrypt(text, key)`: Encrypts the given text using the specified key.
- `decrypt(text, key)`: Decrypts the given text using the specified key.

## Testing

Run the tests using:

```bash
pytest test/test_enc_dec.py
