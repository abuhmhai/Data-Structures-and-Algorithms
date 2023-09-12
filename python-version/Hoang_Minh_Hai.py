def decimal_to_binary(n):
    x=""
    if n==0:
        x=""
    else:
        while n>0:
            x=str(n%2)+x
            n//=2
    return x

if __name__=="__main__":
    while True:
        try:
            d=int(input("Nhập số thập phân n(n>=0): "))
            if d<0:
              print("Vui lòng nhập một số nguyên không âm")
            else:
                b=decimal_to_binary(d)
                print("Số nhị phân tương ứng là: ",b)
                break
        except ValueError:
         print("Vui lòng nhập một số nguyên dương.")

