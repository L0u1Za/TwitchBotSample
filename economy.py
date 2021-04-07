import insertion
class Economy:
    def __init__(self):
        self.users = {"1" : EconomyUser("L0u1Za", "1")} #str(id) -> EconomyUser, get from json
    def get_user_balance(self, nickname): #find by nickname -> id
        return self.users["1"].get_balance()
    def update_user_balance(self, nickname, value):
        self.users[user_id].update_balance(value)

class EconomyUser:
    def __init__(self, nickname, user_id):
        self.nickname = nickname
        self.id = user_id
        self.balance = 100 #get from json
    def get_balance(self):
        return self.balance
    def update_balance(self, value):
        self.balance += value

def UpdateEconomyData():
    pass #update json
def GetEconomyData():
    pass #get info from json

economy = Economy()

activeEconomyEvent = False

class EconomyEvent:
    def __init__(self, text, result_text):
        self.text = text
        self.result_text = result_text
        self.m_winners = list()
        self.m_prize = int()
    def get_text(self):
        return self.text
    def get_result_text(self):
        return self.result_text
    def update(self, users_values):
        for (user_id, value) in users_values.items():
            economy.users[user_id].update_balance(value)
    def winners(self):
        return ''.join(self.m_winners)
    def prize(self):
        return str(self.m_prize)
    def result(self):
        activeEconomyEvent = False
    def accept(self, nickname, user_id , value):
        pass
CurrentEconomyEvent = EconomyEvent        
class CollectBets(EconomyEvent):
    def __init__(self, text, result_text):
        self.bets = dict()
        super().__init__(text, result_text)
    def accept(self, nickname, user_id , value):
        user = economy.users[user_id]
        if (user_id in self.bets):
            return "${TagTarget(" + nickname + ")}, вы уже участвуете в игре."
        current_user_balance = user.get_balance()
        if current_user_balance < value:
            return "${TagTarget(" + nickname + ")}, у вас недостаточно средств."
        user.update_balance(-value)
        self.bets[user_id] = value
        return "${TagTarget(" + nickname + ")}, ставка принята."
    def result(self):
        if (len(self.bets) == 0):
            self.m_winners = ["Никто."]
            self.m_prize = 0
            return
        random_number = int(insertion.RandomNumber(0, len(self.bets) - 1).get())
        prize = 0
        for value in self.bets.values():
            prize += value
        winner = list(self.bets.keys())[random_number]
        self.update(self.bets)
        self.m_winners = [economy.users[winner].nickname]
        self.m_prize = prize

events = {
    CollectBets : ['Скидываемся все в цыганскую общину, один человек получает все! Пиши в чат: !отдатьзолото {cумма}, чтобы участвовать.', 'И победитель у нас... ${EconomyEventWinners()}. Он получает ${EconomyEventPrize()} золотца.']
}
