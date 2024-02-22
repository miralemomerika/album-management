from crud.base import CRUDBase
from database_app.models import Distributor
from schemas.distributor import DistributorCreate, DistributorUpdate


class CRUDDistributor(
    CRUDBase[Distributor, DistributorCreate, DistributorUpdate]
):
    pass


crud_distributor = CRUDDistributor(Distributor)
