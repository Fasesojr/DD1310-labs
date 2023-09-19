import lab3_modul
"""Importerar modul filen för funktioner och felhantering"""

def a_summa(a1, d, n):  #  funktion för att beräkna en aritmetisk summa med givna parameter
    a2 = a1 + d*(n-1)
    aritmetisk_summa = n*(a1 + a2)/2
    return aritmetisk_summa

def g_summa(g1, q, n):  #  funktion för att beräkna en geometrisk summa med givna parameter
   geometrisk_summa = g1*((q**n)-1)/(q-1)
   return geometrisk_summa

def main():
    n = lab3_modul.is_int("Skriv in antal element i summorna [n]: ")
    summa1 = 0
    summa2 = 0

    val1 = lab3_modul.choice("Är den första summan aritmetisk[a] eller geometrisk[g]?\n")
    
    if val1 == "a":
        a1 = lab3_modul.is_float("Skriv in startvärde [a1]: ")
        
        d = lab3_modul.is_float("Skriv in differens [d]: ")
        
        summa1 = a_summa(a1, d, n)
    
    elif val1 == "g":
        g1 = lab3_modul.is_float("Skriv in startvärde [g1]: ")
        q = lab3_modul.is_float("Skriv in kvoten [q]: ")
        summa1 = g_summa(g1, q, n)

    val2 = lab3_modul.choice("Är den andra summan aritmetisk[a] eller geometrisk[g]?\n")  #  tar in användarens val för andra summan
    
    if val2 == "a":
        a1 = lab3_modul.is_float(input("Skriv in startvärde [a1]: "))  
        d = lab3_modul.is_float(input("Skriv in differens [d]: "))
        summa2 = a_summa(a1, d, n)  #  beräknar aritmetisk summan med givna siffror från användaren
    
    elif val2 == "g":
        g1 = lab3_modul.is_float("Skriv in startvärde [g1]: ")
        q = lab3_modul.is_float("Skriv in kvoten [q]: ")
        summa2 = g_summa(g1, q, n)  #  beräknar geometriska summan med givna siffror från användaren
    
    if summa1 > summa2:
        print("Den första summan är störst.")
   
    elif summa1 < summa2: 
        print("Den andra summan störst.")
        
    else:
        print("De två summorna är lika")
"""Huvud program med alla loopar som behövs för programmet"""

main()

