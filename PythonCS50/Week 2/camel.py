def main():
    ipt = input("camelcase: ")

    res = ""
    for char in ipt :
        if char.isupper():
            res=res +'_'+char.lower()
        else:
            res+=char
    print(res)

main()