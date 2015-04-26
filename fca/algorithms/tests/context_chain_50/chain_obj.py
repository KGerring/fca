from fca import *

n = 1600
ct1 = [[True, False, False, False, False, False]  for j1 in range(n)]
ct2 = [[True, True, False, False, False, False]  for j2 in range(n)]
ct3 = [[True, True, True, False, False, False]  for j3 in range(n)]
ct4 = [[True, True, True, True, False, False]  for j4 in range(n)]
ct5 = [[True, True, True, True, True, False]  for j5 in range(n)]
ct6 = [[True, True, True, True, True, True]  for j6 in range(n)]
ct = ct1 + ct2 + ct3 + ct4 + ct5 + ct6 
objs = ['Obj '+str(j+1) for j in range(6*n)]
attrs = ['A', 'B', 'C', 'D', 'E', 'F']
c = Context(ct, objs, attrs)
write_cxt(c, 'context_chain_'+str(n)+'.cxt')
