## Implementation document/toteutusdokumentti

#### General structure

The project consists of four main parts: `app.py`, `bowyerwatson.py`, `prim.py` and a directory called `classes` containing `hallwayclass.py`, `roomclass.py` and `triangleclass.py`.
User can start the program by running `app.py`. Then they get to input parameters for the dungeon generation. The parameters are width, height and room count.
There are limits for the parameters and if an invalid input is given the program asks for a new one.

When the program receives a valid input, it generates a number of coordinates equal to the room count and gives them
to the Bowyer-Watson's algorithm located in `bowyerwatson.py`. The algorithm then forms a Delaunay triangulation based on the coordinates.
The triangle objects are defined in `triangleclass.py`. Room objects defined in `roomclass.py` are also generated at this point.

Next the Delaunay triangulation is turned into a minimum spanning tree by Prim's algorithm in `prim.py`. This eliminates possibility for alternate 
routes and therefore each removed edge has a 13% chance to be returned. Now the program has an array of edges needed for hallway generation.
It forms a graph with the edges and generates the hallways.

Finally the dungeon is plotted step by step in a Pygame window to show the process behind it. When the generation is finished, the user can either generate 
a new dungeon with the same parameters, give a new input or close the program.

#### Achieved time and space requirements

My implementations of Bowyer-Watson's and Prim's algorithms both run in O(n<sup>2</sup>) time. 

#### Shortcomings and suggestions for improvement

Having multiple room shapes would make the dungeon look cooler. The program would be more user friendly if instead of the console it was controlled with buttons on the Pygame window.

#### Usage of chatbots

I have not used ChatGPT or any other chatbot for my project.

#### Sources:

[Gorilla Sun article on dungeon generation](https://www.gorillasun.de/blog/bowyer-watson-algorithm-for-delaunay-triangulation/)\
[Gamedeveloper article on dungeon generation](https://www.gamedeveloper.com/programming/procedural-dungeon-generation-algorithm#close-modal)\
[Programiz article on Prim's algorithm](https://www.programiz.com/dsa/prim-algorithm)\
[FreeCodeCamp article on Prim's algorithm](https://www.freecodecamp.org/news/prims-algorithm-explained-with-pseudocode/)\
[StackOverFlow discussion about Bowyer-Watson's algorithm](https://stackoverflow.com/questions/58116412/a-bowyer-watson-delaunay-triangulation-i-implemented-doesnt-remove-the-triangle)\
[Wikipedia article on Bowyer-Watson's algorithm](https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm)
