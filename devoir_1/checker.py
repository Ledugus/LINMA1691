import solve

### Just do "python checker.py" to launch the tests ###

"""
    Interpret one line in numbers
"""
def load_num(f_in):
    num_str = f_in.readline()
    return list(map(int, num_str.split()))

"""
    Load graph into its adjacency list
"""
def load_graph(f_in):
    # number of nodes and edges
    N,E = load_num(f_in)

    # Construct the adjacency list
    adj = [list() for _ in range(N)]
    for i in range(E):
        x,y = load_num(f_in)
        adj[x-1].append(y-1)

    return adj

"""
    For all the problems in one file : load graph and solve it
"""
def read_and_solve_tests(input_file, output_file):
    f_in = open(input_file, "r")
    f_out = open(output_file, "w")

    n_prob = int(f_in.readline())
    for _ in range(n_prob):
        adj = load_graph(f_in)
        f_out.write(str(solve.solve(adj)) + "\n")

    f_in.close()
    f_out.close()

"""
    Simply compares if two files are identical (expected output versus computed output)
"""
def compare_files(file1, file2):
    f1 = open(file1, "r")
    f2 = open(file2, "r")

    the_same = True
    line_num = 0
    while the_same:
        l1 = f1.readline()
        l2 = f2.readline()
        if l1=="" or l1=="\n":
            break
        the_same = int(l1.split()[0]) == int(l2.split()[0])
        if not the_same:
            print('expected output : ' + str(int(l1.split()[0])))
            print('computed output : ' + str(int(l2.split()[0])))
        line_num = line_num+1

    f1.close()
    f2.close()
    return the_same, line_num

"""
    Test for one file
"""
def do_test(test):
    input_file = "tests/input"+str(test)+".txt"
    expected_output_file = "tests/output"+str(test)+".txt"

    read_and_solve_tests(input_file, "tmp/output"+str(test)+".txt")
    ok,errorLine = compare_files(expected_output_file, "tmp/output"+str(test)+".txt")
    if not ok:
        print("Difference between output and expected output for test : "+str(test)+ " on line : "+str(errorLine))
    else:
        print("Test "+str(test)+" is ok :)")

for i in range(5):
    do_test(i+1)
