# PAD is a recursive function that takes in one argument, n, that represents the Nth 
# index and returns the Nth term of the Padovan sequence.
def PAD(n):
  if (n == 0 or n == 1 or n == 2): # Base Case checks for n = 1, 2, or 3 b/c given PAD(0) = PAD(1) = PAD(2) = 1.
    return 1
  else: # Recursive Case calculates PAD(n-1) + PAD(n-2)
    x = n - 1 # To fit Padovan Sequence formula
    return(PAD(x-1)+PAD(x-2)) 


# SUMS is a recursive function that takes in one argument, n, that represents the Nth 
# index and returns the number of additions required to calculate the Nth term.
def SUMS(n):
    if (n == 0 or n == 1 or n == 2): # Base Case checks for n = 1, 2, 3, or 4 b/c given that PAD(0) = PAD(1) = PAD(2) = 1 so no additions are necessary.
        return 0
    elif (n == 3 or n == 4): # n = 3 or 4 just requires 1 addition
        return 1
    else: # Recursive Case adds the number of additions for each function call together, and increments sum by 1 to take into account the current addition.
        x = n - 1
        return(SUMS(x-1)+SUMS(x-2)+1) # Increment by 1


# ANON is a recurisve function that takes in one argument, tree, that should represent a tuple
# and returns the input but with all symbols replaced with '?'.
def ANON(tree):
    #print(tree)
    if (type(tree) != tuple): # Base Case check if the arguement is a tuple (replaces symbols w/ '?')
        new_tup = ('?')
        return(new_tup)
    elif (len(tree) == 0): # Base Case check if the argument is empty (replace with empty tuple)
        return(tuple())
    else: # Recursive Case rcursively unpacks/accesses each tuple/nested tuple
        #print(tree[0])
        return(ANON(tree[0]),) + ANON(tree[1:]) 

# Test Cases for ANON.  Expected output from Homework spec and Piazza
# print('>>> ANON(())')
# print( ANON(()) )
# print( ANON(()) == () )
# print('>>> ANON(None)')
# print( ANON(None) )
# print( ANON(None) == "?" )
# print('>>> ANON(42)')
# print( ANON(42) )
# print( ANON(42) == "?" )
# print('>>> ANON("FOO")')
# print( ANON("FOO") )
# print( ANON("FOO") == "?" )
# print('>>> ANON(((("L", "E"), "F"), "T"))')
# print( ANON(((("L", "E"), "F"), "T")) )
# print( ANON(((("L", "E"), "F"), "T")) == ((('?', '?'), '?'), '?') )
# print('>>> ANON((5, "FOO", 3.1, -0.2))')
# print( ANON((5, "FOO", 3.1, -0.2)) )
# print( ANON((5, "FOO", 3.1, -0.2)) == ('?', '?', '?', '?') )
# print('>>> ANON((1, ("FOO", 3.1), -0.2))')
# print( ANON((1, ("FOO", 3.1), -0.2)) )
# print( ANON((1, ("FOO", 3.1), -0.2)) == ('?', ('?', '?'), '?') )
# print('>>> ANON((((1, 2), ("FOO", 3.1)), ("BAR", -0.2)))')
# print( ANON((((1, 2), ("FOO", 3.1)), ("BAR", -0.2))) )
# print( ANON((((1, 2), ("FOO", 3.1)), ("BAR", -0.2))) == ((('?', '?'), ('?', '?')), ('?', '?')) )
# print('>>> ANON(("R", ("I", ("G", ("H", "T")))))')
# print( ANON(("R", ("I", ("G", ("H", "T"))))) )
# print( ANON(("R", ("I", ("G", ("H", "T"))))) == ('?', ('?', ('?', ('?', '?')))) )
