import traceback
from env import Env
from interpreter import eval_string

class Repl:
    def __init__(self):
        self.env = Env()
        self.code = ''

    def valid(self, code: str) -> bool:
        count = 0
        for c in code:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            if count < 0:
                raise Exception('not a list, %s' % self.code)

        return count == 0

    def rep(self, prompt='REPL: '):
        self.code += input(prompt).strip()
        if self.code == '' or not self.valid(self.code):
            return

        print(eval_string(self.code, self.env))
        self.code = ''

    def loop(self):
        while True:
            try:
                self.rep()
            except Exception:
                self.code = ''
                print(traceback.format_exc())

if __name__ == '__main__':
    Repl().loop()
