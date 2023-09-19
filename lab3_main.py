import lab3_modul
"""Importerar modul filen för felhantering"""

def a_summa(a1, d, n):
    a2 = a1 + d*(n-1)
    aritmetisk_summa = n*(a1 + a2)/2
    return aritmetisk_summa
"""Funktion för att beräkna aritmetisk summa"""
def g_summa(g1, q, n):
   geometrisk_summa = g1*((q**n)-1)/(q-1)
   return geometrisk_summa
"""Funktion för att beräkna en geometrisk summa"""
def main():

    print("Data för aritmetiska summan:\n")
    a1 = lab3_modul.is_float("Skriv in startvärde [a1]: ")
    d = lab3_modul.is_float("Skriv in differens [d]: ")
    """Inmatning av data för aritmetisk summa"""

    print("Data för den geometriska summan:\n")
    g1 = lab3_modul.is_float("Skriv in startvärde [g1]: ")
    q = lab3_modul.is_float("Skriv in kvoten [q]: ")
    while q <= 0:
        q = lab3_modul.is_float("Skriv in kvoten [q]: ")
    """Inmatning av data för geometrisk summa"""
    
    n = lab3_modul.is_int("Skriv in antal element i summorna [n]: ")
    while n<=0:
        n = lab3_modul.is_int("n måste vara större än noll: ")
    """Inmatning av data för antal siffror i summorna"""
    
    if a_summa(a1, d, n) > g_summa(g1, q, n):
        print("Den aritmetiska summan är störst.")
    elif a_summa(a1, d, n) < g_summa(g1, q, n): 
        print("Den geometriska summan störst.") 
    else:
        print("De två summorna är lika")
    """if - elif - else loop som kontrollerar och skriver ut vilken summa som är störst"""
"""Huvud program med alla loopar som behövs för programmet"""

main()

