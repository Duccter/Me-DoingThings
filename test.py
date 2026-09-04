# def solution(orders, num):
#     # Please write code here.
#     answer = 0 
    
#     n = len(orders)
#     orders = [[0, 0]] + orders
#     m = num
#     f = [[0] * (m + 1) for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if (j - orders[i][0] >= 0):
#                 f[i][j] = max(f[i-1][j-orders[i][0]] + orders[i][1], f[i-1][j]) 
#             else:
#                 f[i][j] = f[i-1][j]
#             answer = max(f[i][j], answer)
#     for i in f:
#         print(i)
#     return answer


# print(solution([ [ 3, 5 ], [ 4, 7 ] ], 6))



# scores = list(map(int, input().split()))

# print(round(sum(scores) / 4, 1))

# a = int(input())
# b = int(input())

# print(a + b, a - b, a * b, a / b, a % b)


# def solution(cards = [ "8Q2JK3", "J7QK32", "4JQK29", "JK32Q4"]):
#     answer = []
    
#     n = len(cards)
#     for i in range(n):
#         q = cards[i].index("Q")
#         j = cards[i].index("J")
#         k = cards[i].index("K")

#         print(q, j, k)
#         if j < q < k:
#             answer.append(i + 1)

#     return answer

# print(solution())


def separateBirth(birth):
    result = []
    
    year = 1900
    month = int(str(birth)[-3:-5:-1])
    date = int(str(birth)[-1:-3:-1])
    
    result.append(year)
    result.append(month)
    result.append(date)
    
    return result

def solution(birth, gender):
    answer = []
    
    separatedBirth = separateBirth(birth)
    
    if gender < 3:
        answer.append(separatedBirth[0] + (int(str(birth)[0:2]) if len(str(birth)) == 6 else int(str(birth)[0])))
        
    else:
        answer.append(separatedBirth[0] + ((int(str(birth)[0:2]) + 100) if len(str(birth)) == 6 else (int(str(birth)[0]) + 100)))
    
    answer.append(separatedBirth[1])
    answer.append(separatedBirth[2])
    
    return answer


print(solution(951230, 2))