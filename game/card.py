class Card:
    def __init__(self, name, attack, defense, ability=None):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.ability = ability

    def apply_ability(self, target, caster):
        if self.ability:
            if self.ability == "heal":
                caster.health += 5
            elif self.ability == "double_attack":
                target.health -= self.attack * 2
            elif self.ability == "shield":
                caster.health += self.defense
            elif self.ability == "burn":
                target.health -= 3  # Additional damage over time
            # Add more abilities as needed

    def __str__(self):
        return f"{self.name} (ATK: {self.attack}, DEF: {self.defense}, ABILITY: {self.ability})"
