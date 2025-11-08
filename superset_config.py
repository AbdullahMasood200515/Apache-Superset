# Superset specific config
import os

# Set the secret key - replace with your generated key
SECRET_KEY = 'Eo8VzNMZyevEDFtdh9ytvMH_RG1ouUWoqDQ1oGqwbOiRbfocqtPJ9vxZ'

# SQL Alchemy connection string
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'superset.db')

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True

# Add additional security measures
WTF_CSRF_TIME_LIMIT = None

# ADD THESE LINES TO ALLOW SQLITE FOR CSV UPLOADS
PREVENT_UNSAFE_DB_CONNECTIONS = False
ALLOWED_EXTRA_DB_URI_SCHEMES = ["sqlite"]

# Enable CSV upload
CSV_EXTENSIONS = {'csv', 'tsv', 'txt'}
ALLOWED_EXTENSIONS = {'csv', 'tsv', 'txt'}