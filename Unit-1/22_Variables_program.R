# create a new variable called my.num that contains 6 numbers

var1 = "hello"
print(var1)

var2 <- "hello"
print(var2)

"hello" -> var3
print(var3)


# multiply my.num by 4

a <- 4
b <- 9
result <- a * b
print(result) 



# create a second variable called my.char that contains 5 character strings

assign("variable_name",3)

print(variable_name)


# combine the two variables my.num and my.char into a variable called both

string1 <- "Geeks" # 
string2 <- "forGeeks" 

vec <- cbind(string1, string2) # combined vector.

S <- paste(string1, string2, sep ="")

print(S)# print the output string

M <- paste(vec, collapse = "#")
print(M)


# what is the length of both?

x <- c(6)
y <- c(1, 2, 3, 4, 5)

length(x)
length(y)

# what class is both?

a <- list(name="yanshu", Roll_No=7144)

class(a) <- "Student"

a

# divide both by 3, what happens?

gender <- c("m", "f", "f", "f", "m", "m", "f", "m", "f", "f", "m") 
height <- c(71, 64, 65, 70, 79, 80, 69, 79, 70, 71, 78) 
df <- data.frame(gender, height) 

cat("Original data frame:\n") 
print(df) 
 
s <- split(df, df$gender) 

cat("\nAfter splitting data:\n") 
print(s) 


# create a vector with elements 1 2 3 4 5 6 and call it x

vec=c( 1 : 20, "jenish", "yanshu",
       "meet", 45.7, 56, 34, 56)
print(vec)



# create another vector with elements 10 20 30 40 50 and call it y

for (i in 1:5) {
  cat("Iteration ", i, "\n")
}


# what happens if you try to add x and y together? why?

vec1 <- 1:9
vec1

vec2 <-9:1
vec2

c(vec1,vec2)


# append the value 60 onto the vector y (hint: you can use the c() function)

x <- rep(1:5) 

gfg <- append(x, 10) 

print(gfg) 


# add x and y together

x <- c(1.3, 3.5, 1.4, -3.1, 5.7, 2.4, 
       3.3, 2.5, 2.3, 1.9, 1.8, 2.3)
y <- c(2.5, 5.8, 2.1, -3, 12, 5, 6.2,
       4.8, 4.2, 3.5, 3.7, 5.2)

plot(x, y, cex = 1, pch = 3,
     xlab ="x", ylab ="y",
     col ="Red")

lines(x, y, col = "Blue")


# multiply x and y together. pay attention to how R performs operations on vectors of the same length.

X <- c(1, 4, 5, 2, 6, 7) 
print('using c function')
print(X)

Y <- seq(1, 10, length.out = 5) 
print('using seq() function') 
print(Y)

Z <- 5:10
print('using colon')
print(Y)

