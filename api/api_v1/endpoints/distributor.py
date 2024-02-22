from fastapi import APIRouter, Depends, HTTPException, status
from api.deps import get_db, CurrentAdminUser
from schemas.distributor import (
    DistributorCreate,
    DistributorUpdate,
    DistributorRead,
)
from typing import Any
from sqlalchemy.orm import Session
from crud.crud_distributor import crud_distributor
from crud.crud_bc_detail import crud_bc_detail
from schemas.common import SuccessResponse

router = APIRouter()


@router.get("/", response_model=SuccessResponse)
def get_all_distributors(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db)
) -> Any:
    """
    Get all distributors.
    """
    distributors = crud_distributor.get_all(db=db)
    return SuccessResponse(
        description="Distributors retrieved successfully",
        data=[
            DistributorRead.model_validate(dist).model_dump()
            for dist in distributors
        ],
    )


@router.get("/{distributor_id}", response_model=SuccessResponse)
def get_distributor_by_id(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    distributor_id: int,
) -> Any:
    """
    Get distributor by ID.
    """
    dist = crud_distributor.get_by_id(db=db, obj_id=distributor_id)
    if not dist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Distributor not found",
        )
    return SuccessResponse(
        description="Distributor retrieved successfully",
        data=DistributorRead.model_validate(dist).model_dump(),
    )


@router.post("/", response_model=SuccessResponse)
def create_distributor(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    dist_in: DistributorCreate,
) -> Any:
    """
    Create new distributor.
    """
    if getattr(dist_in, "browser_details_id"):
        browser_details = crud_bc_detail.get_by_id(
            db=db, obj_id=dist_in.browser_details_id
        )
        if not browser_details:
            raise HTTPException(
                status_code=400,
                detail=f"The Browser Details with id `{dist_in.browser_details_id}` doesn't exist.",
            )

    crud_distributor.create(db=db, obj_in=dist_in)
    return SuccessResponse(
        description="Distributor created successfully",
    )


@router.put("/{distributor_id}", response_model=SuccessResponse)
def update_distributor(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    distributor_id: int,
    dist_in: DistributorUpdate,
) -> Any:
    """
    Update a distributor.
    """
    distributor_db = crud_distributor.get_by_id(db=db, obj_id=distributor_id)
    if not distributor_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Distributor not found",
        )
    if getattr(dist_in, "browser_details_id"):
        browser_details = crud_bc_detail.get_by_id(
            db=db, obj_id=dist_in.browser_details_id
        )
        if not browser_details:
            raise HTTPException(
                status_code=400,
                detail=f"The Browser Details with id `{dist_in.browser_details_id}` doesn't exist.",
            )
    distributor = crud_distributor.update(
        db=db, db_obj=distributor_db, obj_in=dist_in
    )
    return SuccessResponse(
        description="Distributor updated successfully",
        data=DistributorRead.model_validate(distributor).model_dump(),
    )


@router.delete("/{distributor_id}", response_model=SuccessResponse)
def delete_distributor(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    distributor_id: int,
) -> Any:
    """
    Delete a distributor.
    """
    distributor = crud_distributor.get_by_id(db=db, obj_id=distributor_id)
    if not distributor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Distributor not found",
        )
    distributor = crud_distributor.remove(db=db, id=distributor_id)
    return SuccessResponse(
        description="Distributor deleted successfully",
        data=DistributorRead.model_validate(distributor).model_dump(),
    )
