from value import *
from env import *
from util import *

@dump_args
def eval_exp(val: Value, env: Env) -> Value:

    if isinstance(val, Symbol):
        return env.lookup(val)
    elif isinstance(val, Number) or isinstance(val, String) or isinstance(val, Procedure):
        return val
    elif isinstance(val, Pair):
        return eval_pair(val, env)
    else:
        raise ValueError('unknown exp type %s' % val)


@dump_args
def eval_pair(pair: Pair, env: Env):

    param = pair.cdr

    if is_special_form(pair.car):
            return apply_special_form(pair.car, param, env)

    proc = eval_exp(pair.car, env)
    if not isinstance(proc, Procedure):
        raise ValueError('car of pair %s is %s need Procedure' % (pair, type(proc)))
    
    return apply(proc, param, env)


@dump_args
def apply(proc: Procedure, param: Pair, env: Env) -> Value:

    if proc.param is None:
        if param is not None:
            raise ValueError('too many param for Procedure %s' % proc)

        if proc.body.cdr is None:
            return eval_exp(proc.body.car, proc.env)
        else:
            eval_exp(proc.body.car, proc.env)
            newProc = Procedure(proc.param, proc.body.cdr, proc.env)
            return apply(newProc, param, proc.env)

    if param is None:
        return proc

    # partial apply
    newEnv = Env(env if len(proc.env.env) == 0 else proc.env)
    newEnv.define(proc.param.car, eval_exp(param.car, env))
    newProc = Procedure(proc.param.cdr, proc.body, newEnv)
    return apply(newProc, param.cdr, newEnv)

# special form

def add(p: Pair, env: Env) -> Value:
    if p is None:
        return Number(0)

    val = eval_exp(p.car, env)
    if not isinstance(val, Number):
        raise ValueError('%s is not Number' % val)

    return Number(val + add(p.cdr, env))

def sub(p: Pair, env: Env) -> Value:
    return Number(eval_exp(p.car, env) - eval_exp(p.cdr.car, env))

def eq(p: Pair, env: Env) -> bool:
    return eval_exp(p.car, env) == eval_exp(p.cdr.car, env)

def lt(p: Pair, env: Env) -> bool:
    return eval_exp(p.car, env) < eval_exp(p.cdr.car, env)

def le(p: Pair, env: Env) -> bool:
    return eval_exp(p.car, env) <= eval_exp(p.cdr.car, env)

def cons(p: Pair, env: Env) -> Pair:
    pass

def define(p: Pair, env: Env) -> None:
    if isinstance(p.car, Symbol):
        env.define(p.car, eval_exp(p.cdr.car, env))
    elif isinstance(p.car, Pair):
        func_def = p.car
        func_name = func_def.car
        func_para = func_def.cdr
        func_body = p.cdr
        env.define(func_name, Procedure(func_para, func_body, env))
    else:
        raise ValueError('can not define %s' % p)

def _lambda(p: Pair, env: Env) -> Procedure:
    if p is None:
        raise ValueError('no lambda param %s' % p)
    elif p.cdr is None:
        raise ValueError('no lambda body %s' % p)

    return Procedure(p.car, p.cdr, env)

def _if(p: Pair, env: Env) -> Value:
    return eval_exp(p.cdr.car, env) if eval_exp(p.car, env) else eval_exp(p.cdr.cdr.car, env)

special_form = {
    Symbol('+'): add,
    Symbol('-'): sub,
    Symbol('='): eq,
    Symbol('<'): lt,
    Symbol('<='): le,
    Symbol('if'): _if,
    Symbol('lambda'): _lambda,
    Symbol('define'): define,
    Symbol('cons'): cons,

    Symbol('加'): add,
    Symbol('减'): sub,
    Symbol('等于'): eq,
    Symbol('小于'): lt,
    Symbol('如果'): _if,
    Symbol('兰姆达'): _lambda,
    Symbol('定义'): define,
    Symbol('组合'): cons,

    Symbol('赋能'): define,
    Symbol('细分'): _if,
}

def is_special_form(form: Symbol) -> bool:
    return isinstance(form, Symbol) and form in special_form

def apply_special_form(form: Symbol, param: Pair, env: Env) -> Value:
    f = special_form[form]
    return f(param, env)
