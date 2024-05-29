def main():
    ipt = input("Input: ")
    res= ""
    for char in ipt:
        if char.lower() not in ['a','e','i','o','u']:
            res+=char

    print(res)

main()