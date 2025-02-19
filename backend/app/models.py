from sqlalchemy import ForeignKey, String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app import db
from typing import Optional, List
from werkzeug.security import generate_password_hash, check_password_hash

# Table for User Account
class User(db.Model): 
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, index=True, unique=True)
    password: Mapped[Optional[str]] = mapped_column(String) # Optional means that it can be null (optional field)
    clan_tag: Mapped[Optional[str]] = mapped_column(String, index=True, unique=False) # multiple accounts can view same clan

    clan_members: Mapped[List["ClanMember"]] = relationship(back_populates="leader")

    def __repr__(self):
        return "<User {}>".format(self.username) # if username is Bob, will return: <User Bob>

# Table for Clan Members
class ClanMember(db.Model):
    __tablename__ = "clan_member"

    # pulled from get clan members
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True, unique=False)
    tag: Mapped[str] = mapped_column(String, index=True, unique=False)
    role: Mapped[str] = mapped_column(String, index=True, unique=False)
    trophies: Mapped[int] = mapped_column(Integer, index=True, unique=False)
    donations: Mapped[int] = mapped_column(Integer, index=True, unique=False)
    town_hall_level: Mapped[int] = mapped_column(Integer, index=True, unique=False)

    #pulled from get player (specific player)
    war_preference: Mapped[bool] = mapped_column(Boolean, default=False)
    clan_capital_contributions: Mapped[int] = mapped_column(Integer, index=True, unique=False)
    attackWins: Mapped[int] = mapped_column(Integer, index=True, unique=False)
    user_id: Mapped[int]= mapped_column(ForeignKey("user_account.id"), index=True)

    leader: Mapped["User"] = relationship(back_populates="clan_members")

    def __repr__(self):
        return "<Clan Member {}>".format(self.name)

#p = ClanMember(name='whably', tag="abd", role="coleader", trophies=5000, donations=2000, town_hall_level=14, war_preference=True, clan_capital_contributions = 3000, attackWins=100, leader=u)    
