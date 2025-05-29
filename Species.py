class Species:
    def __init__(self, species: str):
        if not isinstance(species, str):
            raise TypeError("Species must be a string")
        if species.lower() not in ['dragonborn', 'dwarf', 'elf', 'gnome', 'halfling', 'half-orc', 'human', 'tiefling']:
            raise ValueError(f"Invalid species: {species}. Valid species are: dragonborn, dwarf, elf, gnome, halfling, half-orc, human, tiefling")
        self.species = species
        pass

    def get_species(self):
        return self.species
    
    def get_species_as_string(self):
        return self.species.capitalize()

    def get_species_bonuses(self):
        species_bonuses = {
            'dragonborn': {'strength': 2, 'dexterity': 0, 'constitution': 0, 'intelligence': 0, 'wisdom': 0, 'charisma': 1},
            'dwarf': {'strength': 0, 'dexterity': 0, 'constitution': 2, 'intelligence': 0, 'wisdom': 0, 'charisma': 0},
            'elf': {'strength': 0, 'dexterity': 2, 'constitution': 0, 'intelligence': 0, 'wisdom': 0, 'charisma': 0},
            'gnome': {'strength': 0, 'dexterity': 0, 'constitution': 0, 'intelligence': 2, 'wisdom': 0, 'charisma': 0},
            'half-elf': {'strength': 0, 'dexterity': 0, 'constitution': 0, 'intelligence': 0, 'wisdom': 0, 'charisma': 2},
            'half-orc': {'strength': 2, 'dexterity': 0, 'constitution': 1, 'intelligence': 0, 'wisdom': 0, 'charisma': 0},
            'human': {'strength': 1, 'dexterity': 1, 'constitution': 1, 'intelligence': 1, 'wisdom': 1, 'charisma': 1},
            'tiefling': {'strength': 0, 'dexterity': 0, 'constitution': 1, 'intelligence': 0, 'wisdom': 0, 'charisma': 2}
            # half-elves are not included due to the choice of two ability scores
            # that can be increased by 1
        }
        return species_bonuses.get(self.species.lower(), {})
    
    def __str__(self):
        return self.species.capitalize()