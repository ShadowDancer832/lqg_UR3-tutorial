from std_msgs.msg import Int64
from python_bindings_tutorial import AddTwoInts

a = Int64(42)
b = Int64(21)
addtwoints = AddTwoInts()
sum = addtwoints.add(a, b)
print(sum)