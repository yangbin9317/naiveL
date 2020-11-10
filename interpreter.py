from eval_apply import eval_pair
from typing import List
from value import *
from eval_apply import *
from util import *

def tokenize(chars: str) -> list:
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def read(tokens: list) -> Value:
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')

    token = tokens.pop(0)
    if token == '(':
        return read_pair(tokens)
    else:
        return read_value(token)

def read_value(token: str) -> Value:
    if is_string(token):
        return read_string(token)
    elif is_number(token):
        return read_number(token)
    else:
        return read_symbol(token)

def read_pair(tokens: list) -> Pair:
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')

    if tokens[0] == ')':
        tokens.pop(0)
        return None

    p = Pair(None, None)
    p.car = read(tokens)
    p.cdr = read_pair(tokens)

    return p

def read_string(code: str) -> Value:
    return read(tokenize(code))

def eval_string(code: str, env) -> Value:
    tokens = tokenize(code)
    exp = read(tokens)
    return eval_exp(exp, env)