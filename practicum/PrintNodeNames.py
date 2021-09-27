Tree1 = ("Desk 1",[])
Tree2 = ("Desk 2",[])
Tree3 = ("Office 301",[])
Tree4 = ("Office 302",[Tree1,Tree2])
Tree5 = ("Office 303",[])
Tree6 = ("Left",[Tree3,Tree4,Tree5])
Tree7 = ("Right",[])
Tree8 = ("Floor 1",[])
Tree9 = ("Floor 2",[])
Tree10 = ("Floor 3",[Tree6,Tree7])
Tree11 = ("Building 1",[])
Tree12 = ("Building 2",[Tree8,Tree9,Tree10])
Tree13 = ("Street",[Tree11,Tree12])
 
def print_node_names(T):
    print(T[0])
    for child in T[1]: print_node_names(child)

print_node_names(Tree13)
