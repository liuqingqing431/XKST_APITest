with open('../dataconfig/1.txt','r') as f:
    c=f.read()
    print('{')
    print('\t"',end='')
    flag=1
    for i in range(len(c)) :
        if c[i]==':'and flag==1:
            print('":"',end='')
            flag=0
        elif c[i]=='\n':
            print('",\n\t"',end='')
            flag=1
        elif c[i]==' 'and c[i-1]==':':
            continue
        else:
             print(c[i],end='')
    print('"')
    print('}')
