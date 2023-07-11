##############
# Homework 2 #
##############

##############
# Question 1 #
##############

# BFS takes in a tuple that represents a tree and returns a tuple of the nodes in BFS visiting order
def BFS(FRINGE):
    if (len(FRINGE) == 1 and type(FRINGE[0]) != tuple): # when passed a single non-tuple, return it as a tuple
        return((FRINGE[0]),)
    elif (len(FRINGE) == 1 and type(FRINGE[0]) == tuple): # when passed a single tuple, unpack tuple starting at first element
        return(BFS(FRINGE[0]))
    elif (type(FRINGE[0]) == tuple): # if nested tuples, recurse on the next element on the same level; move tuple to the back of "queue"
        return(BFS(FRINGE[1:] + FRINGE[0]))
    else:
        return((FRINGE[0],) + BFS(FRINGE[1:])) # if first element on level is a non-tuple, consider it "visited" and continue to investigate next elements on the same level

# print(BFS(("ROOT",)))
# print(BFS((((("L", "E"), "F"), "T"))))
# print(BFS((("R", ("I", ("G", ("H", "T")))))))
# print(BFS(((("A", ("B",)), "C", ("D",)))))
# print(BFS((("T", ("H", "R", "E"), "E"))))
# print(BFS((("A", (("C", (("E",), "D")), "B"))))) 

##############
# Question 2 #
##############

# These functions implement a depth-first solver for the homer-baby-dog-poison
# problem. In this implementation, a state is represented by a single tuple
# (homer, baby, dog, poison), where each variable is True if the respective entity is
# on the west side of the river, and False if it is on the east side.
# Thus, the initial state for this problem is (False False False False) (everybody
# is on the east side) and the goal state is (True True True True).

# The main entry point for this solver is the function DFS, which is called
# with (a) the state to search from and (b) the path to this state. It returns
# the complete path from the initial state to the goal state: this path is a
# list of intermediate problem states. The first element of the path is the
# initial state and the last element is the goal state. Each intermediate state
# is the state that results from applying the appropriate operator to the
# preceding state. If there is no solution, DFS returns [].
# To call DFS to solve the original problem, one would call
# DFS((False, False, False, False), [])
# However, it should be possible to call DFS with a different initial
# state or with an initial path.

# First, we define the helper functions of DFS.

# FINAL-STATE takes a single argument S, the current state, and returns True if it
# is the goal state (True, True, True, True) and False otherwise.
def FINAL_STATE(S):
    if (S == (True, True, True, True)): # return true if passed in state is goal state (True, True, True)
        return True
    else:
        return False #otherwise return false

# NEXT-STATE returns the state that results from applying an operator to the
# current state. It takes three arguments: the current state (S), and which entity
# to move (A, equal to "h" for homer only, "b" for homer with baby, "d" for homer
# with dog, and "p" for homer with poison).
# It returns a list containing the state that results from that move.
# If applying this operator results in an invalid state (because the dog and baby,
# or poisoin and baby are left unsupervised on one side of the river), or when the
# action is impossible (homer is not on the same side as the entity) it returns [].
# NOTE that next-state returns a list containing the successor state (which is
# itself a tuple)# the return should look something like [(False, False, True, True)].
def NEXT_STATE(S, A):
    if (A == "h"): # homer only
        x = not S[0]
        new_tup = (x,) + S[1:]
        if ((new_tup[1] == new_tup[2]) and new_tup[1] != new_tup[0]): # (unsupervised) homer is on other side with dog and baby together on other side
            return []
        elif ((new_tup[1] == new_tup[3]) and new_tup[1] != new_tup[0]): # (unsupervised) homer is on other side with baby and poison together on other side
            return []
        else:
            return([new_tup])
    elif (A == "b"): # homer w/ baby
        x = not S[0]
        y = not S[1]
        new_tup = (x, y) + S[2:]
        if ((new_tup[1] == new_tup[2]) and new_tup[1] != new_tup[0]): # (unsupervised) homer is on other side with dog and baby together on other side
            return []
        elif ((new_tup[1] == new_tup[3]) and new_tup[1] != new_tup[0]): # (unsupervised) homer is on other side with baby and poison together on other side
            return []
        elif (new_tup[0] != new_tup[1]): # (impossible) homer isn't on same side with entity
            return []
        else:
            return([new_tup])
    elif (A == "d"): # homer w/ dog
        x = not S[0]
        y = not S[2]
        new_tup = (x, S[1], y, S[3])
        if ((new_tup[1] == new_tup[2]) and new_tup[1] != new_tup[0]): # (unsupervised) homer is on other side with dog and baby together on other side
            return []
        elif ((new_tup[1] == new_tup[3]) and new_tup[1] != new_tup[0]): # (unsupervised) homer is on other side with baby and poison together on other side
            return []
        elif (new_tup[0] != new_tup[2]): # (impossible) homer isn't on same side with entity
            return []
        else:
            return([new_tup])
    elif (A == "p"): # homer w/ poison
        x = not S[0]
        y = not S[3]
        new_tup = (x, S[1], S[2], y)
        if ((new_tup[1] == new_tup[2]) and new_tup[1] != new_tup[0]): # (unsupervised) homer is on other side with dog and baby together on other side
            return []
        elif ((new_tup[1] == new_tup[3]) and new_tup[1] != new_tup[0]): # (unsupervised) homer is on other side with baby and poison together on other side
            return []
        elif (new_tup[0] != new_tup[3]): # (impossible) homer isn't on same side with entity
            return []
        else:
            return([new_tup])
    else:
        return []

