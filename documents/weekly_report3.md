## Weekly report 3 

My main goal for this week was to implement Prim's algorithm. This took me two sessions and
was more difficult than I expected. During the first session I coded a rough version of the algorithm 
which returned a minimum spanning tree as an array of nodes. That was a problem because I needed edges.
The nodes were in the correct order but they were impossible to plot correctly. During the second session 
I modified the algorithm and now it returns an array of edges.

Once I got the Prim's algorithm going I coded a little function that returns some of the edges removed
by the algorithm. That way I can generate alternate paths into my dungeon. I also created a
class for the rooms. I have been using a 800px by
400px display while working on my project. About 10-15 rooms seems to be the optimal amount for a 
display of that size. 

I wrote more tests for the program and then I did a lot of refactoring as most of my source code
was still in the same file. My tests covered about 90% of my main file before the refactoring. I should 
have done the refactoring before writing more tests because right now
**my tests are broken because of the refactoring**. Unfortunately I have no time to fix them until this week's
deadline. I will do that next week.

At the moment my program connects an array of nodes with a Delaunay triangulation. Then it
turns the triangulation into a minimum spanning tree. After that it returns some edges into the
tree and plots rooms on top of the nodes.

Next I will fix my tests and then keep working on the project. I'll optimize the room generation
in a way that rooms can't spawn on top of each other. Then I'll start
working on the last major part of my program which is hallway generation. I have worked for around 16 hours this week.
