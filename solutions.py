import copy

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
    """
    Given a list of palindromes, finds the longest one and returns it
    """
    longest = ""
    for palindrome in pal_list:
        if len(palindrome) > len(longest):
            longest = palindrome

    return longest

def find_palindrome(string, lower, upper):
    """
    Provided the string and starting points, finds the palindrome within the
    string by fanning out from the starting point
    """
    distance = 1
    while string[lower] == string[upper]:
        upper += 1
        lower -= 1
        if upper >= len(string) or lower <= -1:
            break

    return string[lower+1:upper]

def question2(a):
    """
    Takes in a string and returns the longest palindrome found within it
    """
    palindromes = []
    if a:
        # remove all the spaces within the string and convert to lowercase
        # to avoid errors
        a = a.replace(" ", "")
        a = a.lower()
        for pivot in range(len(a)):
            # if a pivot matches a neighboring letter, begin the palindrome
            # finding process
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
G1 = {'A': [('B', 3), ('C', 2), ('D', 4)],
      'B': [('A', 3), ('C', 5), ('D', 7)],
      'C': [('A', 2), ('B', 5), ('D', 1)],
      'D': [('A', 4), ('B', 7), ('C', 1)]}

G2 = {
    'A': [('B', 9),('C', 3),('D', 2)],
    'B': [('A', 9),('C', 8),('H', 9)],
    'C': [('A', 3),('B', 8),('D', 7),('E', 6),('F', 1)],
    'D': [('A', 2),('C', 7),('I', 10)],
    'E': [('C', 6),('G', 3)],
    'F': [('C', 1),('G', 5),('I', 8)],
    'G': [('E', 3),('F', 5)],
    'H': [('B', 9),('I', 4)],
    'I': [('D', 10),('F', 8),('H', 4)]
}
# =========================================================== BEGIN Q3 OLD CODE
# def create_tree(path, graph_in):
#     """
#     Uses the idealized path of visited nodes to construct a new filtered graph
#     """
#     filtered = copy.deepcopy(graph_in)
#     for node in path:
#         for edge in graph_in[node]:
#             # removes all unnecessary edges that aren't part of the ideal path
#             if path.index(node) == 0 and path[path.index(node)+1] != edge[0]:
#                 filtered[node].pop(filtered[node].index(edge))
#             elif path.index(node) == len(path)-1 and path[path.index(node)-1] != edge[0]:
#                 filtered[node].pop(filtered[node].index(edge))
#             elif path[path.index(node)-1] != edge[0] and path[path.index(node)+1] != edge[0]:
#                 filtered[node].pop(filtered[node].index(edge))
#
#     return filtered
#
#
# def lightest_edge(edges, visited):
#     """
#     Provided a list of available edges, returns the lightest, non-visited edge
#     """
#     lightest = None
#     for edge in edges:
#         if (lightest == None or edge[1] < lightest[1]) and (edge[0] not in visited):
#             lightest = edge
#
#     if lightest:
#         return edges.index(lightest)
#
#     return None
#
#
# def question3(graph):
#     """
#     Given a complete undirected graph, finds the ideal path to visit all nodes
#     while maintaining the least possible total weight
#     """
#     if not graph or graph == None:
#         return None
#
#     # duplicates the graph rather than creating a reference to it
#     result = copy.deepcopy(graph)
#     start = list(result.keys())[0]
#
#     visited = []
#     visited.append(start)
#
#     fin_weight = None
#     ideal_visited = []
#
#     while len(result[start]) != 0:
#         if len(visited) == 1:
#             # initializes the search process starting from a "pivot" node
#             edge = result[start][lightest_edge(result[start], visited)]
#             prev_node = start
#             cur_node = edge[0]
#             visited.append(cur_node)
#             cur_weight = edge[1]
#         elif len(visited) == len(result):
#             # when all nodes in the graph have been visited, check if an ideal
#             # path was created then reset for another run
#             if fin_weight == None or cur_weight < fin_weight:
#                 fin_weight = cur_weight
#                 ideal_visited = visited
#
#             result[prev_node].pop(result[prev_node].index(edge))
#             visited = []
#             visited.append(start)
#         else:
#             if lightest_edge(result[cur_node], visited) != None:
#                 # a non-visited node is found so record it and continue along
#                 # this path
#                 edge = result[cur_node][lightest_edge(result[cur_node], visited)]
#                 prev_node = cur_node
#                 cur_node = edge[0]
#                 visited.append(cur_node)
#                 cur_weight += edge[1]
#             else:
#                 # this path doesn't visit all nodes so reset and start a new
#                 # path to test
#                 result[prev_node].pop(result[prev_node].index(edge))
#                 result[cur_node] = copy.deepcopy(graph[cur_node])
#
#                 visited = []
#                 visited.append(start)
#
#     return create_tree(ideal_visited, graph)
# ===========================================================END Q3 OLD CODE
def create_edge_list(graph):
    pass


def convert_to_graph(edge_list):
    pass


def question3(graph):
    pass


