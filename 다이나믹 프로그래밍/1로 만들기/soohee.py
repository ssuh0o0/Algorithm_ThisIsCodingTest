arr = [0,0,1] + [0] * 30

def makeOne(x):
    if x == 1:
        return 1

    if arr[x] != 0:
        return arr[x]
    
    if x % 5 == 0 :
        arr[x] = min( makeOne( x // 5 ) , arr[ x - 1 ] ) + 1
    elif x % 3 == 0 :
        arr[x] = min( makeOne( x // 3 ) , arr[ x - 1 ] ) + 1
    elif x % 2 == 0 :
        arr[x] = min( makeOne( x // 2 ) , arr[ x - 1 ] ) + 1
 
    return arr[x]

# def makeOne(x):
    
#     for i in range(2,x+1):
#         if x % 5 == 0 :
#             arr[i] = min( makeOne( i // 5 ) , makeOne( i - 1 ) ) + 1
#         elif x % 3 == 0 :
#             arr[i] = min( makeOne( i // 3 ) , makeOne( i - 1 ) ) + 1
#         elif x % 2 == 0 :
#             arr[i] = min( makeOne( i // 2 ) , makeOne( i - 1 ) ) + 1
 
#     return arr[x]

print(makeOne(26))