from typing import Any, Callable


union_type = int | float
class Calculator():
    def __init__(self,func) :
        self.func = func
    
    def __call__(self, *args):
        result =  self.func(args)
        print("runnnn")
        return result
        