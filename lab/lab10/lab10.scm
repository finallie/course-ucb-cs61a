(define (make-adder num) (lambda (x) (+ x num)))

(define (composed f g) (lambda (x) (f (g x))))

(define (my-filter pred s) (cond ((null? s) '())
                                 ((pred (car s)) (cons (car s) (my-filter pred (cdr s))))
                                 (else (my-filter pred (cdr s)))))

(define (exp b n)
  (define (helper n acc p) 
    (cond 
      ((= n 0) acc)
      ((even? n) (helper (/ n 2) acc (* p p)))
      (else (helper (- n 1) (* acc p) p))
    )
  )
  (helper n 1 b))

(define (interleave lst1 lst2) 
  (cond 
    ((null? lst1) lst2)
    ((null? lst2) lst1)
    (else (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2)))))
  )
)

(define (square n) (* n n))

(define (pow base exp)
  (define (helper base exp acc)
    (cond 
      ((= exp 0) acc)
      ((even? exp) (helper (square base) (/ exp 2) acc))
      (else (helper base (- exp 1) (* acc base)))
    )
  )
  (helper base exp 1)
)
