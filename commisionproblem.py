def commissionp():
    lprice=45
    sprice=30
    bprice=25
    tstocks=0
    tlocks=0
    tbarrels=0
    locks=int(input("enter the numer of locks to exit the loop enter -1\n")) 
    while(locks!=-1):
        c1=(locks >= 0 and locks <= 70)
        stock=int(input("enter the value of number of stocks\n"))
        barrel=int(input("enter the number of barrels\n"))
        c2=(stock>=0 and stock<=80)
        c3=(barrel>=0 and barrel<=90)
        if c1:
            tlocks=locks
            
        else:
            print("invalid locks entry")
            break
        if c2:
            tstocks=stock
        else:
            print("invalid stock entry")
            break
        if c3:
            tbarrels=barrel
        else:
            print("invalid barrel entry")
            break
        sales=(tlocks*lprice)+(tstocks*sprice)+(tbarrels*bprice)
        print("total sales is = ",sales)
        if sales>1800:
            comm=((sales-1800)*0.20)+(1000*0.1)+(800*0.15)
            print("total commission is equal to = ",comm)
            break
        elif sales>1000:
            comm=(1000*0.1)+((sales-1000)*0.15)
            print("total commission is equal to = ",comm)
            break

        else:
            comm=sales*0.1
            print("total commission is equal to = ",comm)
            break


            

commissionp()