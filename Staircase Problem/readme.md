# The Staircase Problem:
I saw this problem earlier today and I wanted to solve it, so why not. Here is my solution to the staircase problem: I have solved it through an iterator solution and I'm currently missing the bonus part. I plan to solve the extra part and make a recursive solution. Moreover, I tried my best to analyse the algorithm. I used Python because I have a workshop next week and I might as well practice a little bit.

## Task:
### You are given a staircase with n steps. You can only go up the stairs taking one or two steps at a time. Write the number of ways that describes how many ways it is possible to go from the bottom to the top. **Bonus:** Make a second function where you can also input X that is a list of the number of steps you can take at a time.

My first instinct was to simplify it and then try to spot a pattern. So I manually computed the ways I could climb a stair case of two, three and four. 

<p align="center">
  <img src="https://i.imgur.com/u60wqeO.png" >
</p>
There are two distinct ways of going up the stairs of two steps:


- Taking a 1 step twice.
- Taking a 2 step once.  

<p align="center">
  <img src="https://i.imgur.com/j5smpQ6.png" >
</p>
There are three disticnt ways of going up the stars of three steps:

* Taking a 1 step three times.
* Taking a 2 step one time and then one 1 step one time.
* Taking a 1 step and then a 2 step one time. 

<p align="center">
  <img src="https://i.imgur.com/KCAIfTs.png" >
</p>
There are five disticnt ways of going up the stars of four steps:

* Taking a 1 step four times.
* Taking a 2 step twice. 
* Taking a 1 step, then a 2 step then a 1 step.
* Taking a 2 step then a 1 step twice.
* Taking a 1 step twice and then a 2 step.

At this point I realized that the question was basically asking the number of ways we can make n from combinations of 1 and 2. For example if we try to make 4 we have five different ways. Two come from using only 1's and the other from only 2's but then there are three ways that come from the distinct arrangements of (1, 1, 2).  

I can do this by using factorials: 
Using the following formula I can find how many ways I can arrange an arbitrary number of 1s and 2s.

<p align="center">
  <img src="https://i.imgur.com/icbSrEU.png" >
</p>


if we use n to equal five then there are a total of eight combinations of 1's and 2's to make five. 
* Taking a 1 step five times
* Taking a 1 set three times and a 2 step one time (A total of four combinations)
* Taking a 1 step one time and a 2 step two times. (A total of three combinations)
This can be done using the formula above. 

### So now it's time to write it in an algorithm:
```python
import math

def num_ways(n):
    head = 0
    counter = 0
    u = 0
    d = 0
    i = 0
    if (n == 0):
        return counter
    if (n%2 != 0):
        head = 1
    while (i*2-n-head != 0):
            u = (n - (2*i))
            d = i
            i += 1
            counter += math.factorial(u + d)/(math.factorial(u)*math.factorial(d))
    print(i * 2 - n - head)
    return counter + ((1 - head))
```
This algorithm uses the math.factorial function which is not very efficient. Theres a better and more efficient way to find the factorial of a function but I will make an enitrely new entry on it (soon...). I will do the algorithm analysis at a later date. However I have also found a recursive algorithm.

```python
def numWays(n): 
  if n = 1 return 1 
  else if n = 2 
    return 2 
  else return numWays(n-1) + numWays(n-2)
```
