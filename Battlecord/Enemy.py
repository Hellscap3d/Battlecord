
class Enemy(object):
    def __init__(self):
        self.name = 'Enemy'
        self.description = 'This is an enemy.'
        self.power = 5
        self.coins = 5
        self.emoji = '<:slime:1106744847148253335>'
        self.boss = False
        self.buffs = []
        self.debuffs = []
    
    def calc(self):
        for buff in self.buffs:
            self.power += buff.modifier
        for debuff in self.debuffs:
            self.power += debuff.modifier # negative modifier = debuff