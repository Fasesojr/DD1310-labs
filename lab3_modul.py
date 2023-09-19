
def is_int(a):
    try:
        x = int(a)
    except ValueError:
        print("Detta är ingen heltal, försök igen!")

def is_float(b):
    try:
        y = float(b)
    except ValueError:
        print("Detta är inget flyttal, försök igen!")

def a_summa(a1, d, n):  #  funktion för att beräkna en aritmetisk summa med givna parameter
    a2 = a1 + d*(n-1)
    aritmetisk_summa = n*(a1 + a2)/2
    return aritmetisk_summa

def g_summa(g1, q, n):  #  funktion för att beräkna en geometrisk summa med givna parameter
   geometrisk_summa = g1*((q**n)-1)/(q-1)
   return geometrisk_summa

