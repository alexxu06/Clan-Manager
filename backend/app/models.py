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

    # connects list of members
    clan_members: Mapped[List["ClanMember"]] = relationship(back_populates="leader")
    # connects war history (list of wars)
    clan_wars: Mapped[List["War"]] = relationship(back_populates="leader")

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

    # pulled from get player (specific player)
    war_preference: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    clan_capital_contributions: Mapped[int] = mapped_column(Integer, index=True, unique=False)
    attackWins: Mapped[int] = mapped_column(Integer, index=True, unique=False)

    # this will be calculated from war history
    average_war_stars: Mapped[int] = mapped_column(Integer, index=True, unique=False)
    averate_num_attacks: Mapped[int] = mapped_column(Integer, index=True, unique=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"), index=True)

    # connects with User
    leader: Mapped["User"] = relationship(back_populates="clan_members")
    # list of member's performance in previous wars
    war_performances: Mapped[List["WarPerformance"]] = relationship(back_populates="member")

    def __repr__(self):
        return "<Clan Member {}>".format(self.name)

# Table for wars clan has been in 
class War(db.Model):
    __tablename__ = "war"

    id: Mapped[int] = mapped_column(primary_key=True)

    # pulled from war history (cannot access performance of individual players)
    # will be used to calculate general clan stats
    team_size: Mapped[int] = mapped_column(Integer, index=True, unique=False)
    attacks_per_member: Mapped[int] = mapped_column(Integer, index=True, unique=False)

    ## From Clan
    result: Mapped[Optional[bool]] = mapped_column(Boolean) # Optional because war may not have ended
    attacks: Mapped[int] = mapped_column(Integer, index=True, unique=False)
    stars: Mapped[int] = mapped_column(Integer, index=True, unique=False)

    ## From Enemy Clan
    enemy_result: Mapped[Optional[bool]] = mapped_column(Boolean) # Optional because war may not have ended
    attacks: Mapped[int] = mapped_column(Integer, index=True, unique=False)
    stars: Mapped[int] = mapped_column(Integer, index=True, unique=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"), index=True)

    #connects war with user
    leader: Mapped["User"] = relationship(back_populates="clan_wars")
    # connects war with war performance, list of all player's performance during this war
    performance: Mapped[List["WarPerformance"]] = relationship(back_populates="war")

    def __repr__(self):
        return "<War {}>".format(self.team_size)


#Table for war performance for each member
class WarPerformance(db.Model):
    __tablename__ = "war_performance"

    id: Mapped[int] = mapped_column(primary_key=True)

    clan_member_id: Mapped[int] = mapped_column(ForeignKey("clan_member.id"), index=True)
    war_id: Mapped[int] = mapped_column(ForeignKey("war.id"), index=True)

    member: Mapped["ClanMember"] = relationship(back_populates="war_performances")
    war: Mapped["War"] = relationship(back_populates="performance")

    # pulled from current war (not applicable to past wars)
    # will be used to determine who is on the naughty list (underperforming members)
    attacks: Mapped[int] = mapped_column(Integer, index=True, unique=False)
    stars: Mapped[int] = mapped_column(Integer, index=True, unique=False)
    destruction: Mapped[int] = mapped_column(Integer, index=True, unique=False)


#p = ClanMember(name='whably', tag="abd", role="coleader", trophies=5000, donations=2000, town_hall_level=14, war_preference=True, clan_capital_contributions = 3000, attackWins=100, leader=u)    
