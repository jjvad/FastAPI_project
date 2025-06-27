from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. URL подключения (аналог SQLALCHEMY_DATABASE_URI)
SQLALCHEMY_DATABASE_URL = "sqlite:///./news.db"

# 2. Создаём движок (аналог db.engine)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Только для SQLite
)

# 3. Фабрика сессий (аналог db.session)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Базовый класс для моделей (аналог db.Model)
Base = declarative_base()

# 5. Зависимость для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()