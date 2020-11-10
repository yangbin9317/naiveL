from value import * 

class Env():

    def __init__(self, outter=None):
        self.env = {}
        self.outter = outter

    def lookup(self, token: str) -> Value:
        if token in self.env:
            return self.env[token]
        if self.outter is None:
            raise ValueError('token %s not found in env' % token)
        return self.outter.lookup(token)
    
    def define(self, sym: Symbol, val: Value) -> None:
        self.env[sym] = val

    def __str__(self) -> String:
        return 'env: %s, outter: %s' % (self.env, self.outter)
