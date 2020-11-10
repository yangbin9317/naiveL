from typing import Union, List, Any

class Symbol(str):
    pass

class String(str):
    pass

class Number(int):
    pass

class Pair():

    def __init__(self, v1: Any, v2: Any):
        self.car: Pair = v1
        self.cdr: Pair = v2

    def __str__(self):
        tmp = self
        l = []
        while tmp is not None:
            l.append(str(tmp.car))
            tmp = tmp.cdr
        return '(%s)' % (' '.join(l))

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Pair):
            raise ValueError('%s is not Pair' % o)
        return self.car == o.car and self.cdr == o.cdr

class Procedure():

    def __init__(self, param: Pair, body: Pair, env: Any):
        self.param = param
        self.body = body
        self.env = env
        
    def __str__(self):
        return 'procedure(param: %s body: %s)' % (self.param, self.body)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Procedure):
            raise ValueError('%s is not Procedure' % other)
        return other.param == self.param and other.body == self.body

Value = Union[Symbol, String, Number, Pair, Procedure]