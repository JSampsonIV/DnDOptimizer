#the DnD character to be assessed, with all relevant information
from CharacterClass import CharacterClass
from Species import Species
from modifiers import get_ability_modifier, get_all_ability_modifiers, get_ability_modifier_as_string, get_all_ability_modifiers_as_strings
from SpellList import SpellList
from Spell import Spell
class Character:
    #ability scores could be a dictionary, but for now, we'll keep them as separate variables
    def __init__(self, name: str, char_class: str, species: str, level: int = 1, str_score: int = 0, dex: int = 0, con: int = 0, int_score: int = 0, wis: int = 0, cha: int = 0, known_spells: set=None): #strength cannot be abbreviated to the standard str, as that's string, and same for intelligence
        self.name = name
        self.character_class = CharacterClass(char_class)
        self.species = Species(species)
        self.level = level
        #ability scores
        self.strength = str_score
        self.dexterity = dex
        self.constitution = con
        self.intelligence = int_score
        self.wisdom = wis
        self.charisma = cha
        #known spells, if any
        if known_spells is None or known_spells == set() or self.character_class.get_character_class() in set(['Barbarian', 'Fighter', 'Monk', 'Rogue']):
            pass  #no spells for these classes, so we don't need to do anything
        else:
            #initialize known_spells as an empty list
            self.known_spells = set()  #using a set to avoid duplicates
            #assign known_spells only if it's a list, otherwise raise an error
            if not isinstance(known_spells, list):
                raise TypeError("Known spells must be a list")
            #we know that known_spells is a list, so we can assign it
            else:
                for spell in known_spells:
                    if isinstance(spell, Spell):
                        #if it's a Spell object, we can add it to the list
                        self.known_spells.append(spell)
                    elif isinstance(spell, str):
                        #if it's a string, we can look it up in the spell list
                        spell_list = SpellList(self.character_class.get_character_class())
                        found_spell = spell_list.get_spell_by_name(spell_list.full_spell_list, spell)
                        if found_spell:
                            self.known_spells.add(found_spell)
                        else:
                            raise ValueError(f"Spell '{spell}' not found in the spell list for class {self.character_class.get_character_class()}")
                self.known_spells = SpellList(self.character_class.get_character_class(), self.known_spells).spell_list  #convert to a SpellList object to ensure it's valid
                    
    #getters and setters
    def get_name(self):
        return self.name
    def get_character_class(self):
        return self.character_class.get_character_class()
    def get_species(self):
        return self.species.get_species()
    def get_level(self):
        return self.level
    def get_strength(self):
        return self.strength
    def get_dexterity(self):
        return self.dexterity
    def get_constitution(self):
        return self.constitution
    def get_intelligence(self):
        return self.intelligence
    def get_wisdom(self):
        return self.wisdom
    def get_charisma(self):
        return self.charisma
    def get_known_spells(self):
        return self.known_spells
    
    def set_name(self, name: str):
        self.name = name
    def set_strength(self, str_score: int):
        self.strength = str_score
    def set_dexterity(self, dex: int):
        self.dexterity = dex
    def set_constitution(self, con: int):
        self.constitution = con
    def set_intelligence(self, int_score: int):
        self.intelligence = int_score
    def set_wisdom(self, wis: int):
        self.wisdom = wis
    def set_charisma(self, cha: int):
        self.charisma = cha
    
    def __str__(self):
        str_ability_modifiers = get_all_ability_modifiers_as_strings({
            'strength': self.strength,
            'dexterity': self.dexterity,
            'constitution': self.constitution,
            'intelligence': self.intelligence,
            'wisdom': self.wisdom,
            'charisma': self.charisma
        })
        str_strength_mod = str_ability_modifiers['strength']
        str_dexterity_mod = str_ability_modifiers['dexterity']
        str_constitution_mod = str_ability_modifiers['constitution']
        str_intelligence_mod = str_ability_modifiers['intelligence']
        str_wisdom_mod = str_ability_modifiers['wisdom']
        str_charisma_mod = str_ability_modifiers['charisma']
        
        # Print the character's information
        return f"{self.name}\nLevel {self.level} {self.species} {self.character_class}\nStrength: {self.strength} {str_strength_mod} modifier\nDexterity: {self.dexterity} {str_dexterity_mod} modifier\nConstitution: {self.constitution} {str_constitution_mod} modifier\nIntelligence: {self.intelligence}  {str_intelligence_mod} modifier\nWisdom: {self.wisdom} {str_wisdom_mod} modifier\nCharisma: {self.charisma} {str_charisma_mod} modifier\nKnown Spells: {self.known_spells if len(self.known_spells) > 0 else 'None'}"