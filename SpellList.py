import csv
from Spell import Spell
from CharacterClass import CharacterClass
from Species import Species

#TODO: Add spells given by species, like Tiefling's Hellish Rebuke and Thaumaturgy
class SpellList:
    def __init__(self, char_class: str, spell_list: set=None, file_path: str='dnd-spells.csv'):
        self.full_spell_list = self.create_full_spell_list(file_path)
        if not isinstance(char_class, str):
            raise TypeError("Character class must be a string")
        self.char_class = CharacterClass(char_class)
        self.spell_list = spell_list if spell_list is not None else []
        for spell in self.spell_list:
            if not isinstance(spell, Spell):
                if not isinstance(spell, str):
                    raise TypeError("Spell must be a Spell object or a string")
                #lookup the spell by name in the full spell list
                spell = self.get_spell_by_name(self.full_spell_list, spell)
                if spell is None:
                    raise ValueError(f"Spell '{spell}' not found in the full spell list")
                spell_list.append(Spell(spell['name'], spell['level'], spell['casting_time'], spell['range'], spell['duration']))
            else:
                print(f"Adding spell: {spell.get_name()}")
                spell_list.add(spell)
                print(len(spell_list))

    def create_full_spell_list(self, file_path: str='dnd-spells.csv'):
        # Create a dictionary to hold spells for each class
        # The key is the class name, and the value is a list of spells
        # Each spell is represented as a list of its attributes
        # [name, level, casting time, range, duration]
        
        # Read the CSV file and populate the spell list
        spell_list = {}
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            # Read the entire CSV file into a list
            next(reader)  # Skip the header row
            for row in reader:
                classes = row[1]
                for char_class in classes.split(','):
                    char_class = char_class.strip()
                    if char_class not in spell_list:
                        spell_list[char_class] = set()  # Initialize an empty set for the class if it doesn't exist
                    added_spell = Spell(row[0], int(row[2]), row[4], row[5], row[6], row[11]) #name, level, casting time, range, duration, description
                    spell_list[char_class].add(added_spell) 
        return spell_list

    def get_spell_list_by_class(self, spell_list: dict, char_class: str):
        # Return the list of spells for the given class
        return spell_list.get(char_class, [])

    def get_spell_list_by_level(self, spell_list: dict, char_class: str, level: int):
        # Return the list of spells for the given class and level
        spells = self.get_spell_list_by_class(spell_list, char_class)
        return [spell for spell in spells if int(spell[1]) == level]

    def get_spell_by_name(self, full_spell_list: dict, spell_name: str):
        # Search for a spell by its name in the full spell list
        for char_class, spells in full_spell_list.items():
            for spell in spells:
                if spell.get_name().lower() == spell_name.lower():
                    return Spell(
                        name=spell.get_name(),
                        level=spell.get_level(),
                        casting_time=spell.get_casting_time(),
                        range_=spell.get_range(),
                        duration=spell.get_duration(),
                        description=spell.get_description()
                    )
        return None  # Spell not found
    
    def get_spell_list(self):
        return self.spell_list
    
    def __str__(self):
        return_value = ''
        for spell in self.known_spells:
            return_value += spell.get_name()
            if spell != self.known_spells[-1]:
                return_value += ', '
        return return_value