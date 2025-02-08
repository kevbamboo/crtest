from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from daysInactive import get_clan_members, check_inactive_members

app = Flask(__name__)
cors = CORS(app, origins='*') #currently accepts all origins

@app.route("/api/daysInactive", methods=['GET'])
def daysInactive():
    with open('members.json', 'r') as f:
            dummy_data = json.load(f)
    
    members = get_clan_members("#R9QVVUG9", "", dummy_data)
    days = request.args.get('days')
    print(type(days))
    if (days):
        print(days)
    else:
        days = 3 #no input default to 3
    inactive = check_inactive_members(members, int(days))
    return jsonify(inactive)

'''
@app.route("/api/users", methods=['GET'])
def users():
    return jsonify(
        {
            "users": [
                'arpan',
                'zach',
                'jessie',
                'abcde'
            ]
        }
    )
'''

if __name__ == "__main__":
    app.run(debug=True, port=8080)

