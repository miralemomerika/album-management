from typing import Optional

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from database_app.models import User
from schemas.user import UserCreate, UserUpdate, UserRead


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[UserRead]:
        return db.query(User).filter(User.email == email).first()


crud_user = CRUDUser(User)
