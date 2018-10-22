## Conditional expression
result = true_value if <condition is true> else false_value

## Lambda / Anonymous Function Object
Lambda is an anonymous function. Example

scientists = ['Marie Curie', 'Albert Einstein', 'Niels Bohr', 'Issac Newton', 'Alfred Wegener', 'Charles Darwin']

sorted(scientists, key=lambda name: name.split()[-1])

-----
is_odd = lambda x: x % 2 == 1
is_even = lambda x: x % 2 == 0

> Read more on Lambda Function
