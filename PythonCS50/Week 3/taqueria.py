#global variables
dico = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

#main function
def main():
    total = 0
    while True:
        try:
            plat=input("Item: ")
            while not (plat.lower() in dico):
                plat=input("Item :")
            total+=dico[plat.lower()]
            print(f"${format(total, '.2f')}")
        except EOFError:
            exit(0)

main()
