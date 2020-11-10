from typing import List, Union
from value import *
from env import *

class Exp():

    def __init__(self, exps: List[Exp]) -> Union[Value, Exp]:
        self.values = exps

    def eval(self, env: Env):
        l = map(lambda e: e.eval(), self.values)

        procSymbol = l[0]
        parameter = [] if len(l) == 0 else l[1:]

        if not isinstance(procSymbol, Symbol):
            raise ValueError('can not use %s: %s as procedure' % (procSymbol, type(procSymbol)))

        if isNativeProcedure(procSymbol):
            return applyNativeProcedure(procSymbol, parameter)
        
        procedure = env.lookup(procSymbol)
        if procedure is None:
            raise ValueError('procedure %s not found' % procSymbol)
        if not isinstance(procedure, Procedure):
            raise ValueError('%s is not procedure' % procSymbol)

        return procedure.apply(parameter)


class ValueExp(Exp):

    def __init__(self, value: Value):
        self.value = value

    def eval(self, env: Env) -> Value:
        return self.value