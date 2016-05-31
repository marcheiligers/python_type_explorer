from type_explorer import *
from type_printer import *

my_string = "my string"
print TypeExplorer(my_string)
print TypeExplorer(my_string, "my_string")
my_num = 12.3
print TypeExplorer(my_num)
print TypeExplorer(my_num, "my_num")
print TypeExplorer([1, 2, 3, 4], "mylist")

complex_type = TypeExplorer({ "a": 1, "b": { "key": "val" }, "c": [1, 2, 3, 4], "d": [1, "2", 3, 4] }, "data")
print StringTypePrinter(complex_type)
