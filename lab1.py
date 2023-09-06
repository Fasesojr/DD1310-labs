def a_följd(a1, d, n):  #  funktion för aritmetisk följd
	a2 = a1 + d*(n-1)
	a_summa = n * (a1 + a2)/2
	return a_summa

def g_följd (g1, q, n):  #  funktion för aritmetisk följd

	g_summa = g1*((q**n)-1)/(q-1)
	return g_summa

print("Skriv in startvärdet (a1): ", end="")  # frågar för input för a1
a1 = int(input())  #  sätter värdet på a1 = input och konverterar till en int

print("Skriv in differensen (d): ", end="")  # frågar för input för d
d = int(input())  #  sätter värdet på d = input och konverterar till en int

print("Skriv in antal element i följden (n): ", end="")  # frågar för input för n
n = int(input())  #  sätter värdet på n = input och konverterar till en int

print("Den aritmetiska summan är: " + str(a_följd(a1, d, n)))  #  beräknar och sedan skriver ut talföljdens resultat

print("Skriv in startvärdet (g1): ", end="")  # frågar för input för g1
g1 = int(input())  #  sätter värdet på g1 = input och konverterar till en int

print("Skriv in differensen (q): ", end="")  # frågar för input för q
q = int(input())  #  sätter värdet på q = input och konverterar till en int

print("Skriv in antal element i följden (n): ", end="")  # frågar för input för n
n = int(input())  #  sätter värdet på n = input och konverterar till en int

print("Den geometiska summan är: " + str(g_följd(g1, q, n)))  #  beräknar och sedan skriver ut talföljdens resultat