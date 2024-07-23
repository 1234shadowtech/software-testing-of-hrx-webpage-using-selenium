def bisrc(a,low,high,key):
    while(low<=high):
        mid=(low+high)//2
        if(key==a[mid]):
            return mid
        elif(key<a[mid]):
            high=mid-1
        else:
            low=mid+1
    return -1

def main():
    list=[]
    n=int(input("enter the number of elements in the list\n"))
    for i in range(n):
        element=int(input("enter the element\n"))
        list.append(element)
    key=int(input("enter the key element to be searched\n"))
    print(list[0])
    print(list[n-1])
    yes=bisrc(list,list[0],list[n-1],key)
    if (yes>=0):
        print("the key is found in pos =",yes)
    else:
        print("the key is not found")
main()





