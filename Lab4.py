import Lab4_modul
class Student:
    def __init__(self, förnamn:str, efternamn:str, personnummer:int):
        """Init funktionen som skapar objekt utifrån klassen 'Student'"""
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnummer = personnummer
    
    def __str__(self):
        """Init funktionen som skriver ut objektet"""
        return ("Namn: " + self.förnamn + " " + self.efternamn + "\nPersonnummer: " + str(self.personnummer))

def main():
    """Huvud funktion som skapar och sätter in studenter i lista och sedan skriver ut listan"""
    studentlista = []
    while True:
        val = input("Vill du skapa ny student? [ja] [nej] \n")
        if val == "ja" or val == "Ja":
            förnamn, efternamn = Lab4_modul.input_namn()
            personnummer = Lab4_modul.input_int("Vad är Studentens personnummer? \n")
            studentlista.append(Student(förnamn, efternamn, personnummer))
            print("Objekt Skapat!")
        elif val == "nej" or val == "Nej":
            break
        else:
            print("Svara med antingen [ja] eller [nej]! ")
    for x in range(len(studentlista)):
        print (str(studentlista[x]))
main()
