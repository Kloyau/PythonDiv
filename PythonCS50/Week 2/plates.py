def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    Num=False
    if not(2<=len(s)<=6):
        return False
    elif s[0].isdigit() or s[1].isdigit():
        return False
    for char in s :
        if char == "0" and Num==False:
            return False
        if char.isdigit():
            Num=True
        if char in [".",",",";"," "]:
            return False
        if not(char.isdigit()) and Num==True:
            return False
    return True
main()
