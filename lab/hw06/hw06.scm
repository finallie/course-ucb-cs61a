(define (member? x lst)
  (cond ((null? lst) #f)
        ((equal? x (car lst)) #t)
        (else (member? x (cdr lst))))
)
(define (no-repeats lst) 
  (if (null? lst)
      '()
      (let ((rest (no-repeats (cdr lst))))
        (if (member? (car lst) rest)
            rest
            (cons (car lst) rest)))
  )
)

(define (student-attend-class student class)
  (student-create 
    (student-get-name student)
    (cons class (student-get-classes student))
  ))

(define (teacher-hold-class teacher)
  (define class (teacher-get-classes teacher))
  (teacher-create
    (teacher-get-name teacher)
    class
    (map (lambda (student) (student-attend-class student class)) (teacher-get-students teacher))
  ))


(define (add-leaf t x)
  (if (is-leaf t)
      t
      (begin (define mapped-branches
                     (map (lambda (b) (add-leaf b x)) (branches t)))
             (tree (label t)
                   (append mapped-branches (list (tree x '())))))))