print(question3(G1))
# Expected result: {
# 'A': [('B', 3)],
# 'B': [('A', 3), ('C', 5)],
# 'C': [('B', 5), ('D', 1)],
# 'D': [('C', 1)]
# }
print(question3({}))
# Expected result: None
print(question3(G2))
# Expected result: {
# 'A': [('D', 2)],
# 'B': [('C', 8), ('H', 9)],
# 'C': [('B', 8), ('F', 1)],
# 'D': [('A', 2), ('I', 10)],
# 'E': [('G', 3)],
# 'F': [('C', 1), ('G', 5)],
# 'G': [('E', 3), ('F', 5)],
# 'H': [('B', 9), ('I', 4)],
# 'I': [('D', 10), ('H', 4)]
# }
#============================ END QUESTION_3 ======================================
print("")
print("================= QUESTION 4 =================")
#============================ BEGIN QUESTION_4 ======================================
matrix_1 = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

matrix_2 = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
]

class Node(object):
    """
    Node instance that defines a value and children nodes for a specific node
    object
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree(matrix):
    """
    Takes a given matrix and builds a tree with Node objects. Returns a list of
    those nodes
    """
    node_list = []
    node_index = 0
    for node in matrix:
        # create a Node object for each entry in the matrix
        cur_node = Node(node_index)
        node_list.append(cur_node)
        child_index = 0
        # check to see if each entry has children. if so, then add the data to
        # the corresponding Node object
        for child in node:
            if child == 1:
                if child_index <= node_index:
                    cur_node.left = child_index
                elif child_index > node_index:
                    cur_node.right = child_index

            child_index += 1
        node_index += 1

    return node_list


def find_orphans(nodes):
    """
    Takes in a list of Node objects and finds if there are any orphan nodes.
    Orphans are defined as not having any parent nodes and are not the root
    node.
    """
    children = []
    orphan_list = []
    # if the node isn't an orphan, append its value to children
    for node in nodes:
        if node.left != None or node.right != None:
            children.append(node.left)
            children.append(node.right)
            children.append(node.data)

    # find which node values don't exist in children and append them to
    # orphan_list
    for node in nodes:
        if node.data not in children:
            orphan_list.append(node.data)

    return orphan_list


def question4(T, r, n1, n2):
    """
    Takes in a matrix, root value, and two endpoints in order to find the least
    common ancestor between those two endpoints
    """
    if not (T or r or n1 or n2):
        return None
    elif n1 < 0 or n1 >= len(T) or n2 < 0 or n2 >= len(T):
        return None
    elif n1 == n2:
        return n1

    # create the tree and find any orphans that may exist
    nodes = create_tree(T)
    orphans = find_orphans(nodes)

    if n1 in orphans or n2 in orphans:
        return None

    cur_node = r

    # traverse the tree to find the least common ancestor of the endpoints
    while (cur_node <= n1 and cur_node <= n2) or (cur_node > n1 and cur_node > n2):
        if cur_node == None or (cur_node in orphans):
            return None
        elif cur_node == n1 or cur_node == n2:
            return cur_node
        elif cur_node <= n1 and cur_node <= n2:
            cur_node = nodes[cur_node].right
        elif cur_node > n1 and cur_node > n2:
            cur_node = nodes[cur_node].left

    return cur_node


print(question4(matrix_1, 3, 1, 4))
# Expected result: 3
print(question4(matrix_1, 3, 2, 4))
# Expected result: None
print(question4(matrix_1, 3, 0, 1))
# Expected result: 0
print(question4(matrix_1, 3, 1, 1))
# Expected result: 1
print(question4(matrix_2, 6, 0, 3))
# Expected result: 2
#============================ END QUESTION_4 ======================================
print("")
print("================= QUESTION 5 =================")
#============================ BEGIN QUESTION_5 ======================================
class Node(object):
    """
    Node instance that provides a value and a pointer to the next Node object
    in a series.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


def populate_linked(main_list):
    """
    Helper function to create the linked list for use in the main function
    """
    linked = []
    for value in main_list:
        node = Node(value)
        linked.append(node)

    for node in linked:
        if linked.index(node) != len(linked)-1:
            node.next = linked[linked.index(node)+1]

    return linked

main_list = [8,25,45,69,2,1,8,6,2,36,45]
linked_list = populate_linked(main_list)
root = linked_list[0]

def question5(ll, m):
    """
    Creates an ordered list of values taken from the linked list, then indexes
    that list in order to find the desired value and return it.
    """
    if ll == None or m > len(linked_list):
        return None

    ordered_list = []
    cur_node = ll
    # traverses the linked list to create an ordered list of values
    while True:
        ordered_list.append(cur_node.data)
        if cur_node.next == None:
            break
        else:
            cur_node = cur_node.next

    return ordered_list[-m]

print(question5(root, 6))
# Expected Value: 1
print(question5(None, 6))
# Expected Value: None
print(question5(root, 11))
# Expected Value: 8
print(question5(root, 312))
# Expected Value: None
#============================ END QUESTION_5 ======================================
