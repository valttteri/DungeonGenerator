## Weekly report 4

This week I completed the first version of my project. I coded a class for hallways and a function which plots them into the dungeon.
This turned out to be easier than I expected. If the edge between two rooms is less than 20 pixels from being vertical/horizontal,
the program plots a straight hallway between them. Otherwise an L-shaped hallway will be plotted. I also fixed my tests and tried to
improve them. There is definitely room for improvement and I'll work on that later.

Since the program now plots hallways, every important component of my project can be found in the source code. This doesn't mean that
my work is done. Next step is optimization. The most essential things to optimize are room and hallway generation. I need to make the rooms 
spawn in a way that they don't overlap. As far as I know there are some algorithms to make this work but I'm not sure how I'm going to do this.
What comes to hallways they should not go throught rooms. I think this can be done with some simple calculations.

My tasks for next week are improving the tests and optimizing the code. I have worked for about 15 hours this week.

