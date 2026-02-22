import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from requestValidator import RequestValidator

class TestRequestValidator:
    @pytest.fixture
    def v(self): return RequestValidator()

    def test_valid_string(self, v):
        v.validate_string('name', 'Alice')
        assert v.is_valid()

    def test_empty_required_string(self, v):
        v.validate_string('name', '', required=True)
        assert not v.is_valid()

    def test_string_too_long(self, v):
        v.validate_string('name', 'A' * 300, max_len=255)
        assert not v.is_valid()

    def test_valid_number(self, v):
        v.validate_number('age', 25, min_val=0, max_val=150)
        assert v.is_valid()

    def test_number_out_of_range(self, v):
        v.validate_number('age', -1, min_val=0)
        assert not v.is_valid()

    def test_valid_email(self, v):
        v.validate_email('email', 'test@example.com')
        assert v.is_valid()

    def test_invalid_email(self, v):
        v.validate_email('email', 'not-an-email')
        assert not v.is_valid()

    def test_sanitize(self, v):
        result = v.sanitize_string('  hello   world  ')
        assert result == 'hello world'
