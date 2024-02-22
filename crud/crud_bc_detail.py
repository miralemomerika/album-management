from crud.base import CRUDBase
from database_app.models import BrowserConnectionDetail
from schemas.bc_detail import BCDetailCreate, BCDetailUpdate


class CRUDBCDetail(
    CRUDBase[BrowserConnectionDetail, BCDetailCreate, BCDetailUpdate]
):
    pass


crud_bc_detail = CRUDBCDetail(BrowserConnectionDetail)
