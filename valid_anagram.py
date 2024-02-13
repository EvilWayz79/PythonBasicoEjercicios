# test if two words are valid anagrams
# anagram: sames number of letter, same component letters, same frequency of letters

# Let's complicate a little by making a fully functional hash table
# let's introduce unit test

#hashA = hash("Lorem")
#print(hashA)

def validate_anagram(a, b):
    a = input("Ingresa la primera cadena:\t ")
    b = input("Ingresa la segunda cadena:\t ")
    returnVal = 'Iguales'
    if a != b:
        returnVal = 'Diferentes'
        
    return returnVal
    

def test_validate_anagram():    
    assert validate_anagram('a','b'), "strings alike"
    
def main():
    print(validate_anagram('',''))
    

if __name__ == '__main__':
    main()