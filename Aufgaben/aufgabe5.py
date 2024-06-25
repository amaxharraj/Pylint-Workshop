#AUFGABE 5

# a) Was macht folgender Code?

def f(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0: return False
        return True
def main():
    n = 20
    for i in range(2, n):
        if f(i): print(i)
        
if __name__ == "__main__":
    main()



