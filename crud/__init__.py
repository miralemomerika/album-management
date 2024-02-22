from sqlalchemy.orm import Session
from schemas.auth import AdminUserCreate
from database_app.models import AdminUser
from core.security import get_password_hash, verify_password


def create_user(
    *, session: Session, user_create: AdminUserCreate
) -> AdminUser:
    hashed_password = get_password_hash(user_create.password)
    db_obj = AdminUser(
        first_name=user_create.first_name,
        last_name=user_create.last_name,
        email=user_create.email,
        hashed_password=hashed_password,
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def get_user_by_email(*, session: Session, email: str) -> AdminUser | None:
    session_user = (
        session.query(AdminUser).where(AdminUser.email == email).first()
    )
    return session_user


def authenticate(
    *, session: Session, email: str, password: str
) -> AdminUser | None:
    user = get_user_by_email(session=session, email=email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
