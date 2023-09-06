def a_följd(a1, d, n):  #  funktion för aritmetisk följd
	a2 = a1 + d*(n-1)
	a_summa = n * (a1 + a2)/2
	return a_summa

def g_följd (g1, q, n):  #  funktion för geometrisk följd

	g_summa = g1*((q**n)-1)/(q-1)
	return g_summa

  #  Frågar för värden som används för att skapa variablerna som behövs och sedan insättes in i funktionen a_följd
a1 = int(input("Skriv in startvärdet (a1): "))
d = int(input("Skriv in differensen (d): "))
n = int(input("Skriv in antal element i följden (n): "))
print("Den aritmetiska summan är: " + str(a_följd(a1, d, n)))  #  beräknar och sedan skriver ut talföljdens summa


  #  Exakt samma sak som i förra kod bunten som fyller upp variablarna som vi behöver för geometriska följden och insätter det in i funktionen g_följd
g1 = int(input("Skriv in startvärder (g1): "))
q = int(input("Skriv in differensen (q): ")) 
n = int(input("Skriv in antal element i följden (n): "))

print("Den geometiska summan är: " + str(g_följd(g1, q, n)))  #  beräknar och sedan skriver ut talföljdens summa
