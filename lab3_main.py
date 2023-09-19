import lab3_modul
"""Importerar modul filen för funktioner och felhantering """

def main():  #  huvudprogram
    
    n = lab3_modul.is_int(input("Skriv in antal element i summorna [n]: "))
    
    val1 = input("Är den första summan aritmetisk[a] eller geometrisk[g]?\n")
    
    if val1 == "a":
        a1 = lab3_modul.is_float(input("Skriv in startvärde [a1]: "))
        d = lab3_modul.is_float(input("Skriv in differens [d]: "))
        summa1 = lab3_modul.a_summa(a1, d, n)
    
    elif val1 == "g":
        g1 = lab3_modul.is_float(input("Skriv in startvärde [g1]: "))
        q = lab3_modul.is_float(input("Skriv in kvoten [q]: "))
        summa1 = lab3_modul.g_summa(g1, q, n)
   
    
    val2 = input("Är den andra summan aritmetisk[a] eller geometrisk[g]?")  #  tar in användarens val för andra summan
    
    if val2 == "a":
        a1 = lab3_modul.is_float(input("Skriv in startvärde [a1]: "))  
        d = lab3_modul.is_float(input("Skriv in differens [d]: "))
        summa2 = lab3_modul.a_summa(a1, d, n)  #  beräknar aritmetisk summan med givna siffror från användaren
    
    elif val2 == "g":
        g1 = lab3_modul.is_float(input("Skriv in startvärde [g1]: "))
        q = lab3_modul.is_float(input("Skriv in kvoten [q]: "))
        summa2 = lab3_modul.g_summa(g1, q, n)  #  beräknar geometriska summan med givna siffror från användaren
    
    if summa1 > summa2:
        print("Den första summan är störst.")
   
    elif summa1 < summa2: 
        print("Den andra summan störst.")
        
    else:
        print("De två summorna är lika")

main()

