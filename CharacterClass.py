class CharacterClass:
    def __init__(self, char_class: str):
        # Validate the character class
        valid_classes = ['Artificer','Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
        if char_class not in valid_classes:
            raise ValueError(f"Invalid character class: {char_class}. Valid classes are: {', '.join(valid_classes)}")
        self.character_class = char_class

    def get_character_class(self):
        return self.character_class
    
    def __str__(self):
        return self.character_class
    
    #class will be immutable for now, so no setter