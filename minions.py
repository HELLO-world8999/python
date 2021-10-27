def check(string,list1):
    count=0
    x=len(list1)
    for i in range(x):
        element=list1[i]
        y=len(element)
        for j in range(len(string)):
            try:
                if element==string[j:j+y]:
                    count+=1
            except IndexError:
                break
    return count       
        

def minion_game(string):
    l=len(string)
    stuart=[]
    kevin=[]
    if l>0 and l<=10**6:
        for i in range(l):
            empty_str=""
            if string[i] not in ("A","E","I","O","U","a","e","i","o","u"):
                for j in range(i,l):
                    empty_str+=string[j]
                    if empty_str not in stuart:
                        stuart.append(empty_str)
            else:
                for j in range(i,l):
                    empty_str+=string[j]
                    if empty_str not in kevin:
                        kevin.append(empty_str)
    x=check(string,stuart)
    y=check(string,kevin)

    if x>y:
        print("Stuart ",x)
    else:
        print("Kevin ",y)

if __name__ == '__main__':
    s = input("Enter you word:")
    minion_game(s)
