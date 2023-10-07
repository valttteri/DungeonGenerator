## Implementation document/toteutusdokumentti

#### General structure

My project consists of three main parts: app.py file which runs the program, algorithm implementations and helpful tools.
The height and width of the dungeon and the number of rooms to be generated are given to the program by user. If the 
input is invalid the user gets notified and has to give another input. Once a valid input is given, the program gives
Bowyer-Watson's algorithm a bunch of coordinates that get turned into a Delaunay's triangulation. Then Prim's algorithm 
turns it into a minimum spanning tree and finally rooms and hallways are generated.

#### Achieved time and space requirements

My implementations of Bowyer-Watson's and Prim's algorithms both run in O(n<sup>2</sup>) time

#### Shortcomings and suggestions for improvement

The biggest problem right now is hallways going through rooms. 

#### Usage of chatbots

I have not used ChatGPT or any other chatbot for my project.

#### Sources:

[Gorilla Sun article on dungeon generation](https://www.gorillasun.de/blog/bowyer-watson-algorithm-for-delaunay-triangulation/)\
[Gamedeveloper article on dungeon generation](https://www.gamedeveloper.com/programming/procedural-dungeon-generation-algorithm#close-modal)\
[Programiz article on Prim's algorithm](https://www.programiz.com/dsa/prim-algorithm)\
[FreeCodeCamp article on Prim's algorithm](https://www.freecodecamp.org/news/prims-algorithm-explained-with-pseudocode/)\
[StackOverFlow discussion about Bowyer-Watson's algorithm](https://stackoverflow.com/questions/58116412/a-bowyer-watson-delaunay-triangulation-i-implemented-doesnt-remove-the-triangle)\
[Wikipedia article on Bowyer-Watson's algorithm](https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm)
