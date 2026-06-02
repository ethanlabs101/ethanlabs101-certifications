# ----- freecodecamp Build an RPG Character workshop -----
#
# --------------------------------------------------------
#
# Overview:
#
# In this project, I was instructed to make a small RPG
# character application. The instructions are as follows:
#
# 1. You should have a function named create_character.
#
# 2. The function should accept, in order, a character name followed by three stats: strength, intelligence, and charisma.
#
# 3. The character name should be validated:
#    - If the character name is not a string, the function should return The character name should be a string.
#    - If the character name is an empty string, the function should return The character should have a name.
#    - If the character name is longer than 10 characters, the function should return The character name is too long.
#    - If the character name contains spaces, the function should return The character name should not contain spaces.
#
# 4. The stats should also be validated:
#    - If one or more stats are not integers, the function should return All stats should be integers.
#    - If one or more stats are less than 1, the function should return All stats should be no less than 1.
#    - If one or more stats are more than 4, the function should return All stats should be no more than 4.
#    - If the sum of all stats is different than 7, the function should return The character should start with 7 points.
#
# 5. If all values pass the verification, the function should return a string with four lines:
#    - the first line should contain the character name
#    - lines 2-4 should start with the stat abbreviation, STR, INT or CHA (in this order), then a space,
#      and then a number of full dots (●) equal to the value of the stat, and a number of empty dots (○) to reach 10.
#      Example: if the value of strength is 3 there must be 3 full dots followed by 7 empty dots. The dots are given in the editor.
#
# Here's the string that should be returned by create_character('ren', 4, 2, 1):
#
#    ren
#  STR ●●●●○○○○○○
#  INT ●●○○○○○○○○
#  CHA ●○○○○○○○○○
#
# --------------------------------------------------------
# Here is the freecodecamp project below. I decided to practice some of the concepts learned during this project and
# previous lessons so I extended scope a little beyond what the project asked for just to get a good grasp of what I
# am learning. You will find the extended version below this one along with explanations on how it works.
#
#
# full_dot = '●'
# empty_dot = '○'
#
# def create_character(name, strength, intelligence, charisma):
#     if not isinstance(name, str):
#         return 'The character name should be a string'
#     if name == '':
#         return 'The character should have a name'
#     if len(name) > 10:
#         return 'The character name is too long'
#     if ' ' in name:
#         return 'The character name should not contain spaces'
#
#     stats = (strength, intelligence, charisma)
#     for s in stats:
#         if not isinstance(s, int):
#             return 'All stats should be integers'
#         if s < 1:
#             return 'All stats should be no less than 1'
#         if s > 4:
#             return 'All stats should be no more than 4'
#     if sum(stats) != 7:
#         return 'The character should start with 7 points'
#
#     full_strength = full_dot * strength
#     empty_strength = (10-strength)* empty_dot
#     full_intelligence = full_dot * intelligence
#     empty_intelligence = (10-intelligence)* empty_dot
#     full_charisma = full_dot * charisma
#     empty_charisma = (10-charisma)* empty_dot
#
#     return f"{name}\nSTR {full_strength}{empty_strength}\nINT {full_intelligence}{empty_intelligence}\nCHA {full_charisma}{empty_charisma}"
#
# character = create_character('ren', 4, 2, 1)
#
# print(character)
#
#
# [END OF FREECODECAMP EXAMPLE]
# --------------------------------------------------------
#
# Extension Summary:
#
# The original workshop required only three stats:
# Strength, Intelligence, and Charisma.
#
# To further practice Python fundamentals, I expanded the
# project by:
#
# - Adding a fourth stat (Mana)
# - Creating character classes
# - Adding flavor text based on stat values
# - Building a terminal user interface
# - Adding screen clearing between menus
# - Returning multiple values from a function
#
# The goal was not to improve the assignment itself, but to
# gain additional practice with conditionals, functions,
# tuples, user input, string formatting, and simple game logic.
#
# --------------------------------------------------------

