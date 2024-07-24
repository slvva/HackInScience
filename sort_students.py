my_class= [(85, "Susan"), (6, "Joshua"), (37, "Jeanette")]


def sort_by_mark(my_class):
    my_class=sorted(my_class, reverse=True)
    return my_class
    
def sort_by_name(my_class):
    my_class = sorted(my_class, key = lambda x: x[1])
    return my_class
        
print(sort_by_mark(my_class))
print(sort_by_name(my_class))
