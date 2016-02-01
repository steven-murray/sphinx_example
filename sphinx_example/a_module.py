"""
A module defining several objects aimed at showing different parts of the sphinx reportoire.
"""
import numpy as np

def a_one_liner(a):
    print "Result is: ", a

def a_math_func(a,b,hypot=True):
    if hypot:
        c = np.sqrt(a**2 + b**2)
        a_one_liner(c)
        return c
    else:
        a = np.atleast_1d(a)
        b = np.atleast_1d(b)
        h = np.where(a>=b,a,b)
        s = np.where(a<b,a,b)
        c = np.sqrt(h**2 - s**2)
        if len(c)==1:
            c = c[0]
        a_one_liner(c)
        return c

class Klass(object):
    x = 0

    def __init__(self,thing):
        self.thing = thing

    def tell_me(self):
        print "I like %s about %s"%(self.thing,self.x)

    @property
    def love_factor(self):
        return 4*self.x