import os

# For production: use secret key:
# To generate:
# python -c "import secrets;print(secrets.token_hex())"
SECRET_KEY = os.getenv('SECRET_KEY', 'replace with generated key here')

# for Render using env var DATABASE_URL
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///project.db")

# for local env
# DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost/vitality-nector-db"
# SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
# SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost/vitality-nector-db"

RESOURCE_SMOOTHIES = "resources/smoothies.csv"
RESOURCE_BENEFITS = "resources/benefits.csv"
