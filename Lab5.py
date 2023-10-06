import Lab4_modul
class Student:
    def __init__(self, förnamn:str, efternamn:str, personnummer:int, skola ="KTH"):
        """Init funktionen som skapar objekt utifrån klassen 'Student'"""
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnummer = personnummer
        self.skola = skola
    
    def __str__(self):
        """Init funktionen som skriver ut objektet"""
        return ("Skola: " + self.skola + "\nNamn: " + self.förnamn + " " + self.efternamn + "\nPersonnummer: " + str(self.personnummer))

class Skola:
    """Skapar en objekt utifrån klassen och agerar som en meny för användaren att skapa och spara studenter i skolan"""
    def __init__(self):
        """Init funktionen som skapar objekt utifrån klassen 'Skola'"""
        self.student = []
    
    def visa_alla(self):
      """Funktion som skriver ut alla student som är sparad i listan"""
      for student in self.student:
          print(student)
    
    def ny_student(self):
        """Funktion som skapar en objekt av klassen 'Student' utifrån input och sparar i listan i objektet 'Skola'"""
        förnamn, efternamn = Lab4_modul.input_namn()
        personnummer = Lab4_modul.input_int("Vad är Studentens personnummer? \n")
        nytt = Student(förnamn, efternamn, personnummer, skola="KTH")
        self.student.append(nytt)
        print("Objekt Skapat!")


def main():
    """Huvud funktion som skapar och sätter in studenter i lista och sedan skriver ut listan"""
    KTH = Skola()
    while True:
        val = input("Vill du skapa ny student? [ja] [nej] \n")
        if val == "ja" or val == "Ja":
            KTH.ny_student()
        elif val == "nej" or val == "Nej":
            break
        else:
            print("Svara med antingen [ja] eller [nej]! ")
    KTH.visa_alla()
main()
