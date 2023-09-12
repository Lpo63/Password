#1.1 inplement a recursive function to calculate the factorial of a given numbers

""
11 =1*1
21 =2*11->2*1
31 =3*21->3*2*1
.
.
10!=10*9*8*.........*1

formula-n*(n-1)!
""


def factorial_rec(n)
if n==o or n==1
  return 1
else:
return n* fact_rec(n-1)

number=int(input("enter a value"))
res=fact_rec(number)

print("the factorial of {}is{}".format(number,res))

