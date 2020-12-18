brackets = '())(())(())('
print(len(brackets))
print(brackets)
requests = int(input('Please input the amount of requests: '))


left_and_right = []

# i = 0
# while i < requests:
#     l_r = list(map(int, input().split()))
#     left_and_right.append(l_r)
#     i += 1
# print(left_and_right)

count = 0
count_l = 0
count_r = 0
# for j in range(len(left_and_right)):
for k in range(0,3):
    if brackets[k] == '(':
        count += 1
    else:
        count -= 1
print(count)
# for k in range(0,12):
#     print(brackets[k])
#     if brackets[k] == '(':
#         count_l += 1
#         if brackets[k] == ')':
#             count_r += 1
#
#     if count_l > count_r:
#         count = count_l - count_r
#         count_l = count + count_r
#     elif count_l < count_r:
#         count = count_r - count_l
#         count_r = count + count_r
#     else:
#         count = count_r + count_l
# print(count)