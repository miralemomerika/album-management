from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.deps import get_db
from schemas.auth import AdminUserRead, AdminUserCreate
import crud
from core import security
from schemas.auth import LoginResponse
from datetime import timedelta
from core.config import settings
from schemas.common import SuccessResponse
from api.deps import CurrentAdminUser
from typing import Any, Annotated
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/register", response_model=SuccessResponse)
def create_user(
    *, db: Session = Depends(get_db), user_in: AdminUserCreate
) -> Any:
    """
    Create new Admin user that will be operating and moderating this platform.
    """
    user = crud.get_user_by_email(session=db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )

    user = crud.create_user(session=db, user_create=user_in)

    return SuccessResponse(description="User created successfully.")


@router.post("/login", response_model=LoginResponse)
def login_access_token(
    *,
    db: Session = Depends(get_db),
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    user = crud.authenticate(
        session=db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=400, detail="Incorrect email or password"
        )
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return LoginResponse(
        access_token=security.create_access_token(
            subject=user.id, expires_delta=access_token_expires
        ),
        token_type="bearer",
        first_name=user.first_name,
        last_name=user.last_name,
    ).model_dump()


@router.post("/test-token", response_model=SuccessResponse)
def test_token(current_admin_user: CurrentAdminUser) -> Any:
    """
    Test access token and get currently logged user.
    """
    return SuccessResponse(
        description="Token is valid.",
        data=AdminUserRead.model_validate(current_admin_user).model_dump(),
    )
