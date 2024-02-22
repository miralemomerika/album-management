from crud.base import CRUDBase
from database_app.models import Song
from schemas.song import SongCreate, SongUpdate


class CRUDSong(CRUDBase[Song, SongCreate, SongUpdate]):
    pass


crud_song = CRUDSong(Song)
