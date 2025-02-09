"""Server development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\xc4\x0ci\x8coH /nZ/"\x07\xb8\xbc$\xb7\xec5\x86\\b(\xfb'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
SERVER_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = SERVER_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

