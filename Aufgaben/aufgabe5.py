#AUFGABE 5

# Zusatzaufgabe
# Versuche den Code so schlecht wie möglich zu machen, er sollte jedoch funktioneren!

'''Modul'''
def sort_numbers(numbers):
    'Nummern sortieren'
    return sorted(numbers)

def main():
    'Nummern'
    numbers = [5, 3, 6, 2, 10]
    sorted_numbers = sort_numbers(numbers)
    print(sorted_numbers)

if __name__ == "__main__":
    main()
