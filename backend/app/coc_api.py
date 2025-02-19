import requests
import json

headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjFkYmM0ZjE3LTkwMzMtNDljOS1iZDFlLTQxOTM5OTZiMzM4OSIsImlhdCI6MTczOTkxOTIzNywic3ViIjoiZGV2ZWxvcGVyLzc0NDFiOWMyLThlNGEtNDgzMy1iZWVmLWZhYjRlNDc0NGUyMyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjIwNi44Ny4yMjIuMjM4Il0sInR5cGUiOiJjbGllbnQifV19.oyuKb_5Xe1GZ0AWVGulIcpWNECHgMLDzxg9EaeiOfNkG0F129WIx8n9kIunKJXKn7n2wi-vPnl0rAeeu5Zt6xQ'
}

url = "https://api.clashofclans.com/v1/clans/%23"

class CocAPI:
    def __init__(self, clan_tag):
        self._clan_tag = clan_tag

    def get_clan_members(self):
        try:
            members = requests.get(url + self._clan_tag + "/members?limit=50", headers=headers)
            members.raise_for_status()
            return members.json()
        except requests.exceptions.HTTPError as err:
            print("Clan Does not exist!")

    def get_clan_current_war(self):
        try:
            war = requests.get(url + self._clan_tag + "/currentwar", headers=headers)
            war.raise_for_status()
            return war.json()
        except requests.exceptions.HTTPError as err:
            print("Clan Does not exist!")





