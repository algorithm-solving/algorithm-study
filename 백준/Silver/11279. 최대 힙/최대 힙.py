import sys
input = sys.stdin.readline

# insert


def insert(heap, num):
    heap.append(num)

    i = len(heap) - 1
    while i > 1:
        if heap[i] > heap[i//2]:
            tmp = heap[i]
            heap[i] = heap[i//2]
            heap[i//2] = tmp
            i = i // 2
        else:
            break
# remove


def remove(heap):
    max_val = heap[1]
    tmp = heap.pop()

    parent = 1
    child = 2
    while child <= len(heap)-1:
        if child < len(heap)-1 and heap[child] < heap[child+1]:
            child += 1
        if heap[child] <= tmp:
            break

        heap[parent] = heap[child]

        parent = child
        child *= 2

    if len(heap) != 1:
        heap[parent] = tmp
    return max_val

# main


n = int(input())
heap = [0]
for _ in range(n):
    num = int(input())

    if num == 0:
        if len(heap) == 1:
            print(0)
        else:
            print(remove(heap))
    else:
        insert(heap, num)

# import heapq
# from sys import stdin

# n = int(stdin.readline())
# heap = []

# for _ in range(n):
#     num = int(stdin.readline())

#     if num == 0:
#         if heap:
#             print(heapq.heappop(heap)[1])
#         else:
#             print(0)
#     else:
#         heapq.heappush(heap, [-num, num])
