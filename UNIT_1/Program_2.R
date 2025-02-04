# 2. Write R script for some inbuilt functions like : seq(),min(),max(),assign(),print().

#Create a sequence of number
sequence<-seq(1,10,by=2)
print(sequence)

#Find minimum value
min_value<-min(1,2,3,5,4)
print(min_value)

#Find maximum value
max_value<-max(1,2,3,5,4)
print(max_value)

#Assign value to a variable
assign("myVar",100)
print(myVar)

#Print a message
print("Hello,R!")