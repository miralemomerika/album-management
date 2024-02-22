from fastapi import APIRouter, Depends, HTTPException, status
from api.deps import get_db, CurrentAdminUser
from schemas.user import UserCreate, UserRead, UserUpdate
from typing import Any
from sqlalchemy.orm import Session
from crud.crud_user import crud_user
from schemas.common import SuccessResponse

router = APIRouter()


@router.get("/", response_model=SuccessResponse)
def get_all_users(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db)
) -> Any:
    """
    Get all users.
    """
    users = crud_user.get_all(db=db)
    return SuccessResponse(
        description="Users retrieved successfully",
        data=[UserRead.model_validate(user).model_dump() for user in users],
    )


@router.get("/{user_id}", response_model=SuccessResponse)
def get_user_by_id(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db), user_id: int
) -> Any:
    """
    Get user by ID.
    """
    user = crud_user.get_by_id(db=db, obj_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return SuccessResponse(
        description="User retrieved successfully",
        data=UserRead.model_validate(user).model_dump(),
    )


@router.post("/", response_model=SuccessResponse)
def create_user(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    user_in: UserCreate,
) -> Any:
    """
    Create new user.
    """
    user = None
    if getattr(user_in, "email"):
        user = crud_user.get_by_email(db=db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )

    user = crud_user.create(db=db, obj_in=user_in)
    return SuccessResponse(
        description="User created successfully",
    )


@router.put("/{user_id}", response_model=SuccessResponse)
def update_user(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    user_id: int,
    user_in: UserUpdate,
) -> Any:
    """
    Update a user.
    """
    user = crud_user.get_by_id(db=db, obj_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    user = crud_user.update(db=db, db_obj=user, obj_in=user_in)
    return SuccessResponse(
        description="User updated successfully",
        data=UserRead.model_validate(user).model_dump(),
    )


@router.delete("/{user_id}", response_model=SuccessResponse)
def delete_user(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db), user_id: int
) -> Any:
    """
    Delete a user.
    """
    user = crud_user.get_by_id(db=db, obj_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    user = crud_user.remove(db=db, id=user_id)
    return SuccessResponse(
        description="User deleted successfully",
        data=UserRead.model_validate(user).model_dump(),
    )
