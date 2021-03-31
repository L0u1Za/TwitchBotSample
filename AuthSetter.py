print("Введи логин Twitch: ", end="")
login = input()
print("Введи OAuth аутентификатор без префикса (доступен по ссылке https://twitchapps.com/tmi): ", end="")
oauth = input()
import json
path = "data.json"
with open(path, 'w') as f:
    data = {"login" : login, "oauth" : oauth}
    json.dump(data, f, indent=4, sort_keys=True, separators=(',', ' : '), ensure_ascii=False)
with open(path, 'r') as f:
    data = json.loads(f.read())
    print("login : " + data["login"])
    print("oauth : " + data["oauth"])
print("Верно? При неверном вводе перезапусти файл")
