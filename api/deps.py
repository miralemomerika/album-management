from typing import Annotated
from database_app.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from database_app.models import AdminUser
from fastapi.security import OAuth2PasswordBearer
from core import config, security
import jwt
from schemas.auth import TokenPayload
from pydantic import ValidationError

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{config.settings.API_V1_STR}/auth/login"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


TokenDep = Annotated[str, Depends(reusable_oauth2)]


def get_current_user(
    *, session: Session = Depends(get_db), token: TokenDep
) -> AdminUser:
    try:
        payload = jwt.decode(
            token, config.settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = session.get(AdminUser, token_data.sub)
    if not user:
        raise HTTPException(
            status_code=404, detail="The user doesn't have enough privileges"
        )
    return user


CurrentAdminUser = Annotated[AdminUser, Depends(get_current_user)]
