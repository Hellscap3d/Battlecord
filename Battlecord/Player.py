class Player(object):
    def __init__(self,uid,bot):
        if bot.player.exists:
            self = bot.player.get(uid)
        else:
            self.id = uid
            self.name = None
            self.description = None
            self.power = 5
            self.coins = 0
            self.buffs = []
            self.debuffs = []
            self.inventory = []
            self.exists = True
            self.bot = bot
            self.bot.player.insert(self.id,self)
        
    def calc(self):
        for buff in self.buffs:
            self.power += buff.modifier
        for debuff in self.debuffs:
            self.power += debuff.modifier
    
    def save(self):
        self.bot.player.update(self.id,self)
    
    def delete(self):
        self.bot.player.delete(self.id)
    
    def buy(self,item):
        if self.coins < item.cost:
            return f'You don\'t have enough coins to buy {item.name}!'
        self.coins -= item.cost
        self.inventory.append(item)
        return f'You bought {item.name}!'
    
    def use(self,item,target):
        item.use(self,target)
    
    def equip(self,item):
        item.equip(self)
    
    def unequip(self,item):
        item.unequip(self)
    
    def attack(self,target):
        bp = self.power - target.power # check if the bp is positive or negative, and then use that to determine the winner
        if bp > 0:
            self.coins += target.coins
            self.power += target.power
            return f'You won!'
        elif bp < 0:
            target.coins += self.coins
            target.power += self.power
            return f'You lost!'
        else:
            return f'You reached a stalemate!'