from datetime import date

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Date,
    CheckConstraint,
    Table,
)
from sqlalchemy.orm import relationship
from database import Base, SessionLocal


player_tournament = Table("player_tournament_association", Base.metadata,
                        Column("id", Integer, primary_key=True, autoincrement=True),
                        Column("player_id", Integer, ForeignKey("Player.id")),
                        Column("tournament_id", Integer, ForeignKey("Tournament.id"))
                    )

class Tournament(Base):    # type: ignore (Pylance doesn't recognize Base)
    __tablename__ = 'Tournament'
    __table_args__ = (
        CheckConstraint('end_date >= start_date', name='check_dates'),
    )

    id          = Column(Integer, primary_key=True, autoincrement=False)
    name        = Column(String, nullable=False, unique=True)
    start_date  = Column(Date, nullable=False)
    end_date    = Column(Date, nullable=False)

    players_enrolled = relationship("Player", back_populates="tournament", secondary=player_tournament)
    #secondary=player_tournament
#:

# Tournament.players = relationship("Player", order_by=Player.id, back_populates="tournament")

class Player(Base):  # type: ignore  (Pylance )
    __tablename__ = 'Player'

    id                  = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    full_name           = Column(String, nullable=False)
    email               = Column(String, unique=True, index=True, nullable=False)
    hashed_password     = Column(String, nullable=False)
    phone_number        = Column(String(13))
    # birth_date        = Column(Date, nullable=False)
    level               = Column(String(30), nullable=False)
    tournaments         = Column(Integer, nullable=False)
    is_active           = Column(Boolean, default=True)
    
    tournament          = relationship("Tournament", back_populates="players_enrolled", secondary=player_tournament)
    #secondary=player_tournament,
#:

def populate_db():
    with SessionLocal() as db_session:
        player1 = Player(
            full_name = 'Armando Alves',
            email = 'arm@mail.com',
            hashed_password = 'abc-hashedpw',
            phone_number = '+351922781977',
            level = 'beginner',
            tournaments = '1',
        )
        player2 = Player(
            full_name = 'Augusto Avelar',
            email = 'aug@mail.com',
            hashed_password = '123-hashedpw',
            phone_number = '+351921061344',
            level = 'pre-pro',
            tournaments = '2',
        )
        tournament1 = Tournament(
            id         = 1,
            name      = 'Torneio da Páscoa',
            start_date = date(2023, 4, 17),
            end_date   = date(2023, 4, 25),
        )
        tournament2 = Tournament(
            id         = 2,
            name      = 'Torneio da Amizade',
            start_date = date(2023, 5, 17),
            end_date   = date(2023, 5, 25),
        )

        db_session.add_all([player1, player2, tournament1, tournament2])
        tournament1.players_enrolled.append(player1)
        tournament1.players_enrolled.append(player2)
        tournament2.players_enrolled.append(player1)
        tournament2.players_enrolled.append(player2)
        
        db_session.commit()
    #:
#:
