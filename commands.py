from entities import Timer, Image
import insertion
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
        bot.send_message(insertion.from_origin_to_modified_insertion_handler(self.text, user))

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

lst = [TextResponse('!ало', '${TagTarget()}, ну привет тебе'), TextResponse('!любоф', '${TagTarget()}, я люблю тебя на ${RandomNumber(0, 101)} процентов!')]