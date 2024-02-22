from crud.base import CRUDBase
from database_app.models import MusicService
from schemas.music_service import MusicServiceCreate, MusicServiceUpdate


class CRUDMusicService(
    CRUDBase[MusicService, MusicServiceCreate, MusicServiceUpdate]
):
    pass


crud_music_service = CRUDMusicService(MusicService)
