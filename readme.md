About this small Project:  
Language used: Python  
IDE: VS code

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

```
    235

  +  52
    ----
```

Create the arithmetic_arranger function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Example:

```
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)should return:

    32      3801      45      123
 + 698    -    2    + 43    +  49
 -----    ------    ----    -----
   730      3799      88      172
```
