from django.core.validators import EmailValidator, ValidationError
import re

def validate_email(email):
    validator = EmailValidator(message='The email is in wrong format')
    validator(email)
    if not re.fullmatch("^[^@]+@berkeley\\.edu", email):
        raise ValidationError(message="The domain needs to be @berkeley.edu.")
