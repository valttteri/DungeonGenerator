## Weekly report 5

This week I optimized my code, wrote some tests and made the program more user-friendly. I found a simple solution to a problem I had where rooms
would overlap. If one of two rooms is either on the left side or above the other room, they do not overlap. This requires no more than four calculations.
Very easy. Hallways clipping through rooms is still a thing in my program but techincally it's not that big of a problem. It only creates more alternate 
routes into the dungeon which is basically a useful feature.

Now a user can give inputs to the program. User can decide the width and height of the display and number of rooms to be generated. I made some
conditions where it's not possible to give impossible inputs. If that happens, the user gets a notification and has to enter a new input.

Next I'll write more tests and continue optimizing the code.
