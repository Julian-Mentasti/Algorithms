# The Starcase Problem:
I saw this problem earlier today and I wanted to solve it, so why not. Here is my solution to the staircase problem: I have solved it through an iterator solution and I'm currently missing the bonus part. I plan to solve the extra part and make a recursive solution. Moreover, I tried my best to analyse the algorithm. I used Python because I have a workshop next week and I might as well practice a little bit.

## Task:
### You are given a staircase with n steps. You can only go up the stairs taking one or two steps at a time. Write the number of ways that describes how many ways it is possible to go from the bottom to the top. **Bonus:** Make a second function where you can also input X that is a list of the number of steps you can take at a time.

My first instict was to simplyfy it and then try to spot a pattern. So I manually computed the ways I could climb a stair case of two, three and four. 

<p align="center">
  <img src="https://i.imgur.com/u60wqeO.png" >
</p>
There are two distinct ways of going up the stairs:


- Taking a 1 step twice.
- Taking a 2 step once.  

<p align="center">
  <img src="https://i.imgur.com/j5smpQ6.png" >
</p>
There are three disticnt ways of going up the stars:

* Taking a 1 step three times.
* Taking a 2 step one time and then one 1 step one time.
* Taking a 1 step and then a 2 step one time. 

<p align="center">
  <img src="https://i.imgur.com/KCAIfTs.png" >
</p>
There are five disticnt ways of going up the stars:

* Taking a 1 step four times.
* Taking a 2 step twice. 
* Taking a 1 step, then a 2 step then a 1 step.
* Taking a 2 step then a 1 step twice.
* Taking a 1 step twice and then a 2 step.
