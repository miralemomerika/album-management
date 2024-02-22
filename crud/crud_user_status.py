from crud.base import CRUDBase
from database_app.models import UserStatus
from schemas.user_status import UserStatusCreate, UserStatusUpdate


class CRUDUserStatus(CRUDBase[UserStatus, UserStatusCreate, UserStatusUpdate]):
    pass


crud_user_status = CRUDUserStatus(UserStatus)
