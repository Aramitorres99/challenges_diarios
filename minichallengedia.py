def reverse_characters(character_string):
    ''''''
    if len(character_string) == 0:
        return ""
    
    else:
        return character_string[-1] + reverse_characters(character_string[:-1]) 
    
result= reverse_characters(input("Ingrese una palabra: "))
print(result)
