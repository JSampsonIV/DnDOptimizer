def get_ability_modifier(score: int):
    if score not in range(1, 31): return None #invalid ability score
    return (score - 10) // 2 #formula for calculating ability modifier
def get_all_ability_modifiers(ability_scores: dict):
    return {key: get_ability_modifier(value) for key, value in ability_scores.items()}
def get_ability_modifiers_from_character(character):
    return {
        'strength': get_ability_modifier(character.get_strength()),
        'dexterity': get_ability_modifier(character.get_dexterity()),
        'constitution': get_ability_modifier(character.get_constitution()),
        'intelligence': get_ability_modifier(character.get_intelligence()),
        'wisdom': get_ability_modifier(character.get_wisdom()),
        'charisma': get_ability_modifier(character.get_charisma())
    }
#may not be needed, but keeping it for now
def get_ability_modifiers_from_dict(ability_scores: dict):
    return {
        'strength': get_ability_modifier(ability_scores['strength']),
        'dexterity': get_ability_modifier(ability_scores['dexterity']),
        'constitution': get_ability_modifier(ability_scores['constitution']),
        'intelligence': get_ability_modifier(ability_scores['intelligence']),
        'wisdom': get_ability_modifier(ability_scores['wisdom']),
        'charisma': get_ability_modifier(ability_scores['charisma'])
    }
def get_ability_modifier_as_string(score: int):
    modifier = get_ability_modifier(score)
    if modifier is None:
        return "Invalid ability score"
    elif modifier >= 0:
        return f"+{modifier}"
    else:
        return str(modifier)
def get_all_ability_modifiers_as_strings(ability_scores: dict):
    return {key: get_ability_modifier_as_string(value) for key, value in ability_scores.items()}