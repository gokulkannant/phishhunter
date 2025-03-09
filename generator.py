from faker import Faker
import random

def generate_fake_credential():
    """Generates a fake Indian-style username and a simple password."""
    fake = Faker('en_IN')
    
    first_name = fake.first_name().lower()
    username = first_name + str(random.randint(100, 999))  # Example: rajesh123
    password = first_name + str(random.randint(10, 99))    # Example: rajesh45
    
    return username, password

