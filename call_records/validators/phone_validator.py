from django.core.exceptions import ValidationError

def validate_phone(phone):
    if 10 < len(str(phone)) > 11:
        raise ValidationError(
            f'{phone} is not a valid phone number, the size must be 10 or 11.',
            params={'phone': phone},
        )