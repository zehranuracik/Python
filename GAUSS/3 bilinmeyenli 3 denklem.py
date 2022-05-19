print("""         3 BILINMEYENLI 3 DENKLEMLI MATRIS COZUMU
                     GAUSS YONTEMI""")

a1,a2,a3,a4 = input("1. denklemin katsayilarini ve sonucunu giriniz: ").split()
a1 = int(a1)
a2 = int(a2)
a3 = int(a3)
a4 = int(a4)
b1,b2,b3,b4 = input("2. denklemin katsayilarini ve sonucunu giriniz: ").split()
b1 = int(b1)
b2 = int(b2)
b3 = int(b3)
b4 = int(b4)
c1,c2,c3,c4 = input("3. denklemin katsayilarini ve sonucunu giriniz: ").split()
c1 = int(c1)
c2 = int(c2)
c3 = int(c3)
c4 = int(c4)
print("")
print(""" Matris:
      {}    {}    {}    |  {}
      {}    {}    {}    |  {}
      {}    {}    {}    |  {}""".format(a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3,c4))
print("")
print("1. denklem = S1    2. denklem = S2   3. denklem = S3 \n")
a = -b1 / a1
b = b1 / a1
c = -c1 / a1
d = c1 / a1

print(""" Tips:
1) {}*S1 + S2 --> S2
2) {}*S1 - S2 --> S2

""".format(a, b))
print("")
while True:
    secim = int(input("Yapilacak denklemin numarasini giriniz: "))
    print("")
    if(secim == 1):
        b1 = a * a1 + b1
        b2 = a * a2 + b2
        b3 = a * a3 + b3
        b4 = a * a4 + b4

        print(""" Yeni Matris:
                      {}    {}    {}    |  {}
                      {}    {}    {}    |  {}
                      {}    {}    {}    |  {}""".format(a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4))

    if (secim == 2):
        b1 = b*a1 - b1
        b2 = b*a2 - b2
        b3 = b*a3 - b3
        b4 = b*a4 - b4

        print(""" Yeni Matris:
                      {}    {}    {}    |  {}
                      {}    {}    {}    |  {}
                      {}    {}    {}    |  {}""".format(a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4))
    if(b1==0):
        print("")
        print("""Tips:
        3) {}*S1 + S3 --> S3
        4) {}*S1 - S3 --> S3""".format(c,d))

    if (secim == 3):
        c1 = c*a1 + c1
        c2 = c*a2 + c2
        c3 = c*a3 + c3
        c4 = c*a4 + c4

        print(""" Yeni Matris:
                        {}    {}    {}    |  {}
                        {}    {}    {}    |  {}
                        {}    {}    {}    |  {}""".format(a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4))

    if (secim == 4):
        c1 = d * a1 - c1
        c2 = d * a2 - c2
        c3 = d * a3 - c3
        c4 = d * a4 - c4

        print(""" Yeni Matris:
                        {}    {}    {}    |  {}
                        {}    {}    {}    |  {}
                        {}    {}    {}    |  {}""".format(a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4))
    e = -c2 / b2
    f = c2 / b2
    if(b1==0 and c1 == 0):
        print("")
        print("""Tips:
        5) {}*S2 + S3 --> S3
        6) {}*S2 - S3 --> S3""".format(e,f))
    print("")
    if(secim == 5):
        c1 = e*b1 + c1
        c2 = e*b2 + c2
        c3 = e*b3 + c3
        c4 = e*b4 + c4
        print(""" Yeni Matris:
                        {}    {}    {}    |  {}
                        {}    {}    {}    |  {}
                        {}    {}    {}    |  {}""".format(a1, a2, a3, a4, b1, b2, b3, b4, c1, c2,c3,c4))

    if (secim == 6):
        c1 = f * b1 - c1
        c2 = f * b2 - c2
        c3 = f * b3 - c3
        c4 = f * b4 - c4
        print(""" Yeni Matris:
                        {}    {}    {}    |  {}
                        {}    {}    {}    |  {}
                        {}    {}    {}    |  {}""".format(a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4))


    print("")
    if(b1==0 and c1 ==0 and c2 == 0):
        break
    else:
        pass

x3 = c4/c3
x2 = (b4-(b3*x3))/b2
x1 = (a4-(a3*x3)-(a2*x2))/a1

print("\n")

print("(x1,x2,x3) = ({},{},{})".format(x1,x2,x3))

















