0x12. JavaScript - Warm up

Resources:
1. [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity)
2. [Variables](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Variables)
3. [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures)
4. [Operators](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity)
5. [Operators precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
6. [Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
7. [Functions](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Functions)
8. [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Advanced_JavaScript_objects)
9. [Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Advanced_JavaScript_objects)
10. [Module patterns](https://darrenderidder.github.io/talks/ModulePatterns/#/)
11. [var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)
12. [JavaScript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI)
13. [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

0. Write a script that prints “JavaScript is amazing”:

You must create a constant variable called myVar with the value “JavaScript is amazing”
You must use console.log(...) to print all output
You are not allowed to use var
GitHub repository: alx-higher_level_programming
Directory: 0x12-javascript-warm_up
File: 0-javascript_is_amazing.js

1. Write a script that prints 3 lines:

The first line: “C is fun”
The second line: “Python is cool”
The third line: “JavaScript is amazing”
You must use console.log(...) to print all output
You are not allowed to use var
Directory: 0x12-javascript-warm_up
File: 1-multi_languages.js

2. Write a script that prints a message depending of the number of arguments passed:

If no arguments are passed to the script, print “No argument”
If only one argument is passed to the script, print “Argument found”
Otherwise, print “Arguments found”
You must use console.log(...) to print all output
You are not allowed to use var
Reference:[process.argv](https://nodejs.org/api/process.html#process_process_argv)

Directory: 0x12-javascript-warm_up
File: 2-arguments.js

3. Write a script that prints the first argument passed to it:

If no arguments are passed to the script, print “No argument”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use length
Directory: 0x12-javascript-warm_up
File: 3-value_argument.js

4. Write a script that prints two arguments passed to it, in the following format: “ is ”

You must use console.log(...) to print all output
You are not allowed to use var
Directory: 0x12-javascript-warm_up
File: 4-concat.js

5. Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:

If the argument can’t be converted to an integer, print “Not a number”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use try/catch
Directory: 0x12-javascript-warm_up
File: 5-to_integer.js

6. Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

The first line: “C is fun”
The second line: “Python is cool”
The third line: “JavaScript is amazing”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use any if/else statement
You can use only one console.log
You must use a loop (while, for, etc.)
Directory: 0x12-javascript-warm_up
File: 6-multi_languages_loop.js

7. Write a script that prints x times “C is fun”

Where x is the first argument of the script
If the first argument can’t be converted to an integer, print “Missing number of occurrences”
You must use console.log(...) to print all output
You are not allowed to use var
You can use only two console.log
You must use a loop (while, for, etc.)
Directory: 0x12-javascript-warm_up
File: 7-multi_c.js

8. Write a script that prints a square

The first argument is the size of the square
If the first argument can’t be converted to an integer, print “Missing size”
You must use the character X to print the square
You must use console.log(...) to print all output
You are not allowed to use var
You must use a loop (while, for, etc.)
Directory: 0x12-javascript-warm_up
File: 8-square.js

9. Write a script that prints the addition of 2 integers

The first argument is the first integer
The second argument is the second integer
You have to define a function with this prototype: function add(a, b)
You must use console.log(...) to print all output
You are not allowed to use var
Directory: 0x12-javascript-warm_up
File: 9-add.js

10. Write a script that computes and prints a factorial

The first argument is integer (argument can be cast as integer) used for computing the factorial
Factorial of NaN is 1
You must do it recursively
You must use a function
You must use console.log(...) to print all output
You are not allowed to use var
Directory: 0x12-javascript-warm_up
File: 10-factorial.js

11. Write a script that searches the second biggest integer in the list of arguments.

You can assume all arguments can be converted to integer
If no argument passed, print 0
If the number of arguments is 1, print 0
You must use console.log(...) to print all output
You are not allowed to use var
Directory: 0x12-javascript-warm_up
File: 11-second_biggest.js

12. Update this script to replace the value 12 with 89:

You are not allowed to use var
```
guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$ 
```
Directory: 0x12-javascript-warm_up
File: 12-object.js

13. Write a function that returns the addition of 2 integers.

The function must be visible from outside
The name of the function must be add
You are not allowed to use var
[Tip](https://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html)
Directory: 0x12-javascript-warm_up
File: 13-add.js

14. Write a file that modifies the value of myVar to 333
```
guillaume@ubuntu:~/0x12$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
guillaume@ubuntu:~/0x12$ ./100-main.js
333
guillaume@ubuntu:~/0x12$ 
```
Directory: 0x12-javascript-warm_up
File: 100-let_me_const.js

15. Write a function that executes x times a function.

The function must be visible from outside
Prototype: function (x, theFunction)
You are not allowed to use var
Directory: 0x12-javascript-warm_up
File: 101-call_me_moby.js

16. Write a function that increments and calls a function.

The function must be visible from outside
Prototype: function (number, theFunction)
You are not allowed to use var
Directory: 0x12-javascript-warm_up
File: 102-add_me_maybe.js

17. Update this script by adding a new function incr that increments the integer value.

You are not allowed to use var
```
guillaume@ubuntu:~/0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
guillaume@ubuntu:~/0x12$ 
```
Directory: 0x12-javascript-warm_up
File: 103-object_fct.js