import os

# Thư mục gốc dự án (chứa config.py)
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Thư mục instance để chứa jobs.db
INSTANCE_DIR = os.path.join(BASEDIR, 'instance')
os.makedirs(INSTANCE_DIR, exist_ok=True)  # đảm bảo tồn tại


class Config:
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '131fd895c8b23169dcd7d6df3275704dcd1908b12dbbe6b4e0adbbc03375daed'
    # Đường dẫn tuyệt đối tới jobs.db
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('DATABASE_URL')
        or 'sqlite:///' + os.path.join(INSTANCE_DIR, 'jobs.db')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
