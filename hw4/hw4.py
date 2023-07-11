##############
# Homework 4 #
##############

# Exercise: Fill this function.
# Returns the index of the variable that corresponds to the fact that
# "Node n gets Color c" when there are k possible colors
def node2var(n, c, k):
    var_index = (n - 1) * k + c
    return var_index

# Exercise: Fill this function
# Returns *a clause* for the constraint:
# "Node n gets at least one color from the set {1, 2, ..., k}"
def at_least_one_color(n, k):
    clause = []
    for color in range(1, k + 1):
        clause.append(node2var(n, color, k))
    return(clause)

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Node n gets at most one color from the set {1, 2, ..., k}"
def at_most_one_color(n, k):
    CNF = []
    clause = at_least_one_color(n, k)
    for i in range(len(clause) - 1, -1, -1):
        del clause[i]
        negClause = [-x for x in clause]
        clause = at_least_one_color(n, k)
        CNF.append(negClause)
    return(CNF)
    
    # Goal all ways to pick 1 less from the total, all negative
    # A CNF is a conjunction (ANDs) of clauses;
    # at_most_one_color should return a CNF represented by a list of lists.)

    # 1 = node 1 is color 1
    # 2 = node 1 is color 2
    # 3 = node 1 is color 3
    # 1 AND NOT(2) AND NOT(3) => NOT(2 OR 3)
    # NOT(1) AND 2 AND NOT(3) => NOT(1 OR 3)
    # NOT(1) AND NOT(2) AND 3 => NOT(1 OR 2)
    # [[1, -2, -3], [-1, 2, -3], [-1, -2, 3], [-1,-2, -3]]
    # AT MOST ONE COLOR: 1 color or no color
    # De Morgan's Law (b/c above is not in CNF Form...)
    # NOT A and NOT B => NOT(A OR B)
    # allow at least 2 colors
    # [[-1, -2], [-1, -3], [-2, -3]]
    # (-1 OR -2) AND (-1 OR -3) AND (-2 OR -3) => NOT 1 AND NOT 2 = NOT(1 OR 2) meaning 
    # 1, 2, 3 (all 3) => not allowed
    # -1, 2, 3 (2 colors) => not alowed
    # -1, -2, 3 (1 color) => allowed
    # -1, -2, -3 (0 color) => allowed
    # [[], [], []]

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Node n gets exactly one color from the set {1, 2, ..., k}"
def generate_node_clauses(n, k):
    CNF = [at_least_one_color(n, k)] + at_most_one_color(n, k)
    # CNF.append(at_least_one_color(n, k))
    # CNF.append(at_most_one_color(n, k))
    return(CNF)

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Nodes connected by an edge e (represented by a list)
# cannot have the same color"
def generate_edge_clauses(e, k):
    # "no two nodes can have the same color" => the opposite of this is that two nodes have the same color
    # node x is color 1, 2,or 3 => [1, 2, 3]
    # node y is color 1, 2, or 3 => [4, 5, 6]
    # DNF: [1 AND 4] OR [2 AND 5] OR [3 AND 6]
    # Using De Morgan's Law: not (A or B) = (not A) and (not B); not (A and B) = (not A) or (not B)
    # CNF: NOT([1 AND 4] OR [2 AND 5] OR [3 AND 6]) => NOT(1 AND 4) AND NOT(2 AND 5) AND NOT(3 AND 6)
    # => [NOT(1) OR NOT(4)] AND [NOT(2) OR NOT(5)] AND [NOT(3) OR NOT(6)]
    # => [-1, -4], [-2, -5], [-3, -6]
    node_x, node_y = e
    CNF = []
    for color in range(1, k + 1):
        clause = [-node2var(node_x, color, k), -node2var(node_y, color, k)]
        CNF.append(clause)
    return(CNF)

# print(node2var(3, 1, 4))
# print(node2var(3, 2, 4))
# print(node2var(3, 3, 4))
# print(node2var(3, 4, 4))
# print(node2var(2, 1, 4))
# print(node2var(2, 2, 4))
# print(node2var(2, 3, 4))
# print(node2var(2, 4, 4))
# e = (1, 2)
#print(node2var(1, 4, 4))
#print(at_least_one_color(1, 3))
#print(at_most_one_color(1, 3))
# print(generate_node_clauses(1, 3))
# print(generate_node_clauses(2, 3))
# print(generate_edge_clauses(e, 4))

# The function below converts a graph coloring problem to SAT
# DO NOT MODIFY
def graph_coloring_to_sat(graph_fl, sat_fl, k):
    clauses = []
    with open(graph_fl) as graph_fp:
        node_count, edge_count = tuple(map(int, graph_fp.readline().split()))
        for n in range(1, node_count + 1):
            clauses += generate_node_clauses(n, k)
        for _ in range(edge_count):
            e = tuple(map(int, graph_fp.readline().split()))
            clauses += generate_edge_clauses(e, k)
    var_count = node_count * k
    clause_count = len(clauses)
    with open(sat_fl, 'w') as sat_fp:
        sat_fp.write("p cnf %d %d\n" % (var_count, clause_count))
        for clause in clauses:
            sat_fp.write(" ".join(map(str, clause)) + " 0\n")

# graph_coloring_to_sat("graph2.txt", "graph2_8colors.txt", 8)
# print(generate_node_clauses(1, 3))
# Example function call
# if __name__ == "__main__":
#    graph_coloring_to_sat("graph1.txt", "graph1_3colors.txt", 3)
