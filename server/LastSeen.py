import requests
import json
from datetime import datetime, timezone, timedelta

clanTag = input("Clan Tag")
if (clanTag[0] == '#'):
    clanTag = clanTag[1:]
print(clanTag)
url = "https://api.clashroyale.com/v1/clans/%23"+clanTag+"/members"
key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3ZjQ0MGIwLTBiZDQtNDE0Ny1iYWMzLThhNTkxYzYxY2I1MiIsImlhdCI6MTczNzMyNDUzOCwic3ViIjoiZGV2ZWxvcGVyL2E5NmZjN2RkLTM0YmMtYmI4Zi0zNjBkLTQ5MjdhNjZkZmE1NCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI3Ni4xMjAuMTg4LjEzIl0sInR5cGUiOiJjbGllbnQifV19.FEXSz2X22EgeI58eyPqtUe8eoOcNjNgzJJHuhOXs5VJN6U5nxCpVwpDuw2VsgCuhZnwkp130R2z6HzJ6DRZT-w"
response = requests.get(url, headers={"Accept":"application/json", "authorization":"Bearer "+key})
players = response.json()["items"]
now = datetime.now(timezone.utc)

for player in players:
    lastSeen = player["lastSeen"]
    datetimeobj = datetime(int(lastSeen[0:4]), int(lastSeen[4:6]), int(lastSeen[6:8]), int(lastSeen[9:11]), int(lastSeen[11:13]), int(lastSeen[13:15]), 0, timezone(timedelta()))
    diff = now-datetimeobj
    if (diff.days >= 3):
        print(diff)