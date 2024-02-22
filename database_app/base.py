# Import all the models, so that Base has them before being
# imported by Alembic
from database_app.base_class import Base  # noqa
from database_app.models import *  # noqa
