
def is_int(message):
    x = "true"
    while x != int:
        try:
            x = int(input(message))
            return x
        except ValueError:
            print("Detta är inget heltal, försök igen!")

def is_float(message):
    y = "true"
    while y != float:
        try:
            y = float(input(message))
            return y
        except ValueError:
            print("Detta är inget flyttal, försök igen!")

    


