from fca import *

n = 9600
ct1 = [[True, True, True, False, False, False, False, False, False, False, False, False]  for j1 in range(n/3)]
ct2 = [[False, False, False, True, True, True, False, False, False, False, False, False]  for j2 in range(n/3)]
ct3 = [[False, False, False, False, False, False, True, True, True, False, False, False]  for j3 in range(int(n/4.28))]
ct4 = [[False, False, False, False, False, False, False, False, False, True, True, True]  for j4 in range(n/10)]
ct = ct1 + ct2 + ct3 + ct4
objs = ['Obj '+str(j+1) for j in range(len(ct))]
attrs = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'G', 'J', 'K', 'L']
c = Context(ct, objs, attrs)
write_cxt(c, 'context_antichain_'+str(n)+'.cxt')
