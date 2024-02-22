from fastapi import APIRouter, Depends, HTTPException, status
from api.deps import get_db, CurrentAdminUser
from schemas.payment_info import (
    PaymentInfoCreate,
    PaymentInfoUpdate,
    PaymentInfoRead,
)
from typing import Any
from sqlalchemy.orm import Session
from crud.crud_payment_info import crud_payment_info
from crud.crud_user import crud_user
from schemas.common import SuccessResponse

router = APIRouter()


@router.get("/", response_model=SuccessResponse)
def get_all_payments(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db)
) -> Any:
    """
    Get all payments.
    """
    payments = crud_payment_info.get_all(db=db)
    return SuccessResponse(
        description="Payments retrieved successfully",
        data=[
            PaymentInfoRead.model_validate(payment).model_dump()
            for payment in payments
        ],
    )


@router.get("/{payment_id}", response_model=SuccessResponse)
def get_payment_by_id(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db), payment_id: int
) -> Any:
    """
    Get payment info by ID.
    """
    payment = crud_payment_info.get_by_id(db=db, obj_id=payment_id)
    if not payment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Payment info not found",
        )
    return SuccessResponse(
        description="Payment info retrieved successfully",
        data=PaymentInfoRead.model_validate(payment).model_dump(),
    )


@router.post("/", response_model=SuccessResponse)
def create_payment(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    payment_info_in: PaymentInfoCreate,
) -> Any:
    """
    Create new payment info.
    """
    if getattr(payment_info_in, "user_id"):
        user = crud_user.get_by_id(db=db, obj_id=payment_info_in.user_id)
        if not user:
            raise HTTPException(
                status_code=400,
                detail=f"The user with id `{payment_info_in.user_id}` doesn't exist.",
            )

    crud_payment_info.create(db=db, obj_in=payment_info_in)
    return SuccessResponse(
        description="Payment info created successfully",
    )


@router.put("/{payment_id}", response_model=SuccessResponse)
def update_payment(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    payment_id: int,
    payment_info_in: PaymentInfoUpdate,
) -> Any:
    """
    Update a payment info.
    """
    payment_info = crud_payment_info.get_by_id(db=db, obj_id=payment_id)
    if not payment_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Payment info not found",
        )
    if getattr(payment_info_in, "user_id"):
        user = crud_user.get_by_id(db=db, obj_id=payment_info_in.user_id)
        if not user:
            raise HTTPException(
                status_code=400,
                detail=f"The user with id `{payment_info_in.user_id}` doesn't exist.",
            )
    payment_info = crud_payment_info.update(
        db=db, db_obj=payment_info, obj_in=payment_info_in
    )
    return SuccessResponse(
        description="Payment info updated successfully",
        data=PaymentInfoRead.model_validate(payment_info).model_dump(),
    )


@router.delete("/{payment_id}", response_model=SuccessResponse)
def delete_payment_info(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db), payment_id: int
) -> Any:
    """
    Delete a payment info.
    """
    payment_info = crud_payment_info.get_by_id(db=db, obj_id=payment_id)
    if not payment_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Payment info not found",
        )
    payment_info = crud_payment_info.remove(db=db, id=payment_id)
    return SuccessResponse(
        description="Payment info deleted successfully",
        data=PaymentInfoRead.model_validate(payment_info).model_dump(),
    )
