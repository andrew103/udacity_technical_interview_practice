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


#============================ QUESTION_2 ======================================

#============================ QUESTION_2 ======================================


#============================ QUESTION_3 ======================================

#============================ QUESTION_3 ======================================


#============================ QUESTION_4 ======================================

#============================ QUESTION_4 ======================================


#============================ QUESTION_5 ======================================

#============================ QUESTION_5 ======================================
