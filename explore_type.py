def explore_type(obj, name = "", indent = 0, indent_spaces = 4):
  indent_str = ""
  for i in range(0, indent * indent_spaces):
    indent_str += " "

  type_name = str(type(obj)).split("'")[1]
  type_str = "{} <{}>".format(name, type_name).strip()
  if type_name == "dict":
    print "{}{} {{".format(indent_str, type_str)
    for key in obj:
      explore_type(obj[key], key, indent + 1, indent_spaces)
    print "{}}}".format(indent_str)
  else:
    print "{}{}".format(indent_str, type_str)


explore_type({ "a": 1, "b": { "key": "val" }, "c": [1, 2, 3, 4] })