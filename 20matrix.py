def matrix(n):
    mat=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        mat.append(l)

    for i in range(n):

        for j in range(n):
            print(mat[i][j],end=" ")
        print()


def matrix2(n):
    #loops inside list
    mat=[0 for i in range(n)]
    print(mat)
    mat=[[0 for i in range(n)] for j in range(n+1)]
    print(mat)


matrix(3)
matrix2(3)