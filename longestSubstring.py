
# s = "abcabcbb"

s = "pwwkew"

# def lengthOfLongestSubstring(str):
#     stringKing = ""
#     whoIsTheKing2 = ""
#     result = ""
#     latItem2 = ""
#     for item in str:
#         stringKing += item
#         print(f"here it king1 {stringKing}")
#         for item2 in str:
#             whoIsTheKing2 += item2
#             print(f"here it king2 {whoIsTheKing2}")
#             if stringKing == whoIsTheKing2 :
#                 result = stringKing
#                 print(result)
#                 break;
#         whoIsTheKing2 = ""
#     print(result)
    
# lengthOfLongestSubstring(s)



def lengthOfLongestSubstring(str):
    
    def check(start, end):
            chars = [0] * 128
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True
    n = len(s)

    res = 0
    for i in range(n):
        for j in range(i, n):
            if check(i, j):
                res = max(res, j - i + 1)
    return res


print(lengthOfLongestSubstring(s))