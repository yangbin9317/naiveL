import inspect
from typing import Callable
from value import *

def is_string(code: str) -> bool:
    return code[0] == '"' and code[-1] == '"'

def is_number(code: str) -> bool:
    return code.isnumeric()

def read_string(code: str) -> String:
    if len(code) < 2:
        raise SyntaxError('%s is not string' % code)
    return String(code[1:-1])

def read_number(code: str) -> Number:
    return Number(code)

def read_symbol(code: str) -> Symbol:
    return Symbol(code)

def cons(v1: Value, v2: Value) -> Pair:
    p = Pair(v1, v2)
    return p

def list_to_pair(l: List[Value]) -> Pair:
    if l == []:
        return None
    return cons(l[0], list_to_pair(l[1:]))

def pair_to_list(p: Pair) -> List[Value]:
    if p is None:
        return []
    return [p.car] + pair_to_list(p.cdr)

def pair_map(f: Callable[[Pair], Pair], p: Pair) -> Pair:
    if p is None:
        return None

    newCar = f(p.car)
    newCdr = pair_map(f, p.cdr)
    return Pair(newCar, newCdr)

def dump_args(func):

    def wrapper(*args, **kwargs):
        if False:
            func_args = inspect.signature(func).bind(*args, **kwargs).arguments
            func_args_str = ", ".join(
                "{} = {}".format(*item) for item in func_args.items()
            )
            print(f"{func.__module__}.{func.__qualname__} ( {func_args_str} )")
        return func(*args, **kwargs)

    return wrapper