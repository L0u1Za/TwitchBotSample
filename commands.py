from entities import Timer, RandomNumber, Image
class Command:
    def __init__(self, title):
        self.title = title
    def react(self, user, bot):
        pass

class TextResponse(Command):
    def __init__(self, title, text):
        self.text = text
        super().__init__(title)
    def react(self, user, bot):
        bot.send_message(f"{user}, {self.text}")

#class SoundCommand(Command):
#   def __init__(self, title, path):
#        self.sound = Sound(path)
#        super().__init__(title)
#    def react(self, user, bot):
#        self.sound.play()

class ImageCommand(Command):
    def __init__(self, title, path):
        self.image = Image(path)
        super().__init__(title)
    def react(self):
        self.image.show()

lst = [TextResponse('!ало', 'ну привет'), TextResponse('!любоф', 'я тоже люблю тебя, заюш...')]