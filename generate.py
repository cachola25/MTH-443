
# letters = ['N', 'O', 'N', 'Y', 'A', 'C']

# # Generate all permutations of the list
# def permute(arr, l, r):
    
#     if l == r:
#         print(''.join(arr))
#     else:
#         for i in range(l, r + 1):
#             arr[l], arr[i] = arr[i], arr[l]
#             permute(arr, l + 1, r)
#             arr[l], arr[i] = arr[i], arr[l]
# permute(letters, 0, len(letters) - 1)

def findWords(words,str):
    lst = []
    for word in words:
        i = 0
        while len(str[i:i+len(word)]) == len(word):
            if (str[i:i+len(word)] == word):
                lst.append(i)
            i+=1
    if len(lst) == 0:
        return  []
    lst.sort()
    return lst

print(findWords(["MCD","QFD"],"CMNAMNCOJGNANSMCNMMCDMPAMQDFFQFDMCPDLFNQMDCMCDQDFAKHFD"))