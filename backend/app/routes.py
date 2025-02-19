from app import app
from app.coc_api import CocAPI
import json

# GET -> Retrieve
# POST -> Add new data
# PUT -> Update data
# DELETE -> Delete data

# Default GET

@app.route("/get-clan", methods=["GET", "POST"])
def getClan():
    coc = CocAPI("2LL22QUCC")
    # players = {}
    # members = coc.get_clan_members()
    # for member in members['items']:
    #     players[member["name"]] = member["trophies"]

    return coc.get_clan_members()

@app.route("/get-current-war")
def getCurrentWar():
    coc = CocAPI("2LL22QUCC")
    return coc.get_clan_current_war()
