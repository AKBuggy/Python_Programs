# inp = input("Enter your word: ")
# print(type(inp[::-1]))
#
# if inp == inp[::-1]:
#     print("Its a palindrome")
# else:
#     print("Its not a palindrome")
#
#
# def reverse_string(inp):
#     str1 = ""   # Declaring empty string to store the reversed string
#     for i in inp:
#         str1 = i + str1
#         print(str1)
#     return str1    # It will return the reverse string to the caller function
#
#
# reverse_string(inp)


# func = lambda a, b: (a ** b)
# print(func(float(10), 20))

# my_list = [2, 3, 5, 7, 11]
# squared_list = [x ** 2 for x in my_list]  # list comprehension
# print(squared_list)
# # output => [4 , 9 , 25 , 49 , 121]
# squared_dict = {x: x ** 2 for x in my_list}  # dict comprehension
# print(squared_dict)

# output => {2: 4, 3: 9 , 5: 25 , 7: 49, 11: 121}

# def add_nums(num1, num2):
#     while num2 != 0:
#         data = num1 & num2
#         num1 = num1 ^ num2
#         num2 = data << 1
#     return num1
#
#
# print(add_nums(2, 10))

# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)
#
# mylist = list(set(mylist))
# print(mylist)


# import myModule as nameVar
# from myModule import *
# # nameVar.greet("Ankit Prakash")
# # print(nameVar.greet.__doc__)
# greet("Ankit Prakash")
# sayGoodbye("Ankit Prakash")


# a = 5
# print(a)
# print(a*2)
# print((a*2)-1)

# print('How many potatoes does it take to kill an irish farmer')
# input('Press Enter')
# print('None')

# declaring string variables
# str1 = 'Understanding'
# str2 = '%s'
# str3 = 'at'
# str4 = 'GeeksforGeeks'
#
# # concatenating strings
# final_str = "%s %s %s %s" % (str1, str2, str3, str4)

# printing the final string
# print("Concatenating multiple strings using Python '%s' operator:")
# print(final_str)
#
# dec1 = 5.6
# dec2 = 6.7
#
# final_dec = "%d %d" % (dec1, dec2)
#
# print("Concatenating multiple decimal values using '%d' operator:")
# print(final_dec)

# txt = "For only {price:.2f} dollars!".format(price=60)
# # print(txt.format(price=49))
# print(txt)
#
# txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
# txt2 = "My name is {0}, I'm {1}".format("John", 36)
# txt3 = "My name is {}, I'm {}".format("John", 36)
#
# print(txt1)
# print(txt2)
# print(txt3)

# class SelectionCriteria:
#     CGPA_9 = [0.9, 0.8, 0.97, 0.75, 0.6, 0.4, 0.2, 1.0, 0.0, 0.35]
#     HSC_80 = [0.87, 0.75, 0.63, 0.19, 0.90, 0.40, 0.97, 0.1, 1.0, 0.0]
#     SSC_85 = [0.54, 0.79, 0.68, 0.54, 0.78, 0.32, 0.91, 0.65, 0.20, 0.83]
#
#     # Question no.1
#     minValueQ1 = list(map(min, zip(CGPA_9, HSC_80)))
#     ans = []
#     for i in minValueQ1:
#         if i > 0.5:
#             ans.append(i)
#
#     # Question no.2
#     notSSC_85 = []
#     for j in range(len(SSC_85)):
#         res = 1 - SSC_85[j]
#         notSSC_85.append(round(res, 2))
#
#     minValueQ2 = list(map(min, zip(CGPA_9, notSSC_85)))
#     res1 = []
#     for k in minValueQ2:
#         if k > 0.3:
#             res1.append(k)
#
#     # Question no.3
#     ssc_85_or_hsc_80 = list(map(max, zip(SSC_85, HSC_80)))
#     minValueQ3 = list(map(min, zip(CGPA_9, ssc_85_or_hsc_80)))
#     res2 = []
#     for j in minValueQ3:
#         if j > 0.6:
#             res2.append(j)
#
#
# if __name__ == '__main__':
#     SC = SelectionCriteria()
#     print(SC.ans)
#     print(SC.res1)
#     print(SC.res2)
#
# import random
# """
# 1> Create simple chatbot
# 2> Explore Neural Network free tools
#
# Algorithm
# 1> Create Greetings and goodbyes the chatbot
# 2> Create keywords that the chat will know
# 3> import the random module
# 4> Begin chatting by greeting the user
#
# """
#
# # Creating greetings list
# greetings = ["hi", "Hello", "What's up?!", "Howz you?", "Greetings!"]
#
# # Creating goodbye list
# goodbye = ["Bye!", "Goodbye!", "See you later!", "See you soon!"]
#
# keywords = ["up to", "ai", "ecc", "placements"]
#
# response = ["preparing for entrance exams!", "AI is so exciting!", "ECC is so difficult", "Placements are coming soon!"]
#
# print(random.choice(greetings))
#
# user_response = ""
#
# while user_response != "bye":
#     user_response = input("Go ahead type something (or type bye to quit): ")
#     user_response = user_response.lower().strip()
#     if user_response == "bye":
#         print(random.choice(goodbye))
#         break
#     is_key_found = False
#
#     for index in range(len(keywords)):
#         if keywords[index] in user_response:
#             print("Rusty_The_Bot: ", response[index])
#             is_key_found = True
#         else:
#             continue
#
#     if not is_key_found:
#         print("I am new to your world,I love learning new things!")
#         keywords.append(user_response)
#         # print(keywords)
#         new_response = input("Tell me the correct response to " + user_response + " ? ")
#         print("thank you for teaching me!!")
#         response.append(new_response)
#         # print(response)

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         a = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         sum = 0
#         x = 0
#         while x < len(s):
#             if x < len(s) - 1 and a[s[x]] < a[s[x + 1]]:
#                 sum += (a[s[x + 1]] - a[s[x]])
#                 print("inside if", a[s[x]])
#                 x += 2
#             else:
#                 sum += a[s[x]]
#                 print("inside else", a[s[x]])
#                 x += 1
#         return sum
#
#
# if __name__ == '__main__':
#     sol = Solution()
#     res = sol.romanToInt("XIV")
#     print(res)

# value = 101
# str_value = str(value)
# # print(type(str_value))
# if str_value == str_value[::-1]:
#     print("p")
# else:
#     print("np")
#
# print(str_value)

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # Driver code to test above
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
res = bubbleSort(arr)
print(res)
