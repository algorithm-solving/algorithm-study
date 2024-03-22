N, A = map(int, input().split())
arr = []
for _ in range(N):
    type, atk, hp = map(int, input().split())
    arr.append((type, atk, hp))


def can_clear(curATK, maxHP):
    curHP = maxHP
    # 모든 방 탐색
    for type, atk, hp in arr:
        # 몬스터
        if type == 1:
            turn = hp//curATK if not hp % curATK else hp//curATK+1
            # 용사가 먼저 공격하므로 -1
            curHP -= atk * (turn-1)
        # 물약
        else:
            curATK += atk
            curHP += hp
            # 최대 회복은 maxHP까지만
            if curHP > maxHP:
                curHP = maxHP
        # 용사의 HP가 0이하라면 클리어 불가능
        if curHP <= 0:
            return False
    return True


result = 0
start, end = 1, N*int(1e6)*int(1e6)
while start <= end:
    mid = (start+end)//2
    if can_clear(A, mid):
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)