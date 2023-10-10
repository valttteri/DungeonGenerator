## Testing document/testausdokumentti

[Test coverage report](https://valttteri.github.io/)

I have tested my implementations of Bowyer-Watson's and Prim's algorithms, tools.py file and my Triangle class.
I made the tests and the testing report with Unittest and Coverage. All of my tests are
in the directory called 'tests'. I also have a file named 'dungeon_testing.py' which is an unofficial testing
environment.

File test_tools.py tests the functions from file tools.py. The tests are done with a couple of
different inputs. The algorithm tests run 500 times each. They check if the algorithms return a data structure
of a valid size. These tests actually take the tools.py tests further as the algorithms use 
the functions found in that file.

The tests can be done by installing modules Unittest and Coverage and configuring VSCode's testing
window to include every file starting with "test_".
