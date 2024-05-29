def main():

    valid=False
    while not valid:
        frac=input("Fraction? ")
        if "/" in frac:
            X,Y=frac.split("/")
            if X.isdigit() and Y.isdigit() and int(Y)!=0 and int(X)<=int(Y):
                valid = True

    pr=int(int(X)/int(Y)*100) + (int(X)/int(Y)*100%1>0.5)
    if pr>=99:
        print("F")
    elif pr <= 1:
        print("E")
    else:
        print(f"{int(pr)}%")

main()
