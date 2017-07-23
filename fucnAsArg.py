s = raw_input()
n = input()
def exploder(x):
    print(x*n)
def myfun(exp,s):
    for item in s:
	exp(item)
myfun(exploder,s)