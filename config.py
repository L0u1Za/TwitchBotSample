import json
with open('data.json', 'r') as f:
    data = json.loads(f.read())
    login = data['login']
    oauth = data['oauth']
    client_id = "dig23h2snubyqhqsy0tpjodyx9iii8"
host = 'irc.twitch.tv'
port = 6667

