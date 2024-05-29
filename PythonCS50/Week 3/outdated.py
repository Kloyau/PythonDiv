month_list=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    valid = False
    while not(valid):

        date=input("Date : ")

        if "/" in date:
            m,d,y = date.split("/")
            try:
                d=int(d)
                m=int(m)
                if 1<=m<=12 and 1<=d<=31:
                    valid=True
            except ValueError:
                date=input("Date : ")

        else:
            m,d,y = date.split(" ")
            d = d[:-1]
            if "," in date:
                try:
                    d=int(d)
                    if m in month_list and 1<=d<=31:
                        valid=True
                except ValueError:
                    date=input("Date : ")

            m = month_list.index(m)+1


    print(f"{int(y)}-{m:02}-{d:02}")
main()
