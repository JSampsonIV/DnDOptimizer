from rollDice import rollD4, rollD6, rollD8, rollD10, rollPercentile, rollD12, rollD20
from modifiers import get_ability_modifier
from CharacterClass import CharacterClass
from Species import Species
from Character import Character
from SpellList import SpellList

arrako = Character('Arrako', 'Cleric', 'Tiefling', 5, 14, 12, 17, 15, 20, 16, ['Cure Wounds', 'Guiding Bolt', 'Shield of Faith'])
print(f"Known Spells: {arrako.get_known_spells()}")