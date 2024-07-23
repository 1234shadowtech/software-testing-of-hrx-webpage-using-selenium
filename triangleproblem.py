def triangle():
    s1=int(input("enter the first side of the triangle\n"))
    s2=int(input("enter the second side of the triangle\n"))
    s3=int(input("enter the third side of the triangle\n"))
    c1=s1>=0 and s1<=10
    c2=s2>=0 and s2<=10
    c3=s3>=0 and s3<=10
    if (c1 and c2 and c3):
        if (s1<s2+s3 and s2<s1+s3 and s3<s1+s2):
            if (s1==s2 and s2==s3 ):
                print("it is a equilateral triangle")
            elif(s1!=s2 and s2!=s3 and s1!=s3):
                print("it is a scalen triangle")
            else:
                print("isoseles triangle")
        else:
            print("it is not a triangle")
    else:
        print("incorrect entry")

triangle()