n=int(input())

chessboard=[[0 for _ in range(n)] for _ in range(n)]
count=0

def check(index,n):#행 열
    if index==n:
        global count
        count+=1
        return
    #같은열에 퀸이 있는지 확인
    for i in range(n):#열 바꿔가면서 확인
        checkdd=1
        for j in range(index):
            if chessboard[j][i]==1:
                checkdd=0
                break
        #좌 상단 대각선에 퀸이 있는지 확인
        if checkdd==1:
            leftrow=index#행
            leftcol=i#열
            while leftrow>=0 and leftcol>=0:
                if chessboard[leftrow][leftcol]==1:
                    checkdd = 0
                    break
                leftrow -= 1
                leftcol-=1


        #우 상단 대각선에 퀸이 있는지 확인
        if checkdd == 1:
            rightrow=index
            rightcol=i
            while rightrow>=0 and rightcol<n:
                if chessboard[rightrow][rightcol]==1:
                    checkdd = 0
                    break
                rightrow-=1
                rightcol+=1

        if checkdd==0:
            continue
        chessboard[index][i] = 1
        check(index+1,n)#다음행에서 실행
        chessboard[index][i] = 0



check(0,n)#0줄부터 시작
print(count)
