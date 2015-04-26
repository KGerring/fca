from fca import *
import random
from copy import deepcopy
from sets import Set

contexts = ['context_chain.cxt', 'context_chain_1.cxt', 'context_chain_enlarged.cxt', 'context_antichain.cxt', 'context_3.cxt', 'context_4.cxt']

def generate_noise_cxt_type1(context, percentage):
    n = len(context.objects)
    m = len(context.attributes)
    context_type1 = deepcopy(context)
    x = float(percentage)/100
    for i in range(n):
        for j in range(m):
            if random.random() < x:
                context_type1[i][j] = not context_type1[i][j]
    return context_type1
    
    

def generate_noise_cxt_type2(context, percentage_obj, percentage_attr, k):
    n = len(context.objects)
    m = len(context.attributes)
    # calculate a sparseness proportion of the context
    count = 0
    if k == 1:
        for o in context:
            for a in o:
                if a==True:
                    count+=1
    k = float(count)/(m*n)
    # type2 noise for objects: 
    # y_obj - number of objects to add
    y_obj = n*percentage_obj/100
    count = y_obj
    context_type2 = deepcopy(context)
    while y_obj != 0:
        row = [False]*m
        for i in range(m):
            if random.random() < k:
                row[i] = True
        context_type2.add_object(row, 'Obj_noise ' + str(int(count-y_obj+1)))
        y_obj-=1
    # type2 noise for attributes: 
    # y_attr - number of objects to add
    y_attr = m*percentage_attr/100
    count = y_attr
    while y_attr != 0:
        list1 = random.sample(xrange(len(context_type2.objects)),
                              random.randint(1,int(k*len(context_type2.objects))))
        column = [False]*len(context_type2.objects)
        for i in list1:
            column[i] = True
        context_type2.add_attribute(column, 'm_noise' + str(int(count-y_attr+1)))
        y_attr-=1

    return context_type2


def distance(concept_sys1, concept_sys2, dist_type):
    intent1 = set([frozenset(concept_sys1[j].intent) for j in range(len(concept_sys1))])
    intent2 = set([frozenset(concept_sys2[j].intent) for j in range(len(concept_sys2))])    
    if dist_type == 'sym_diff':
        return len(intent1.symmetric_difference(intent2))
    if dist_type == 'jaccard':
        return 1-len(intent1.intersection(intent2))/float(len(intent1.union(intent2)))
    if dist_type == '10':
        if intent1 == intent2:
            return 0
        else:
            return 1
        
def test(context_paths, dist_type, n):
    for context_path in context_paths:
        f = open('result_'+dist_type+'_'+context_path,'w')
        context = read_cxt(context_path)
        c = ConceptLattice(context, builder=norris)
        for kkk in [3, 5, 8, 10, 15, 20]:
            result1 = []
            result2 = []
            for i in range(n):
                context1 = generate_noise_cxt_type1(context, kkk)
                context2 = generate_noise_cxt_type2(context, kkk, 0, 1)
                c1 = ConceptLattice(context1, builder=norris)
                c2 = ConceptLattice(context2, builder=norris)
                c1f = filter_concepts(c1, compute_istability, "abs", len(c1))
                c2f = filter_concepts(c2, compute_istability, "abs", len(c2))
                minimal_distance1 = 10000 # РїРѕРјРµРЅСЏС‚СЊ РјРёРЅ СЂР°СЃСЃС‚РѕСЏРЅРёРµ
                minimal_distance2 = 10000
                for k in range (0,len(c1f)+1):
                    c1fk = [c1f[j] for j in range(k)]
                    current_distance = distance(c, c1fk, dist_type)
                    minimal_distance1 = min(minimal_distance1, current_distance)
                    if minimal_distance1 == 0:
                        break
                for k in range (0,len(c2f)+1):
                    c2fk = [c2f[j] for j in range(k)]
                    current_distance = distance(c, c2fk, dist_type)
                    minimal_distance2 = min(minimal_distance2, current_distance)
                    if minimal_distance2 == 0:
                        break
                
                result1.append(minimal_distance1)
                result2.append(minimal_distance2)
            print context_path, kkk, sum(result1) / float(len(result1)), sum(result2) / float(len(result2))
            f.write(str(kkk) + ' ' + str(sum(result1) / float(len(result1))) + ' ' + str(sum(result2) / float(len(result2))) + '\n')
        f.close()
