from typing import Generator, Optional

from app.db.session import SessionLocal


def get_db() -> Generator:
    db: Optional[SessionLocal] = None  # type: ignore
    try:
        db = SessionLocal()
        yield db
    finally:
        if db:
            db.close()
