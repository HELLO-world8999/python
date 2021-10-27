def minion_game(string):
    stuart=[]
    kevin=[]
    for i in range(len(string)):
        if string[i] not in ("A","E","I","O","U"):
            for j in range(i,len(string)):
                s=string[i:j+1]
                stuart.append(s)
        else:
            for x in range(i,len(string)):
                s=string[i:x+1]
                kevin.append(s)
    x=len(stuart)
    y=len(kevin)
    if x>y:
        print("Stuart",x)
    elif y>x:
        print("Kevin",y)
    else:
        print("Draw")

if __name__ == '__main__':
    s=input("Enter the string:") #######
    minion_game(s)
