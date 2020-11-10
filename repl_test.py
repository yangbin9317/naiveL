import unittest
from util import list_to_pair
from interpreter import eval_string
from eval_apply import eval_exp
from env import Env
from value import Number, Symbol, Procedure

class TestUtil(unittest.TestCase):

    # def test_self_eval(self):
    #     env = Env()
    #     result = eval_exp(Number(1), env)
    #     self.assertEqual(result, Number(1))

    def test_eval_pair(self):
        cases = [
            # (
            #     '(+ (+ 1 2) 3)', Number(6)
            # ),
            # (
            #     '(lambda (x y) (+ 1 2) (+ 2 3) )', Procedure(
            #         list_to_pair([Symbol('x'), Symbol('y')]), 
            #         list_to_pair([
            #             list_to_pair([Symbol('+'), Number(1), Number(2)]), 
            #             list_to_pair([Symbol('+'), Number(2), Number(3)]), 
            #         ]),
            #         Env()),
            # ),
            (
                '((lambda (x y) (+ x y)) 1)', Procedure(
                    list_to_pair([Symbol('y')]), 
                    list_to_pair([
                        list_to_pair([Symbol('+'), Symbol('x'), Symbol('y')])
                    ]), 
                    Env()),
            ),
            # (
            #     '((lambda (x y) (+ x y)) 1 2)', Number(3),
            # ),
            # (
            #     '(define x 1)', None,
            # ),
        ]

        for c in cases:
            env = Env()
            print('case %s' % c[0])
            result = eval_string(c[0], env)
            print('result %s' % result)
            self.assertEqual(result, c[1])
            print()

if __name__ == '__main__':
    unittest.main()