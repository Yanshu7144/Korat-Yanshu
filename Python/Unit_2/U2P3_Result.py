# Result
#U2P3

s1=int(input("Enter A Mark s1="))
s2=int(input("Enter A Mark s2="))
s3=int(input("Enter A Mark s3="))
s4=int(input("Enter A Mark s4="))

Total_Mark = s1+s2+s3+s4
print("student Total_Mark =",Total_Mark)

Per = (Total_Mark/400) *100
print(Per)

if s1<40 or s2<40 or s3<40 or s4<40:
    result='Fail'
    grade='With Held**'
    
else:
    result='Pass'
    if Per > 90:
        grade='A+'
    elif 90<Per<70:
        grade='A'
    elif 70<Per<60:
        grade='B'
    elif 40<Per<60:
        grade='C'
    else:
        grade='F'
print("Reselt =",result)
print("Grade =",grade)

