full_dot = '●'
empty_dot = '○'
def create_character(character_name,strength,intelligence,charisma):
    if not isinstance(character_name,str):
        return 'The character name should be a string'
    elif len(character_name) > 10:
        return 'The character name is too long'
    elif character_name =='':
        return 'The character should have a name'
    elif ' 'in character_name:
        return 'The character name should not contain spaces'
    elif not isinstance(strength,int)or not isinstance(intelligence,int) or not isinstance(charisma,int):

        return 'All stats should be integers'
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    elif strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    else:
        name = character_name
        stre = "STR " + (full_dot * strength) + (empty_dot * (10 - strength))
        intel = "INT " + (full_dot * intelligence) + (empty_dot * (10 - intelligence))
        cha = "CHA " + (full_dot * charisma) + (empty_dot * (10 - charisma))
        return name + "\n" + stre+"\n" +intel+"\n"+cha
print(create_character('koushik',3,2,2))