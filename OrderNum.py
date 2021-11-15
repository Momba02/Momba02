def sort_list(liststri):
    val = len(liststri)
    for i in range(0, val):
        temp = i
        for t in range(i, val):
            if(liststri[temp] > liststri[t]):
                arrtemp = liststri[temp]
                liststri[temp] = liststri[t]
                liststri[t]= arrtemp
def find_num(num, array):
    newarray =[]
    num = int(num)
    leng = int(len(array)/2)
    if(leng != 1):
        if(num < array[leng]):
            for i in range(0,leng):
                newarray.append(array[i])
            find_num(num,newarray)
        elif(num > array[leng]):
            for i in range(leng,len(array)):
                newarray.append(array[i])
                find_num(num,newarray)
        elif(num == array[leng]):
            print('the number exists')
    else:
        if(array[0 == num]):
            print('the number exists')
        else:
            print('The number does not exist')
liststri=[]
stri = input("Enter nums if u finish put 'done'")
if(stri != 'done'):
    while(stri != 'done'):
        stri = int(stri)
        liststri.append(stri)
        stri = input("Enter nums if u finish put 'done'")
sort_list(liststri)
num = input('enter number to check in the array')
find_num(num, liststri)

