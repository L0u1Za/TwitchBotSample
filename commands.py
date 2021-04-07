from entities import Timer, Image
import insertion
import economy
from economy import EconomyEvent, CollectBets

class Command:
    def __init__(self, title):
        self.title = title
    def react(self, user, bot, *args):
        pass

class TextResponse(Command):
    def __init__(self, title, text):
        self.text = text
        super().__init__(title)
    def react(self, user, bot, *args):
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
    def react(self, user, bot, *args):
        self.image.show()

class StartEconomyEvent(Command):
    def __init__(self, start_title, event_title):
        economy.CurrentEconomyEvent = event_title(*economy.events[event_title])
        super().__init__(start_title)
    def react(self, user, bot, *args):
        if (economy.activeEconomyEvent):
            bot.send_message("Уже есть активное событие.")
            return
        economy.activeEconomyEvent = True
        bot.send_message(insertion.from_origin_to_modified_insertion_handler(economy.CurrentEconomyEvent.get_text(), user))
class EndEconomyEvent(Command):
    def __init__(self, end_title):
        super().__init__(end_title)
    def react(self, user, bot, *args):
        if (not economy.activeEconomyEvent):
            bot.send_message("Сейчас не проходит событий.")
            return
        economy.activeEconomyEvent = False
        economy.CurrentEconomyEvent.result()
        bot.send_message(insertion.from_origin_to_modified_insertion_handler(economy.CurrentEconomyEvent.get_result_text(), user))
class ParticipateInEconomyEvent(Command):
    def __init__(self, participate_title):
        super().__init__(participate_title)
    def react(self, user, bot, *args):
        if (not economy.activeEconomyEvent):
            bot.send_message("Сейчас не проходит событий.")
            return
        if (len(args) != 1 and args[0].isdigit()):
            bot.send_message("Укажите корректную сумму.")
            return
        value = int(args[0])
        user_id = "1" #get user id by nickname
        bot.send_message(insertion.from_origin_to_modified_insertion_handler(economy.CurrentEconomyEvent.accept(user, user_id, value), user))
        

lst = [StartEconomyEvent('!начатьсбор', CollectBets), 
    ParticipateInEconomyEvent('!отдатьзолото'), 
    EndEconomyEvent('!закончить'), 
    TextResponse('!ало', '${TagTarget()}, ну привет тебе'), 
    TextResponse('!любоф', '${TagTarget()}, я люблю тебя на ${RandomNumber(0, 101)} процентов!'),
    TextResponse('!баланс', '${TagTarget()}, твой баланс ${CurrentBalance()}')]