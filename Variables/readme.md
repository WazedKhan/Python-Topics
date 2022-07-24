# <center> <h3>Variables In Python and Its Nature</h3> </center>

<p style = "color:grey; text:bold;">A variable is a value that can change, depending on conditions or on information passed to the program.</p>

<span> In python we do not need to declare variable before using them ( _there are no declarations_ )    </span> </br>


> ## Variable Assignment

<code>
x = 10 | <i>This is read as "n assigned value 10"</i> </br>
</code>

Python also supports chain assignment, which is assign same value to multiple variables. </br>
<code>x = y = z = 100</code>

`print(x, y, z)` #results x = 100, y =  100, z = 100

assign values to multiple variables in one line: </br>
`x, y, z = "Orange", "Banana", "Cherry"` #results x = Orange, y = Banana, z = Cherry

>## Variable Types

<p>In most of the programming languages, variables are statically typed. Which means we have to declare variable type before assignment. Like in C   <code> int x;  x = 10 or int x = 10; </code> so x is now assigned as integer type variable and the value assigned to the variable can't not be changed, we can not re-assign different type value to it. <span style="color: red;"> x = "String"</span> is not allowed as value is string and variable type is integer. </p>

In python variables are not statically typed its means we can assign a integer value to it </br>
<code> x = 10 </code> </br>
and then we can re-assign to variable x a string string value </br>
`x = 'string'` </br>

