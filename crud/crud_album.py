from crud.base import CRUDBase
from database_app.models import Album
from schemas.album import AlbumCreate, AlbumUpdate


class CRUDAlbum(CRUDBase[Album, AlbumCreate, AlbumUpdate]):
    pass


crud_album = CRUDAlbum(Album)
