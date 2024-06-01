#importing value fundtion from bank.py
from bank import value



#defining the test function
def test_value():
     assert value("Hello") == 0
     assert value("hello") == 0
     assert value(" HELLO") == 0

     assert value("How are you?") == 20
     assert value("hey") == 20
     assert value("HEY") == 20

     assert value("what's happening?") == 100
     assert value("What's up ?") == 100
