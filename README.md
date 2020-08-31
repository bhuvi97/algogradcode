# algogradcod
This is a simple algo code of my grad assignment.

The problem which I'm trying to solve is rod cutting problem. The rod cutting problem has been solved in three approaches 
    1) Recursive
    2) Memoized recursive
    3) Dynamic programing

A trial is conducted for 30 times and an average is recorded. A report with the detailed analysis can be found above.

Description: This report is the analysis of the rod cutting problem which is solved in three ways namely recursive, memoized recursive, and dynamic programming. Rod cutting problem is “You are given a rod of size n >0, it can be cut into any number of pieces k (k ≤ n). Price for each piece of size i is represented as p(i) and maximum revenue from a rod of size i is r(i) (could be split into multiple pieces). Find r(n) for the rod of size n” (source: Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein. 2009. Introduction to Algorithms, Third Edition (3rd. ed.). The MIT Press). The algorithms have been coded in python. The detailed analysis of the algorithms can be seen below.

Analysis: The algorithms were implemented as three functions that take an array of prices and the length of the rod.  To minimize the dependencies such as RAM usage, a trial is run for 30 times, and an average is calculated. On average for n=20 the time taken by the recursive method is 0.6sec and dynamic programming and memoized recursive methods are in order of 10e-4 sec. As we know that the time complexity in the recursive method is 2n at n = 20 we got average time is 0.5949 sec. Now let’s see the time taken for n = 21. As per time complexity, we expect it to run in 1.18 to 1.2 seconds. Let’s see how long it takes? At n = 21 the time it took is 1.1822 sec. Let’s see the relative error in our prediction. After calculation, the error is 0.55%. Let’s make a table and see the error as well as times.

The time taken to run an algorithm depends on the input too. For instance [1, 3, 5, 7] takes more time than the input [1, 2, 3, 4]. The time taken by dynamic programming is an order of 10e-4 at n = 21. Now we will make a comparison between the running time of Dynamic programming and Memoized recursive. Let’s take certain inputs and create a table for various input sizes.


The current code is running on a system that contains ubuntu 16.04 and a RAM of 4GB. The question is will RAM affect the running time? Yes it does the same code has been run in a system of Windows 10 and RAM of 16 GB the time taken by the program to run is 0.53 sec. If we run the same program using the parallel pool the time taken in the recursive method will not change since it has reference to the previous value in which the things cannot be parallelized. 

As we are aware that the complexity of Dynamic programming is O(n2) and if we compare the running time for n = 100 and n = 200 we have doubled the input we expect the time taken is increased by 4 times and we could see that the time has increased by 3.77 times and for n = 400, time fold has increased by 3.86 times. This gives clear support to the assertion.

In the memoized recursion we could see the change factor for n = 100 to n = 200 is 3.70 and for n = 200 to n = 400 is 3.91 I guess that the complexity is the same in both cases I.e. O(n2). But the question is why does memoized recursion take more time compared to dynamic programming? Generally, memoization is also slower than tabulation because of the large recursive calls which is the reason for Dynamic programming to take less time even with the same complexity.

To conclude, the running time of the algorithm depends on the various factors like input type, RAM, processor, and clock speed. The order of complexity of the algorithms from lowest to highest is Dynamic programming, Memoized recursive, and Recursive.

