def main(ipt):

    time=convert(ipt)
    if 7<=time<=8:
        lunch = "breakfast time"
    elif 12<=time<=13:
        lunch = "lunch time"
    elif 18<=time<=19:
        lunch = "dinner time"
    print (lunch)

def convert(time):
    h,m=time.split(":")
    h=float(h)
    m=float(m)
    return h+m/60


if __name__ == "__main__":
    main(input("hour?"))