import os

full_mana = '★'
empty_mana = '☆'
full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma, mana):

    strength_message = ''
    intelligence_message = ''
    charisma_message = ''
    mana_message = ''
    class_category = ''

    if not isinstance(name, str):
        return 'The character name should be a string'

    if name == '':
        return 'The character should have a name'

    if len(name) > 10:
        return 'The character name is too long'

    if ' ' in name:
        return 'The character name should not contain spaces'

    # Messages
    if strength >= 5:
        strength_message = 'With great power comes great responsibility'
    elif strength <= 2:
        strength_message = 'Time to hit the gym!'

    if intelligence >= 5:
        intelligence_message = 'Hello, Albert Einstein'
    elif intelligence <= 2:
        intelligence_message = 'Oooga Booga!'

    if charisma >= 5:
        charisma_message = 'A natural leader'
    elif charisma <= 2:
        charisma_message = 'Keep your head up!'

    if mana >= 5:
        mana_message = 'Chill out Harry Potter!'
    elif mana <= 1:
        mana_message = 'Can\'t cast a spell weakling?'

    # Class logic
    if strength + intelligence >= 8:
        class_category = 'Assassin'
    elif intelligence + charisma >= 8:
        class_category = 'Overlord'
    elif strength + mana >= 8:
        class_category = 'Sorceror'
    elif intelligence + mana >= 8:
        class_category = 'Necromancer'
    else:
        class_category = 'Rogue'

    # Stats validation
    stats = (strength, intelligence, charisma, mana)

    for s in stats:
        if not isinstance(s, int):
            return 'All stats should be integers'
        if s < 1:
            return 'All stats should be no less than 1'
        if s > 7:
            return 'All stats should be no more than 7'

    if sum(stats) != 10:
        return 'The character should start with 10 points'

    # UI bars
    charged_mana = full_mana * mana
    no_mana = (10 - mana) * empty_mana

    full_strength = full_dot * strength
    empty_strength = (10 - strength) * empty_dot

    full_intelligence = full_dot * intelligence
    empty_intelligence = (10 - intelligence) * empty_dot

    full_charisma = full_dot * charisma
    empty_charisma = (10 - charisma) * empty_dot

    line = '----------'

    return (
    f"{name}\n{line}\nSTR {full_strength}{empty_strength}\nINT {full_intelligence}{empty_intelligence}\nCHA {full_charisma}{empty_charisma}\nMAN {charged_mana}{no_mana}",
    strength_message,
    intelligence_message,
    charisma_message,
    mana_message,
    class_category
)


def clear():
    os.system('clear')


clear()


def create_banner():
    print("---------------------------------------------------")
    print(" Create Your Character. Stats Must equal 10 Total. ")
    print("---------------------------------------------------")


create_banner()

name = input("Name: ")
clear()


def entered_banner():
    print("---------------------------------------------------")
    print(" Create Your Character. Stats Must equal 10 Total. ")
    print(f"         {name}? Hmm thats a great name!          ")
    print("---------------------------------------------------")


entered_banner()

strength = int(input("(Choose a Number 1-7)\nStrength: "))
clear()
entered_banner()

intelligence = int(input("(Choose a Number 1-7)\nIntelligence: "))
clear()
entered_banner()

charisma = int(input("(Choose a Number 1-7)\nCharisma: "))
clear()
entered_banner()

mana = int(input("(Choose a Number 1-7)\nMana: "))
clear()

character, strength_message, intelligence_message, charisma_message, mana_message, class_category = create_character(name, strength, intelligence, charisma, mana)

print("--------------------------------------------------")
print(f"         This is the story of {name}.            ")
print("--------------------------------------------------")
print()
print(f"{character}              Class: {class_category} ")
print("--------------------------------------------------")
print(f"{strength_message}\n{intelligence_message}\n{charisma_message}\n{mana_message}")
print("--------------------------------------------------")
end = input("\n------------- Press Enter to Exit ----------------\n")
clear()


