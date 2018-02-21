Strings in Python
#####################
In the video, you learned of another standard Python datatype, strings. Recall that these represent textual data. To assign the string 'DataCamp' to a variable company, you execute:

company = 'DataCamp'
You've also learned to use the operations + and * with strings. Unlike with numeric types such as ints and floats, the + operator concatenates strings together, while the * concatenates multiple copies of a string together. In this exercise, you will use the + and * operations on strings to answer the question below. Execute the following code in the shell:

object1 = "data" + "analysis" + "visualization"
object2 = 1 * 3
object3 = "1" * 3
What are the values in object1, object2, and object3, respectively?

###############
output
#############
object1 contains "dataanalysisvisualization", object2 contains 3, object3 contains "111".

#################

Recapping built-in functions
##############################
In the video, Hugo briefly examined the return behavior of the built-in functions print() and str(). Here, you will use both functions and examine their return values. A variable x has been preloaded for this exercise. Run the code below in the console. Pay close attention to the results to answer the question that follows.

Assign str(x) to a variable y1: y1 = str(x)
Assign print(x) to a variable y2: y2 = print(x)
Check the types of the variables x, y1, and y2.
What are the types of x, y1, and y2?

#######################
output
############

x is a float, y1 is a str, and y2 is a NoneType.

#############
Explaination
##########
In [1]: y1 = str(x)

In [2]: y2 = print(x)
4.89

In [3]: print(type(x))
<class 'float'>

In [4]: print(type(y1))
<class 'str'>

In [5]: print(type(y2))
<class 'NoneType'>

In [6]: 

#############
