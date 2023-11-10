a=float(input("Enter your unit : "))
if a<=100:
    e=float(input("enter fule bill charges : "))
    b=a*4.41 #electric bill stored
    print("electric bill :",b)
    c=126 #fixed charges
    print("fixed charges :",c)
    d=a*1.35 # transmission bill
    print("transmission bill :",d)
    print("fule bill :",e)
    f=(b+c+d+e)*16/100 # Power charges on bill
    print("power charges :",f)
    g=0.0 # mahavitran does not take electric sale tax
    print("electric sale tax :",g)
    h=b+c+d+e+f+g
    print("Total Bill :",h)

if a<=300:
    e=float(input("enter fule bill charges : "))
    b=(100*4.41)+(a-100)*9.64 #electric bill stored
    print("electric bill :",b)
    c=126 #fixed charges
    print("fixed charges :",c)
    d=a*1.17 # transmission bill
    print("transmission bill :",d)
    print("fule bill :",e)
    f=(b+c+d+e)*16/100 # Power charges on bill
    print("power charges :",f)
    g=0.0 # mahavitran does not take electric sale tax
    print("electric sale tax :",g)
    h=b+c+d+e+f+g
    print("Total Bill :",h)
if a<=500:
    e=float(input("enter fule bill charges : "))
    b=(100*4.41)+(200*9.64)+(500-a)*13.61 #electric bill stored
    print("electric bill :",b)
    c=126 #fixed charges
    print("fixed charges :",c)
    d=a*1.17 # transmission bill
    print("transmission bill :",d)
    print("fule bill :",e)
    f=(b+c+d+e)*16/100 # Power charges on bill
    print("power charges :",f)
    g=0.0 # mahavitran does not take electric sale tax
    print("electric sale tax :",g)
    h=b+c+d+e+f+g
    print("Total Bill :",h)

if a<=1000:
    e=float(input("enter fule bill charges : "))
    b=(100*4.41)+(200*9.64)+(200*13.61)+(1000-a) #electric bill stored
    print("electric bill :",b)
    c=126 #fixed charges
    print("fixed charges :",c)
    d=a*1.17 # transmission bill
    print("transmission bill :",d)
    print("fule bill :",e)
    f=(b+c+d+e)*16/100 # Power charges on bill
    print("power charges :",f)
    g=0.0 # mahavitran does not take electric sale tax
    print("electric sale tax :",g)
    h=b+c+d+e+f+g
    print("Total Bill :",h)

    if a>1000:
        e=float(input("enter fule bill charges : "))
        b=(100*4.41)+(200*9.64)+(200*13.61)+(a-1000)*15.57 #electric bill stored
        print("electric bill :",b)
        c=126 #fixed charges
        print("fixed charges :",c)
        d=a*1.17 # transmission bill
        print("transmission bill :",d)
        print("fule bill :",e)
        f=(b+c+d+e)*16/100 # Power charges on bill
        print("power charges :",f)
        g=0.0 # mahavitran does not take electric sale tax
        print("electric sale tax :",g)
        h=b+c+d+e+f+g
        print("Total Bill :",h)