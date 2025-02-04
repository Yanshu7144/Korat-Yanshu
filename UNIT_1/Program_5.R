# 5. Write a program to create Multiplication table of given number

num = as.integer(readline(prompt = "Enter a number: "))

for(i in 1:10) {
  print(paste(num,'x', i, '=', num*i))
}