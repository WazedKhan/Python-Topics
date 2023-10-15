# <center> <h3>Variables In Python and Its Nature</h3> </center>

<p style = "color:grey; text:bold;">A variable is a value that can change, depending on conditions or on information passed to the program.</p>

<span> In python we do not need to declare variable before using them ( _there are no declarations_ )    </span> </br>


> ## Variable Assignment
<strong>Assignment statements can be plain or augmented</strong>

<p>Plain assignment is to a variables is how we create a new varible.</p>

<h3 style="color:green;"> Plain Assignment: </h3>
<code>
x = 10 | <i>This is read as "x assigned value 10"</i> </br>
</code>

Python also supports chain assignment, which is assign same value to multiple variables. </br>
<code>x = y = z = 100</code>

`print(x, y, z)` #results x = 100, y =  100, z = 100

assign values to multiple variables in one line: </br>
`x, y, z = "Orange", "Banana", "Cherry"` #results x = Orange, y = Banana, z = Cherry

<h3 style="color:green;"> Augmented Assignment: </h3>

In augmented assignment we use augmented operator(+, -, etc) followed by assignment operator(=) instead of only assignment operator(=) between target and expression.

`x += 10`

`x += y`

Augmented assignment doesn't support chain assignments.


>## Variable Types

<p>In most of the programming languages, variables are statically typed. Which means we have to declare variable type before assignment. Like in C:   <code> int x;  x = 10 or int x = 10; </code> so x is now assigned as integer type variable and the value assigned to the variable can't not be changed, we can not re-assign different type value to it. (<span style="color: red;"> x = "String"</span> is not allowed as value is string and variable type is integer) </p>

In python variables are not statically typed its means we can assign a integer value to it </br>
<code> x = 10 </code> </br>
and then we can re-assign to variable x a string string value </br>
`x = 'string'` </br>
Now the question arises how does python handle assignments?

Python is highly object-oriented, virtually every data item in python is an object of a type or class. For example, think of `x = 10` assigning the integer 10 to x at this time 3 things happen.

1. Creates an integer object

<img src="assets/int_obj.png">

2. Gives it the value 10

<img src="assets/10.png">

3. Sets name `x` to hold the reference to the object

<img src="assets/x=10.png">

Now if look at the type of the variable:

`x = 100`

`print( type(x) )`

`<class 'int'>`

Now re-assigning a "string" to x

`x = 'Hello'`

`print(type(x))`

`<class 'str'>`

So its proves that `x` is just holding an object reference.

> Object Identity

Whenever an object is created in python, a unique integer is given to identify it.

Built-in 