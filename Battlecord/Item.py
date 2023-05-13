
class Item(object):
    def __init__(self): 
        self.name = 'Item' # This is the name of the item.
        self.description = 'This is an item.' # This is the description of the item.
        self.modifier = 5 # This adds 5 to the user's POWER stat, which is their attack power, aka their only stat.
        self.cost = 5 # This is the cost of the item in the shop.
        self.type = 'weapon' # This is the type of the item. It can be 'weapon' or 'consumable'.
        self.rarity = 'common' # This is the rarity of the item. It can be 'common', 'uncommon', 'rare', 'epic', or 'legendary'.
        self.emoji = '<:stick:1106740776311992323>' # This is the discord emoji that will be used to represent the item.
    
    def use(self, user, target):
        user.inventory.remove(self)
        target.debuffs.append(self)
    def equip(self, user):
        user.inventory.remove(self)
        user.buffs.append(self)
        user.power += self.modifier
        return f'You equipped {self.name}!'
    def unequip(self, user):
        user.buffs.remove(self)
        user.inventory.append(self)
        user.power -= self.modifier
        return f'You unequipped {self.name}!'
    def buy(self, user):
        if user.coins < self.cost:
            return f'You don\'t have enough coins to buy {self.name}!'
        user.coins -= self.cost
        user.inventory.append(self)
        return f'You bought {self.name}!'