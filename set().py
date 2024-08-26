from __future__ import annotations
from types import UnionType
from typing import Any
from functools import reduce



class Myset:
    def __init__(self, *args) -> None:
        self. args = list(args)
        i=0
        for number in self.args:
            if number  in self.args[:(i:=i+1)-1]:
                self.args.remove(number)
                
    def __repr__(self) -> str:
        return f" {list(self.args)}"
    
    def __len__(self):
        return len(self.args)
    
    def __contains__(self, item):
        return item in self.args
    
    def __iter__(self):
        return iter(self.args)
    
    def add(self, item):
        if item in self.args:
            None
        else: self.args.append(item)
                
    def remove(self, item):
        if item in self.args:
            self.args.remove(item)
        else : return KeyError (f"{item} not found")

    def __eq__(self, item: object) -> bool:
        if isinstance(item,Myset):
            return self.args == item.args
        else:
            return False
    
    def __lt__(self , item : Myset):
        return len(self) < len(item)
    
    def __gt__(self , item : Myset):
        return len (self) > len (item)
        
    def  __or__(self, item: Myset) :
        i = 0
        union = Myset(*(self.args + list(item)))
        search = (number for number in self.args if number not in self.args[:(i:=i+1)-1])
        return union , search
        # for number in self:
        #     if number  in self.args[:(i:=i+1)-1]:
        #         self.args.remove(number)
            
        
    def __and__(self,item : Myset):
        intections  = Myset(*( x for x in self.args if x in item ))
        return intections
        

    def __sub__(self,item : Myset):
        defference = Myset(*( x for x in self.args if x not in item))
        return defference
        

    
set1 = Myset(1,10,2,3,5,5,6)
set2 = Myset(1,10,2,3,5)
print(set1)
print(set2)
print(set1 > set2)
print(set1 < set2)
print(set1 == set2)
print(len(set1))
print(f"union: ", set1 | set2) 
print(f"intections: ", set1 & set2) 
print(f"difference: ", set1 - set2)