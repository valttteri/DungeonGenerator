## Weekly report 1

This week I started planning my project. I carefully read through the course material and did some research online in order to find a proper topic. 
I ended up with dungeon generation because the methods behind randomly generated environment is interesting to me. 
As of right now I have written very little code because I need to do more research before I can start really building my project. 

I learnt a lot of new things this week because I knew nothing about randomly generated dungeons beforehand. I read about some techniques other people have used to create dungeons.
Most people seem to start by generating the rooms and follow up with generating the hallways that connect the rooms. I will now describe the method I chose for generating a dungeon.
It might change a little along the way but this is my plan right now. First an area for the dungeon is created. Then an algorithm starts placing rooms on the area in a way that they don't overlap.
After a specific number of rooms are created the algorithm stops. Then I will use Bowyer-Watson algorithm to form a triangulation that connects the rooms. I'll use Prim's algorithm to turn the 
triangulation into a minimum spanning tree. Then I'll return a few edges in order to have alternate routes between the rooms. Lastly I will do some optimization.

I think getting started and finding a topic have been the most difficult things this week. For me getting started is usually the hardest part.
Next I will start researching triangulation with Bowyer-Watson algorithm and then I'll try to implement it in code. I have worked for about 6 hours this week.
