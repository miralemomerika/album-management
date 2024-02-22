from crud.base import CRUDBase
from database_app.models import PaymentInfo
from schemas.payment_info import PaymentInfoCreate, PaymentInfoUpdate


class CRUDPaymentInfo(
    CRUDBase[PaymentInfo, PaymentInfoCreate, PaymentInfoUpdate]
):
    pass


crud_payment_info = CRUDPaymentInfo(PaymentInfo)