# SUCC-FN returns all of the possible legal successor states to the current
# state. It takes a single argument (s), which encodes the current state, and
# returns a list of each state that can be reached by applying legal operators
# to the current state.
def SUCC_FN(S): # checks state against all operators and adds to list if not invalid []
    legal_list = []
    if (NEXT_STATE(S, "h") != []):
        legal_list = legal_list + NEXT_STATE(S, "h")
    if (NEXT_STATE(S, "b") != []):
        legal_list = legal_list + NEXT_STATE(S, "b")
    if (NEXT_STATE(S, "d") != []):
        legal_list = legal_list + NEXT_STATE(S, "d")
    if (NEXT_STATE(S, "p") != []):
        legal_list = legal_list + NEXT_STATE(S, "p")
    return legal_list

# ON-PATH checks whether the current state is on the stack of states visited by
# this depth-first search. It takes two arguments: the current state (S) and the
# stack of states visited by DFS (STATES). It returns True if s is a member of
# states and False otherwise.
def ON_PATH(S, STATES):
    for i in STATES: # check current state against each state in the PATH to see if we've seen this step before
        if (S == i):
            return True
    else:
        return False

# MULT-DFS is a helper function for DFS. It takes two arguments: a list of
# states from the initial state to the current state (PATH), and the legal
# successor states to the last, current state in the PATH (STATES). PATH is a
# first-in first-out list of states# that is, the first element is the initial
# state for the current search and the last element is the most recent state
# explored. MULT-DFS does a depth-first search on each element of STATES in
# turn. If any of those searches reaches the final state, MULT-DFS returns the
# complete path from the initial state to the goal state. Otherwise, it returns
# [].
def MULT_DFS(STATES, PATH):
    for i in STATES: # checks for every legal successor
        if (DFS(i, PATH) == []): # continue to other legal successors if current successor has been seen in PATH before (logic in DFS)
            continue
        else:
            return(DFS(i, PATH))

# DFS does a depth first search from a given state to the goal state. It
# takes two arguments: a state (S) and the path from the initial state to S
# (PATH). If S is the initial state in our search, PATH is set to [] (empty list). DFS
# performs a depth-first search starting at the given state. It returns the path
# from the initial state to the goal state, if any, or empty list [] otherwise. DFS is
# responsible for checking if S is already the goal state, as well as for
# ensuring that the depth-first search does not revisit a node already on the
# search path.
def DFS(S, PATH):
    if (S == (True, True, True, True)):
        return(PATH + [S])
    if (ON_PATH(S, PATH) == True): # return [] if inputted state has been seen in PATH before (b/c redundant to redo the path again)
        return []
    else:
        return(MULT_DFS(SUCC_FN(S), PATH + [S])) # if not an already visited state add to PATH, recurse on all its successor states

# S = ((False, False, False, False))
# PATH = []
# print(DFS(S, PATH))
