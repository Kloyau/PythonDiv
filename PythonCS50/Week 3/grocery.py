courses = {}


def main():
    while True:
        try:
            item=input()
            if item.upper() not in courses:
                courses[item.upper()] = 1
            else:
                courses[item.upper()] += 1
        except EOFError:
            myKeys = list(courses.keys())
            myKeys.sort()
            sorted_dict = {i: courses[i] for i in myKeys}
            for keys in sorted_dict:
                print (sorted_dict[keys],keys)
            exit(0)

main()
