import pytest
from enc_dec.enc_dec import encrypt, decrypt

@pytest.fixture
def setup_data():
    """
    Fixture to set up test data for encryption and decryption.
    """
    return {
        'plain_text': 'hello',
        'cipher_text': 'khoor',
        'key': 3,
        'mixed_case_plain': 'HelloWorld',
        'mixed_case_cipher': 'KhoorZruog'
    }

def test_encrypt(setup_data):
    """
    Test case for encrypt function.
    """
    data = setup_data
    assert encrypt(data['plain_text'], data['key']) == data['cipher_text']

def test_decrypt(setup_data):
    """
    Test case for decrypt function.
    """
    data = setup_data
    assert decrypt(data['cipher_text'], data['key']) == data['plain_text']

def test_encrypt_mixed_case(setup_data):
    """
    Test case for encrypt function with mixed case input.
    """
    data = setup_data
    assert encrypt(data['mixed_case_plain'], data['key']) == data['mixed_case_cipher']

def test_decrypt_mixed_case(setup_data):
    """
    Test case for decrypt function with mixed case input.
    """
    data = setup_data
    assert decrypt(data['mixed_case_cipher'], data['key']) == data['mixed_case_plain']

def test_encrypt_with_key_1():
    """
    Test case for encrypt function with key 1.
    """
    assert encrypt('abc', 1) == 'bcd'

def test_decrypt_with_key_1():
    """
    Test case for decrypt function with key 1.
    """
    assert decrypt('bcd', 1) == 'abc'

def test_encrypt_with_key_2():
    """
    Test case for encrypt function with key 2.
    """
    assert encrypt('xyz', 2) == 'zab'

def test_decrypt_with_key_2():
    """
    Test case for decrypt function with key 2.
    """
    assert decrypt('zab', 2) == 'xyz'
