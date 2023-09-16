hero_aliases = {
    'quincy': ['quinc', 'quin', 'q'],
    'obyn': ['oby', 'o'],
    'gwen': ['g', 'gwendolyn'],
    'pat': ['fusty', 'pat fusty', 'p', 'pf'],
    'ben': ['benjamin', 'benjy', 'benj', 'be', 'benny'],
    'sauda': ['s'],
    'brickell': ['brick', 'admiral', 'admiral brickell', 'ab', 'adm'],
    'adora': ['dora', 'ado'],
    'churchill': ['captain', 'captain churchill', 'c'],
    'ezili': ['ez'],
    'ettiene': ['etn', 'et'],
    'jones': ['striker', 'striker jones', 'sj', 'st', 'j']
}

hero_data = {
    'quincy': {
        'title': 'QUINCY',
        'description': 'This is information about Quincy.',
        'image_url': 'https://raw.githubusercontent.com/Anderis/T3CBOT/main/Assets/heroes/Quincy.png',
        'color': 0xF77709  # Set the color code for Quincy
    },
    'obyn': {
        'title': '**OBYN GREENFOOT**',
        'description': 'This is information about Obyn.',
        'image_url': 'https://raw.githubusercontent.com/Anderis/T3CBOT/main/Assets/heroes/Obyn.png',
        'color': 0x1D6FA8  # Set the color code for Obyn
    },
    'gwen': {
        'title': 'Gwendolyn',
        'description': 'This is information about Quincy.',
        'image_url': 'https://raw.githubusercontent.com/Anderis/T3CBOT/main/Assets/heroes/Gwen.png',
        'color': 0xF77709  # Set the color code for Quincy

    },
    'pat': {
        'title': 'PAT FUSTY',
        'description': 'This is information about Quincy.',
        'image_url': 'https://raw.githubusercontent.com/Anderis/T3CBOT/main/Assets/heroes/Pat.png',
        'color': 0xF77709  # Set the color code for Quincy
    },
    'ben': {
        'title': 'BENJAMIN',
        'description': 'This is information about Quincy.',
        'image_url': 'https://raw.githubusercontent.com/Anderis/T3CBOT/main/Assets/heroes/Ben.png',
        'color': 0xF77709  # Set the color code for Quincy
    },
    'sauda': {
        'title': 'QUINCY',
        'description': 'This is information about Quincy.',
        'image_url': 'https://raw.githubusercontent.com/Anderis/T3CBOT/main/Assets/heroes/Sauda.png',
        'color': 0xF77709  # Set the color code for Quincy
    },
    'brickell': {
        'title': 'QUINCY',
        'description': 'This is information about Quincy.',
        'image_url': 'https://raw.githubusercontent.com/Anderis/T3CBOT/main/Assets/heroes/Brickell.png',
        'color': 0xF77709  # Set the color code for Quincy
    },
    'adora': {
        'title': 'QUINCY',
        'description': 'This is information about Quincy.',
        'image_url': 'https://raw.githubusercontent.com/Anderis/T3CBOT/main/Assets/heroes/Adora.png',
        'color': 0xF77709  # Set the color code for Quincy
    },
    'churchill': {
        'title': 'QUINCY',
        'description': 'This is information about Quincy.',
        'image_url': 'https://raw.githubusercontent.com/Anderis/T3CBOT/main/Assets/heroes/Churchill.png',
        'color': 0xF77709  # Set the color code for Quincy
    },
    'ezili': {
        'title': 'QUINCY',
        'description': 'This is information about Quincy.',
        'image_url': 'https://raw.githubusercontent.com/Anderis/T3CBOT/main/Assets/heroes/Ezili.png',
        'color': 0xF77709  # Set the color code for Quincy
    },
    'ettiene': {
        'title': 'QUINCY',
        'description': 'This is information about Quincy.',
        'image_url': 'https://raw.githubusercontent.com/Anderis/T3CBOT/main/Assets/heroes/Quincy.png',
        'color': 0xF77709  # Set the color code for Quincy
    },
    'jones': {
        'title': 'QUINCY',
        'description': 'This is information about Quincy.',
        'image_url': 'https://raw.githubusercontent.com/Anderis/T3CBOT/main/Assets/heroes/Jones.png',
        'color': 0xF77709  # Set the color code for Quincy
    }
    # Add more heroes here with their respective color codes
}


hero_costs = {
        'quincy': 'Easy: $550(495)  Medium: $650(585)\nHard: $700(630)  Impoppable: $780(730)',
        'obyn': 'Easy: [2;32m[2;33m$550[0m[2;32m[0m([2;32m495[0m)  Medium:     [2;32m[2;33m$650[0m[2;32m[0m([2;32m585[0m)\nHard: [2;33m$700[0m([2;32m630[0m)  Impoppable: [2;33m$780[0m([2;32m730[0m)',
        'gwen': '',
        'pat': '',
        'ben': '',
        'sauda': '',
        'brickell': '',
        'adora': '',
        'churchill': '',
        'ezili': '',
        'ettiene': '',
        'jones': ''
        # Add cost information for other heroes here
}

hero_stats = {
        'quincy': '# HERO DATA\n\n## **Stats(Max)**\nPierce:20\nDamage:20\nAttack-Speed:0.5s',
        'obyn': '# HERO DATA\n\n## **Stats(Max)**\nPierce:20\nDamage:20\nAttack-Speed:0.5s',
        'gwen': '# HERO DATA\n\n## **Stats(Max)**\nPierce:20\nDamage:20\nAttack-Speed:0.5s',
        'pat': 'Pierce 10',
        'ben': 'Pierce 10',
        'sauda': 'Pierce 10',
        'brickell': 'Pierce 10',
        'adora': 'Pierce 10',
        'churchill': 'Pierce 10',
        'ezili': 'Pierce 10',
        'ettiene': 'Pierce 10',
        'jones': 'Pierce 10'
}

def get_hero_info(hero_name):
    hero_name = hero_name.lower()  # Convert input to lowercase

    # Check if the input matches a hero name or alias
    for hero, aliases in hero_aliases.items():
        if hero_name == hero or hero_name in aliases:
            return hero_data.get(hero)

    # If no hero or alias matches, return None
    return None

def get_hero_cost(hero_name):
    # Convert the hero_name to lowercase to handle case-insensitive queries
    hero_name = hero_name.lower()

    # Check if the hero_name partially matches any hero name or alias
    matching_heroes = []
    for hero, aliases in hero_aliases.items():
        if hero_name == hero or hero_name in aliases:
            matching_heroes.append(hero)

    if matching_heroes:
        # If there are matching heroes, return the cost information for the first matching hero found
        return hero_costs.get(matching_heroes[0])

    return None  # Return None if cost information is not available for the partial match