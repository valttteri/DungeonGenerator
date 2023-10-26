## User manual

1. Clone the repository
```
~/ $ git clone https://github.com/valttteri/Tiralabra.git
~/ $ cd Tiralabra 
```
2. Download the required modules
```
~/Tiralabra/ $ pip install -r requirements.txt
```
3. Navigate to the root and run the program
```
~/Tiralabra/ $ cd src
~/src/ $ python app.py
```
The program will ask you to enter values for height, width and room count. There are limits displayed and if an invalid input is entered, the program asks for a new one.
Once a valid input is entered, a pygame window opens and the dungeon generation begins. Controls:
- Press 1 to generate a new dungeon with the same input
- Press 2 to enter a new input
- Press 3 to quit

Remember to click the pygame window or pressing a key won't register. The controls above should also be printed to console. If they are not, you can
force this by either setting ```PYTHONUNBUFFERED``` environment variable to equal true
```
~/src/ $ export PYTHONUNBUFFERED=true
~/src/ $ python app.py
```
or run the program as follows
```
~/src/ $ python -u app.py
```
