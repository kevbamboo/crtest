import argparse
import json
import requests
from datetime import datetime

def load_config(config_path='config.json'):
    with open(config_path, 'r') as f:
        return json.load(f)

def get_clan_members(clan_tag, api_key, dummy_data=None):
    if dummy_data:
        return dummy_data.get(clan_tag, [])
    else:
        clan_tag_encoded = clan_tag.replace('#', '%23')
        url = f'https://api.clashroyale.com/v1/clans/{clan_tag_encoded}/members'
        headers = {'Authorization': f'Bearer {api_key}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()['items']

def check_inactive_members(members, inactive_days: int):
    inactive = []
    current_time = datetime.utcnow()
    for member in members:
        last_seen = datetime.strptime(member['lastSeen'], '%Y%m%dT%H%M%S.%fZ')
        delta = (current_time - last_seen).days
        if delta > inactive_days:
            inactive.append({
                'name': member['name'],
                'tag': member['tag'],
                'inactive_days': delta
            })
    return inactive

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dummy', help='Path to dummy data JSON file')
    args = parser.parse_args()

    config = load_config()
    api_key = config['api_key']
    dummy_data = None

    if args.dummy:
        print(args.dummy)
        with open(args.dummy, 'r') as f:
            dummy_data = json.load(f)

    for clan in config['clans']:
        clan_tag = clan['tag']
        inactive_days = clan['inactive_days']
        
        members = get_clan_members(clan_tag, api_key, dummy_data)
        inactive = check_inactive_members(members, inactive_days)
        
        print(f"\nInactive members in {clan_tag}:")
        for m in inactive:
            print(f"{m['name']} ({m['tag']}): {m['inactive_days']} days")

if __name__ == '__main__':
    main()