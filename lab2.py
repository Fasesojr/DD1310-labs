def a_summa(a1, d, n):  #  funktion för att beräkna en aritmetisk summa med givna parameter
    a2 = a1 + d*(n-1)
    aritmetisk_summa = n*(a1 + a2)/2
    return aritmetisk_summa

def g_summa(g1, q, n):  #  funktion för att beräkna en geometrisk summa med givna parameter
   geometrisk_summa = g1*((q**n)-1)/(q-1)
   return geometrisk_summa


def main()):  #  Huvudprogram som körs
    summa1 = 0
    summa2 = 0
    try: 
        
        print("Antal termer i summorna: ")
        n = int(input("Skriv in antal element (n):"))
        
        val1 = input("Är den första summan aritmetisk(a) eller geometrisk(g)?")  #  tar in användarens val för första summan
        if val1 == "a":
            a1 = float(input("Skriv in startvärde (a1): "))  
            d = float(input("Skriv in differens (d): "))
            summa1 = a_summa(a1, d, n)  #  beräknar aritmetiska summan med givna siffror från användaren
        elif val1 == "g":
            g1 = float(input("Skriv in startvärde (g1): "))
            q = float(input("Skriv in kvoten (q)"))
            summa1 = g_summa(g1, q, n)  #  beräknar geometriska summan med givna siffror från användaren
        
        val2 = input("Är den andra summan aritmetisk(a) eller geometrisk(g)?")  #  tar in användarens val för andra summan
        if val2 == "a":
            a1 = float(input("Skriv in startvärde (a1): "))  
            d = float(input("Skriv in differens (d): "))
            summa2 = a_summa(a1, d, n)  #  beräknar aritmetisk summan med givna siffror från användaren
        elif val2 == "g":
            g1 = float(input("Skriv in startvärde (g1): "))
            q = float(input("Skriv in kvoten (q): "))
            summa2 = g_summa(g1, q, n)  #  beräknar geometriska summan med givna siffror från användaren
  #  Jämför värden av de 2 beräknade summorna och skriver ut antingen den största summan eller om de två summorna är lika
        if summa1 > summa2:
            print("Den första summan är störst.")
   
        elif summa1 < summa2: 
            print("Den andra summan störst.")
        
        else:
            print("De två summorna är lika")
                
    except ValueError:
        
        print("Det där var inte ett flyttal, försök igen")


        
main()