print("Running Bot.py.")
from irc.bot import SingleServerIRCBot
import config, commands

def CommandParse(message):
    lst = list(message.split(' '))
    return lst


class Bot(SingleServerIRCBot):
    def __init__(self):
        self.HOST = config.host
        self.PORT = config.port
        self.USERNAME = config.login.lower()
        self.CLIENT_ID = config.client_id
        self.TOKEN = config.oauth
        self.CHANNEL = f"#{self.USERNAME}"

        super().__init__([(self.HOST, self.PORT,self.TOKEN)], self.USERNAME, self.USERNAME)
    
    def on_welcome(self, connection, event):
        for req in ("membership", "tags", "commands"):
            connection.cap("REQ", f":twitch.tv/{req}")
        connection.join(self.CHANNEL)
        self.send_message("Gypsy-bot is now online.")
        print("Succesful connection.")
    
    def on_pubmsg(self, connection, event):
        tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags}
        user = {"name": tags["display-name"], "id": tags["user-id"]}
        message = event.arguments[0]
        print(f"Message from {user['name']}: {message}")
        if message[0] == '!':
            command = CommandParse(message)
            self.handle_command(user, command[0], command[1:])
    
    def send_message(self, message):
        self.connection.privmsg(self.CHANNEL, message)

    def handle_command(self, user, message, flags):
        print(f"{user['name']} executed command: {message}")
        users = list()
        for flag in flags:
            if flag[0] == '@':
                users.append(flag)
        target = user['name']
        if len(users) != 0:
            target = users[0]
        for cm in commands.lst:
            if message == cm.title:
                cm.react(target, bot, *flags)
                print(f"Succesful execution: {message}")
                return
        #self.send_message(f"I don't know this command: {message}.")
        print(f"Unknown command: {message}")
    
if __name__ == "__main__":
    bot = Bot()
    bot.start()