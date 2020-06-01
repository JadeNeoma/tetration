# Tetration
So this is just a simple python script that calculates y = <sup>x</sup>K.
This is done in a way that isn't packaged but can be easily imported into other projects. Tetration.py is safe to import, it can also be run from the commandline with the arguments x and k respectively, or it can just be run in which case it will prompt for x and k within the program.  

## Use
### Imported:
* tetration.calc(x, k) is the same as tetration.calc_y(x, k)
* tetration.calc_y(x, k) returns y
* tetration.calc_x(y, k) returns x, tests between -5 and 5, excl. 0, returns None if not found

### Run from console:
* Self-Explanatory, option 1 tests between -5 and 5 excl. 0

### Run from Command Line:
* takes two required arguments
* defaults to calculating y assuming the required arguments are x and n respectively
* can be forced to find x by ending with -x
* can be forced to find y by ending with -y, included for completeness

## Warning
1. I haven't included a timeout, if you enter numbers to big for your computer to handle it will hang.
2. x can be any integers apart from 0, beware negative numbers could result in complex results.
3. k can be any integer greater than 0
