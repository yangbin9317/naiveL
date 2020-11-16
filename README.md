# A naive language like Lisp

## define var
`(define x 1)`

`x`

get `1`

## lambda: 
`(lambda (x y) (+ x y))`

get `procedure(param: (x y) body: ((+ x y)))`

## eval lambda

`((lambda (x y) (+ x y)) 1 2)`

`3`

## define func

`(define (f x y) (+ x y))` // syntax surgar for (define f (lambda (x y) (+ x y)))

## apply func

`(f 1 2)`

get `3`

## partial apply

`(define (f x y) (+ x y))` 

`f`

get `procedure(param: (x y) body: ((+ x y)))`

`(f 1)`

get `procedure(param: (y) body: ((+ x y)))`

`(define g (f 1))`

`(g 2)`

get `3`
