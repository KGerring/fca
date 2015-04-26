from fca import *
import random
import string

def random_context(n0, n, m, x):
    context0 = []
    for i in range(n0):
        rand_list_bool = []
        for j in range(m):
            if x > random.random():
                rand_list_bool.append(True)
            else:
                rand_list_bool.append(False)
        context0 = context0 + [rand_list_bool]
    context = []
    if n != n0:
        for i in range(n):
            j = random.randint(0, n0-1)
            context.append(context0[j])
    else:
        for i in range(n):
            context.append(context0[i])
    
    objs = ['Obj '+str(j+1) for j in range(len(context))]
    attrs = [list(string.ascii_uppercase)[i] for i in range(m)]
    c = Context(context, objs, attrs)
    write_cxt(c, 'context_random.cxt')
    return c
