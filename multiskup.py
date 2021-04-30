import collections as ct
import bisect
s=[1,1,1,2,2,2,2,3,4,5,5]
skup=ct.Counter(s)
class Multiskup(object):

    def __init__(self, skup=None):
        self.__kljucevi=[]
        self.__skup={}
        
        if skup is not None:
            if isinstance(skup, Multiskup):
                self.__skup=skup.__skup.copy()
                self.__kljucevi=list(skup.__kljucevi)
            else:
                self.__skup=dict(skup)
                self.__kljucevi=sorted(self.__skup.keys())
                
    
    def __repr__(self):
        djelovi = []
        for key in self.__kljucevi:
            djelovi.append("%r * %r" % (key, self.__skup[key]))
        return "UredjeniRjecnik({%s})" % ", ".join(djelovi)
    
    def __str__(self):
        return repr(self)
    
    def __iter__(self):
        return iter(self.__kljucevi)
mskup=Multiskup(skup)
for el in mskup:
    print(el)

                