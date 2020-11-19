"""
v1.2 11-19-20
My solution for the 3.16 working example in Chap. 3 of
Think Python by Allen Downey

I have improved on the challenge so that you can build
a grid of any size by adjusting the variables num_rows
and num_cols.

Code to build unit is now encapsulated for simplicity

I will add a user entry box in the code as the next task

"""

num_rows = 3
num_cols = 3

t_r = "+ - - - -" #single unit beam
m_r = "|        " #single unit post

#function prints out 
def unit_print(a,b):
    for i in range(b):
        print(a,end=' ')
        

#function prints a 'beam' row with num_cols*columns
def beam_print(arg):
    unit_print(arg,num_cols)
    print('+')
#

#function prints a 'post'row with num_cols*columns
def post_print(arg):
    unit_print(arg,num_cols)        
    print("|")
#

#construct the middle of a block
def do_four(f,arg):
    for i in range(4):
        f(arg)
    
def print_unit():
    beam_print(t_r)
    do_four(post_print, m_r)
#

#builds a grid with num_rows*rows
def build_grid():
    for i in range(num_rows):
        print_unit()        
    beam_print(t_r)
#

build_grid()
