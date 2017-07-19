print("================= QUESTION 1 =================")
#============================ QUESTION_1 ======================================
def question1(s, t):
    """
    Takes in two strings, s and t, and compares to see if t is a substring of s
    """
    if s and t:
        # convert strings to lists of letters
        main = [letter for letter in s.lower()]
        anagram = [letter for letter in t.lower()]
        # if all letters popped out of t, the anagram is a substring
        while len(anagram) > 0:
            if anagram[0] in main:
                # for each matching letter, pop that letter out of both strings
                main.pop(main.index(anagram[0]))
                anagram.pop(0)
            else:
                return False

        return True
    return False


print(question1("udacity", "ad"))
# Expected result: True
print(question1("", ""))
# Expected result: False
print(question1("mississippi", "misses"))
# Expected result: False
print(question1("people", "PEPE"))
# Expected result: True
#============================ QUESTION_1 ======================================
print("")
print("================= QUESTION 2 =================")
#============================ QUESTION_2 ======================================
def longest_palindrome(pal_list):
    longest = ""
    for palindrome in pal_list:
        if len(palindrome) > len(longest):
            longest = palindrome

    return longest

def find_palindrome(string, lower, upper):
    distance = 1
    while string[lower] == string[upper]:
        upper += 1
        lower -= 1
        if upper >= len(string) or lower <= -1:
            break;

    return string[lower+1:upper]

def question2(a):
    palindromes = []
    if a:
        a = a.replace(" ", "")
        a = a.lower()
        for pivot in range(len(a)):
            try:
                if a[pivot - 1] == a[pivot + 1]:
                    palindromes.append(find_palindrome(a, pivot, pivot))
                elif a[pivot] == a[pivot + 1]:
                    palindromes.append(find_palindrome(a, pivot, pivot + 1))
            except IndexError:
                pass

        return longest_palindrome(palindromes)
    return None


print(question2("asd;flaoeuigvn;alsdknc;MadamiugsadflRepaperjahfvvfeMome"))
# Expected result: repaper
print(question2("MadamRotorRedderfMy gymRacecar"))
# Expected result: racecar
print(question2(""))
# Expected result: None
print(question2("Step on no petsSagasRepaper"))
# Expected result: steponnopets
#============================ QUESTION_2 ======================================
print("")
print("================= QUESTION 3 =================")
#============================ QUESTION_3 ======================================

#============================ QUESTION_3 ======================================
print("")
print("================= QUESTION 4 =================")
#============================ QUESTION_4 ======================================

#============================ QUESTION_4 ======================================
print("")
print("================= QUESTION 5 =================")
#============================ QUESTION_5 ======================================

#============================ QUESTION_5 ======================================
