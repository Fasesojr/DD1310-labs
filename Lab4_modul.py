def input_namn():
    """En modul som upprerar tills man får det korrekt angivna variabeln. En för namn"""
    namn = ""
    while True:
        try:
            namn = input("Vad heter studenten? \n")
            förnamn, efternamn = namn.split() 
            break
        except ValueError:
            print("Skriv namn i form av 'namn' 'efternamn'")
    return förnamn, efternamn
def input_int(type:str):
    """En modul som upprerar tills man får det korrekt angivna variabeln. En för int"""
    personnummer=0
    while True:
        try:
            personnummer = int(input(type))
            if(len(str(personnummer)) == 10 ):
                break
            else:
                print("Ange 10 siffrig personnummer!")
        except ValueError:
            print("Ange personnummer i siffror!") 
    return personnummer