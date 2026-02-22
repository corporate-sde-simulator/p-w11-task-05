import re

class RequestValidator:
    def __init__(self):
        self.errors = []

    def validate_string(self, field, value, min_len=1, max_len=255, required=True):
        pass

    def validate_number(self, field, value, min_val=None, max_val=None, required=True):
        pass

    def validate_email(self, field, value, required=True):
        pass

    def sanitize_string(self, value):
        pass

    def validate_request(self, data, schema):
        # Schema format: {'field': {'type': 'string', 'required': True, 'min': 1, 'max': 100}}
        pass

    def is_valid(self):
        return len(self.errors) == 0

    def get_errors(self):
        return list(self.errors)