# -------------------------------------------------------------
#
# Concepts learned in this exercise:
#
# 1. input()
#    Used to gather information from the user while the program
#    is running. In this project it is used to collect the
#    character name and stat values.
#
# 2. f-strings
#    Used to embed variables directly into strings.
#
#    Example:
#    f"Welcome {name}"
#
#    This makes formatting output much cleaner and easier to read.
#
# 3. Escape characters and formatting
#    The newline character (\n) is used throughout the project
#    to create readable character sheets and terminal layouts.
#
# 4. Validation
#    Validation ensures the user enters data that follows the
#    rules of the application before processing it further.
#
#    Examples:
#    - Name must be a string.
#    - Name cannot contain spaces.
#    - Stats must be integers.
#    - Stats must remain within allowed ranges.
#
# 5. isinstance()
#    Used to verify the type of a value.
#
#    Example:
#    isinstance(strength, int)
#
#    This prevents unexpected data types from being processed.
#
# 6. Tuples
#    Tuples are used to group the character stats together for
#    validation and summation.
#
#    Example:
#    stats = (strength, intelligence, charisma, mana)
#
# 7. Loops
#    A for loop is used to iterate through each stat and apply
#    the same validation rules without duplicating code.
#
# 8. String multiplication
#    Python allows strings to be multiplied by integers.
#
#    Example:
#    '●' * 5
#
#    Output:
#    ●●●●●
#
#    This technique is used to create visual stat bars.
#
# 9. Functions
#    Functions were used to organize the project into reusable
#    pieces of logic.
#
#    Examples:
#    - create_character()
#    - clear()
#    - create_banner()
#    - entered_banner()
#
# 10. Returning multiple values
#     create_character() returns multiple pieces of information
#     at once by returning a tuple.
#
#     Example:
#     return (
#         character,
#         strength_message,
#         intelligence_message,
#         charisma_message,
#         mana_message,
#         class_category
#     )
#
#     These values can then be unpacked into separate variables.
#
# 11. Basic game logic
#     This project introduced simple game design concepts:
#
#     - Character creation
#     - Attribute systems
#     - Class assignment
#     - Conditional events
#     - User feedback through flavor text
#
# 12. Consistent return values
#
#
#     One issue encountered during development was returning
#     either a string or a tuple from create_character().
#
#     When validation failed, the function returned a string.
#     When validation succeeded, the function returned multiple
#     values packed inside a tuple.
#
#     This caused a ValueError when Python attempted to unpack
#     a string into multiple variables.
#
#
#     Lesson learned:
#     Functions should ideally return data in a consistent
#     format to avoid unexpected runtime errors.
# -------------------------------------------------------------
#
# Additional features added beyond the original workshop:
#
# - Added a fourth stat (Mana)
# - Added character classes
# - Added flavor text for stat values
# - Added terminal screen clearing
# - Added interactive character creation menus
# - Added visual mana bars using stars
# - Added a more game-like presentation layer
#
# These additions were not required by the workshop but were
# implemented to reinforce concepts learned throughout previous
# freeCodeCamp Python exercises.
#
# -------------------------------------------------------------
#
# Example output:
#
#   --------------------------------------------------
#            This is the story of ethanlabs.
#   --------------------------------------------------
#
#   ethanlabs
#   ----------
#   STR ●●○○○○○○○○
#   INT ●●●●●○○○○○
#   CHA ●●○○○○○○○○
#   MAN ★☆☆☆☆☆☆☆☆☆              Class: Rogue
#   --------------------------------------------------
#   Time to hit the gym!
#   Hello, Albert Einstein
#   Keep your head up!
#   Can't cast a spell weakling?
#   --------------------------------------------------
#
#   ------------- Press Enter to Exit ----------------
#
#
#
# -------------------------------------------------------------
