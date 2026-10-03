#!/usr/bin/env python3
"""Targeted exact checks with explicitly encoded textbook data.

Not a proof of every statement or inventory completeness. The separate
derivations and source comparison remain the primary mathematical review.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, gcd, lcm, sqrt
import json
import sympy as sp

out={}
x,m=sp.symbols('x m',real=True)
out['parameter_identity']=str(sp.factor((m-1)*x*x-(m+1)*x+2))
assert sp.expand((x-1)*((m-1)*x-2)-((m-1)*x*x-(m+1)*x+2))==0
out['cubics']=[str(sp.factor(e)) for e in [x**3-4*x*x+x+6,x**3-2*x*x-x+2]]
for values,label in [([4,6,6,8,10,10,12,14],'eight_times'),([5]*2+[10]*5+[15]*3,'weighted_values')]:
    mean=sum(map(F,values))/len(values)
    variance=sum((F(v)-mean)**2 for v in values)/len(values)
    second=sum(F(v*v) for v in values)/len(values)-mean**2
    assert variance==second
    out[label]={'n':len(values),'sum':sum(values),'sum_squares':sum(v*v for v in values),
                'mean':str(mean),'variance_direct':str(variance),'variance_second_moment':str(second),
                'standard_deviation':sqrt(float(variance))}
out['arithmetics']=[{'a':a,'b':b,'gcd':gcd(a,b),'lcm':lcm(a,b)} for a,b in [(180,252),(1071,462),(840,360)]]
ys,zs,ts=sp.symbols('y z t')
out['systems']={
    'c09e01':str(sp.linsolve([x+ys+zs-6,2*x-ys+zs-3,x+2*ys-zs-2],(x,ys,zs))),
    'c09e02':str(sp.linsolve([x+ys-3,ys+zs-5,zs+ts-7,x+ys+zs+ts-10],(x,ys,zs,ts)))}
u=sp.Matrix([1,0,1]);v=sp.Matrix([0,2,1]);cross=u.cross(v)
assert cross.dot(u)==cross.dot(v)==0
out['vector']={'cross':list(map(int,cross)),'norm_squared':int(cross.dot(cross)),'dot':int(u.dot(v))}
urn=list(range(7)); draws=list(combinations(urn,3))
counts={r:sum(sum(b<4 for b in draw)==r for draw in draws) for r in range(4)}
out['urn_no_replacement']={'total':len(draws),'red_counts':counts}
assert counts[2]==18 and counts[3]==4 and sum(counts.values())==35
ordered=list(product(range(7),repeat=2))
out['urn_with_replacement']={'total':len(ordered),'two_red':sum(a<4 and b<4 for a,b in ordered),
    'different':sum((a<4)!=(b<4) for a,b in ordered)}
out['dice']={str(s):sum(a+b==s for a,b in product(range(1,7),repeat=2)) for s in (2,7)}
stock=[F(100)]
for n in range(6):stock.append(F(4,5)*stock[-1]+10)
assert all(stock[n]==50+50*F(4,5)**n for n in range(len(stock)))
out['stock']={'terms':list(map(str,stock)),'sum_0_to_2':str(sum(stock[:3]))}
u=F(10);n=0
while u>=F(61,10):u=u/2+3;n+=1
out['ds2_threshold']={'first_rank':n,'term':str(u),'preceding':str(6+F(4,2**(n-1)))}
assert n==6
out['limits_c03e04']={'right_difference':str(sp.limit(sp.sqrt(x*x+1)-x,x,sp.oo)),
                      'left_difference':str(sp.limit(sp.sqrt(x*x+1)-x,x,-sp.oo)),
                      'left_sum':str(sp.limit(sp.sqrt(x*x+1)+x,x,-sp.oo))}
print(json.dumps(out,ensure_ascii=False,indent=2))
