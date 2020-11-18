"""
My solution for the 3.16 working example in Chap. 3 of
Think Python by Allen Dennings

My plan was to have the code build a grid by changing only
the following two variables:

num_rows = X
num_col = Y

Still a work in progress...
"""


t_r = "+ - - - -" #single grid beam unit
m_r = "|        " #single row post unit

#function prints a three column beam and appends a final '+'
def beam_print(arg): 
    print(arg,arg,arg,'+')

#function prints a three column post and appends a final '|'
def post_print(arg):
    print(arg,arg,arg,"|")

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
    print_unit()
    print_unit()
    print_unit()
    beam_print(t_r)

build_grid()


    
