"""
v1.1 11-19-20
My solution for the 3.16 working example in Chap. 3 of
Think Python by Allen Downey

I have improved on the challenge so that you can build
a grid of any size by adjusting the variables num_rows
and num_cols.

I will add a user entry box in the code as the next task

"""

num_rows = 7
num_cols = 4

t_r = "+ - - - -" #single grid beam unit
m_r = "|        " #single row post unit

#function prints a three column beam and appends a final '+'
def beam_print(arg):
    i = 0
    while i < num_cols:
        print(arg, end=' ')
        i = i + 1
    print('+')

#function prints a three column post and appends a final '|'
def post_print(arg):
    j = 0
    while j < num_cols:
        print(arg, end=' ')
        j = j + 1
    print("|")

#construct the middle of a block
def do_four(f,arg):
    f(arg)
    f(arg)
    f(arg)
    f(arg)

def print_unit():
    beam_print(t_r)
    do_four(post_print, m_r)

#builds a three row grid
def build_grid():
    k = 0
    while k < num_rows:
        print_unit()
        k = k+1
    beam_print(t_r)

build_grid()


    
