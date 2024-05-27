class Card:
    def __init__(self, name, attack, ability=None):
        self.name = name
        self.attack = attack
        self.ability = ability
    
    def apply_ability(self, opponent, player):
        if self.ability == "heal":
            player.health += 5
        elif self.ability == "damage":
            opponent.health -= 5
        elif self.ability == "boost":
            player.health += 3
            opponent.health -= 3

    def __str__(self):
        return f"{self.name} (Attack: {self.attack}, Ability: {self.ability})"
