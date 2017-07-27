print("================= QUESTION 1 =================")
#============================ BEGIN QUESTION_1 ======================================
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
#============================ END QUESTION_1 ======================================
print("")
print("================= QUESTION 2 =================")
#============================ BEGIN QUESTION_2 ======================================
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
#============================ END QUESTION_2 ======================================
print("")
print("================= QUESTION 3 =================")
#============================ BEGIN QUESTION_3 ======================================
G = {'A': [('B', 3), ('C', 2), ('D', 4)],
     'B': [('A', 3), ('C', 5), ('D', 7)],
     'C': [('A', 2), ('B', 5), ('D', 1)],
     'D': [('A', 4), ('B', 7), ('C', 1)]}

def create_tree(path, graph_in):
    filtered = graph_in
    for node in path:
        for edge in filtered[node]:
            

    return filtered


def lightest_edge(edges):
    lightest = None
    for edge in edges:
        if (lightest == None or edge[1] < lightest[1]) and (edge[0] not in visited):
            lightest = edge

    return edges.index(lightest)


def question3(graph):
    result = graph
    start = result[0]

    visited = []
    visited.append(start)

    fin_weight = None
    ideal_visited = []

    while len(result[start]) != 0 and len(visited) == len(result):
        if len(visited) == 1:
            edge = result[start][lightest_edge(result[start], visited)]
            cur_node = edge[0]
            visited.append(cur_node)
            cur_weight = edge[1]
        elif len(visited) == len(result):
            if fin_weight == None or cur_weight < fin_weight:
                fin_weight = cur_weight
                ideal_visited = visited

            result[prev_node].pop(index(edge))
            visited = []
            visited.append(start)
        else:
            if lightest_edge(result[cur_node], visited) != None:
                edge = result[cur_node][lightest_edge(result[cur_node], visited)]
                prev_node = cur_node
                cur_node = edge[0]
                visited.append(cur_node)
                cur_weight += edge[1]
            else:
                result[prev_node].pop(index(edge))
                result[cur_node] = graph[cur_node]

                visited = []
                visited.append(start)

    return create_tree(ideal_visited, graph)

# print(question3(G))
#============================ END QUESTION_3 ======================================
print("")
print("================= QUESTION 4 =================")
#============================ BEGIN QUESTION_4 ======================================

#============================ END QUESTION_4 ======================================
print("")
print("================= QUESTION 5 =================")
#============================ BEGIN QUESTION_5 ======================================
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def question5(root, m):
    pass
#============================ END QUESTION_5 ======================================
