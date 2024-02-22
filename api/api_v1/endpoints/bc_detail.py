from fastapi import APIRouter, Depends, HTTPException, status
from api.deps import get_db, CurrentAdminUser
from schemas.bc_detail import (
    BCDetailCreate,
    BCDetailUpdate,
    BCDetailRead,
)
from typing import Any
from sqlalchemy.orm import Session
from crud.crud_bc_detail import crud_bc_detail
from schemas.common import SuccessResponse

router = APIRouter()


@router.get("/", response_model=SuccessResponse)
def get_all_bc_details(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db)
) -> Any:
    """
    Get all browser connection details.
    """
    bc_details = crud_bc_detail.get_all(db=db)
    return SuccessResponse(
        description="Browser connection details retrieved successfully",
        data=[
            BCDetailRead.model_validate(detail).model_dump()
            for detail in bc_details
        ],
    )


@router.get("/{browser_connection_id}", response_model=SuccessResponse)
def get_bc_detail_by_id(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    browser_connection_id: int,
) -> Any:
    """
    Get browser connection detail by ID.
    """
    bc_detail = crud_bc_detail.get_by_id(db=db, obj_id=browser_connection_id)
    if not bc_detail:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Browser connection detail not found",
        )
    return SuccessResponse(
        description="Browser connection detail retrieved successfully",
        data=BCDetailRead.model_validate(bc_detail).model_dump(),
    )


@router.post("/", response_model=SuccessResponse)
def create_browser_connection(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    bc_detail_in: BCDetailCreate,
) -> Any:
    """
    Create new browser connection detail.
    """
    crud_bc_detail.create(db=db, obj_in=bc_detail_in)
    return SuccessResponse(
        description="Browser connection detail created successfully",
    )


@router.put("/{browser_connection_id}", response_model=SuccessResponse)
def update_browser_connection(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    browser_connection_id: int,
    bc_detail_in: BCDetailUpdate,
) -> Any:
    """
    Update a browser connection detail.
    """
    bc_detail_db = crud_bc_detail.get_by_id(
        db=db, obj_id=browser_connection_id
    )
    if not bc_detail_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Browser connection detail not found",
        )

    bc_detail = crud_bc_detail.update(
        db=db, db_obj=bc_detail_db, obj_in=bc_detail_in
    )
    return SuccessResponse(
        description="Browser connection detail updated successfully",
        data=BCDetailRead.model_validate(bc_detail).model_dump(),
    )


@router.delete("/{browser_connection_id}", response_model=SuccessResponse)
def delete_browser_connection(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    browser_connection_id: int,
) -> Any:
    """
    Delete a browser connection detail.
    """
    bc_detail = crud_bc_detail.get_by_id(db=db, obj_id=browser_connection_id)
    if not bc_detail:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Browser connection detail not found",
        )
    bc_detail = crud_bc_detail.remove(db=db, id=browser_connection_id)
    return SuccessResponse(
        description="Browser connection detail deleted successfully",
        data=BCDetailRead.model_validate(bc_detail).model_dump(),
    )
