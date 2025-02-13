#Compound Interest
#U1P4
p=float(input("Enter First Value P=" ))
r=float(input("Enter Second Value R=" ))
t=float(input("Enter Second Value T=" ))
print("P Value  =",p)
print("R Value =",r)
print("T Value =",t)
A=p*(1+r/100)**t
print("A =",A)
CI=A-p
print("CI= ",CI)

