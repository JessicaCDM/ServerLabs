from enum import Enum
from pydantic import BaseModel, Field


class PlayerBase(BaseModel):
    full_name: str
    email: str

    class Config:
        orm_mode = True
    #:
#:

class PlayerRegister(PlayerBase):
    password: str
    phone_number: str | None = Field(
        title="Local portuguese phone number or international prefixed w/ +XYZ country code"
    )
    birth_date: str | None
    level: str
    tournaments: int | None
#:

class PlayerRegisterResult(PlayerBase):
    id: int
#:

class ErrorCode(Enum):
    ERR_UNSPECIFIED_TOURNAMENT = 'Missing tournament id.'
    ERR_PLAYER_ALREADY_ENROLLED = 'Jogador já registado'
    ERR_UNKNOWN_TOURNAMENT_ID = 'Unknown tournament id'
#    ERR_TOURNAMENT_UNAVAILABLE = 'Sem torneio disponível'

    def details(self, **kargs) -> dict:
        details_dict = {'error_code': self.name, 'error_msg': self.value}
        details_dict.update(kargs)
        return details_dict
    #:
#: