## Weekly report 2

This week I worked on Bowyer-Watson algorithm which is one of the key components of my project. First I plotted some individual
triangles and their circumcircles as this is something that happens a lot in Bowyer-Watson algorithm. After that I started implementing
the algorithm into my project. I found a handy [website](https://www.gorillasun.de/blog/bowyer-watson-algorithm-for-delaunay-triangulation/)
where each part of the algorithm was thoroughly explained. That helped a lot with the coding.
Right now the algorithm is ready. I realized that if multiple nodes end up forming an approximately straight line, the algorithm return an 
empty triangulation. This is a major problem with small inputs. I will try to get rid of this problem later.

I also wrote tests for my project. I used python's unittest module for running the tests and the coverage module for generating a test report.
I created a repository for setting up a Github page where my report can be observed. At first I attempted this with codecov but I couldn't get it to work.
Getting unittest and coverage to work caused some major headache. First VSCode didn't recognize my test file and then
the program kept throwing a ModuleNotFoundError at me. In the end I managed to get everything to work and now my test report is linked in the README file.

Next I'll start working on room generation. First I'll implement Prim's algorithm in order to remove edges from a triangulation and then 
I'll try to figure out how to generate some rooms in a way that they don't overlap. I have worked for about 15 hours this week.
