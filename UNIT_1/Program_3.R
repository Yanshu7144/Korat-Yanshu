# 3. Write a R program to take input from the user (name and age) and display the values. Also print the version of R installation.



name = readline(prompt="Input your name: ")
age =  readline(prompt="Input your age: ")
print(paste("My name is",name, "and I am",age ,"years old."))
print(R.version.string)
