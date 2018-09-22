def compare(mylist,tosearch,low,high):
   
    middle = low + int((high-low)/2)
    
    if tosearch == mylist[middle]:
            return middle

    elif tosearch < mylist[middle]:
        return compare(mylist,tosearch,low,middle)
    
    elif tosearch > mylist[middle]:
        return compare(mylist,tosearch,middle,high)


if __name__ == "__main__":
  
    mylist = [int(x) for x in input().split()]
    print(mylist)
    tosearch = int(input())
    print(tosearch)
    ind = compare(mylist,tosearch,0,len(mylist)-1)
    print(ind)
