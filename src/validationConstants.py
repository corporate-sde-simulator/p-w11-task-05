"""Validation constants. Clean file."""
EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
CONTROL_CHARS = re.compile(r'[\x00-\x1f\x7f-\x9f]') if __import__('re') else None
import re
CONTROL_CHARS = re.compile(r'[\x00-\x1f\x7f-\x9f]')
