INTERESTING_TYPES = ["dict", "list"]
PRETTY_TYPE_NAMES = {
  "dict": "dictionary",
  "list": "list",
  "str": "string",
  "int": "number",
  "float": "number"
}
PLURAL_TYPE_NAMES = {
  "dict": "dictionaries",
  "list": "lists",
  "str": "strings",
  "int": "numbers",
  "float": "number"
}

def TypeExplorer(typ, name = "", depth = 0, indent = 4, parent = None):
  base = BaseTypeExplorer(typ)
  if base.type_name() == "dict":
    return DictionaryExplorer(typ, name, depth, indent, parent)
  elif base.type_name() == "list":
    return ListExplorer(typ, name, depth, indent, parent)
  else:
    return BaseTypeExplorer(typ, name, depth, indent, parent)

class BaseTypeExplorer:
  def __init__(self, typ, name = "", depth = 0, indent = 4, parent = None):
    self.typ = typ
    self.name = name
    self.depth = depth
    self.indent = indent
    self.parent = parent
    self.interesting = []
    self.boring = []

  def type_name(self, typ = None):
    return str(type(typ or self.typ)).split("'")[1]

  def pretty_name(self, typ = None):
    name = self.type_name(typ)
    if name in PRETTY_TYPE_NAMES:
      return PRETTY_TYPE_NAMES[name]
    else:
      return name

  def plural_name(self, typ = None):
    name = self.type_name(typ)
    if name in PLURAL_TYPE_NAMES:
      return PLURAL_TYPE_NAMES[name]
    else:
      return "{}s".format(name)

  def __str__(self):
    suffix = ""
    if len(self.name) > 0:
      suffix = " called {}".format(self.name)
    type_str = "A {}{}".format(self.pretty_name(), suffix)
    return "{}{}".format(self.indent_str(), type_str)

  def indent_str(self, depth = None):
    indent_str = ""
    for i in range(0, (depth or self.depth) * self.indent):
      indent_str += " "
    return indent_str

  def is_interesting(self):
    return self.type_name() in INTERESTING_TYPES

class InterestingTypeExplorer(BaseTypeExplorer):
  def __init__(self, typ, name = "", depth = 0, indent = 4, parent = None):
    BaseTypeExplorer.__init__(self, typ, name, depth, indent, parent)
    self.explore()

  def explore():
    raise Exception('#explore must be implements in a subclass')

  def unique_boring_type_pretty_names(self):
    result = set()
    for type_explorer in self.boring:
      result.add(type_explorer.plural_name())
    return list(result)

  def unique_boring_type_pretty_names_to_sentence(self):
    pretty_names = self.unique_boring_type_pretty_names()
    if len(pretty_names) == 0:
      return "<None>"
    elif len(pretty_names) == 1:
      return pretty_names[0]
    else:
      return ", ".join(pretty_names[0:len(pretty_names) - 1]) + " and " + pretty_names[len(pretty_names) - 1]


class DictionaryExplorer(InterestingTypeExplorer):
  def explore(self):
    for key, val in self.typ.iteritems():
      type_explorer = TypeExplorer(val, key, self.depth + 1, self.indent, self)
      if type_explorer.is_interesting():
        self.interesting.append(type_explorer)
      else:
        self.boring.append(type_explorer)

  def __str__(self):
    type_str = "{}".format(self.name).strip()
    result = []
    result.append("{}{} {{".format(self.indent_str(), type_str))
    for type_explorer in self.interesting:
      result.append(str(type_explorer))
    if len(self.boring) > 0:
      prefix = "Some"
      if len(self.interesting) > 0:
        prefix = "And some"
      result.append("{}{} keys holding {}".format(self.indent_str(self.depth + 1), prefix, self.unique_boring_type_pretty_names_to_sentence()))
    result.append("{}}}".format(self.indent_str()))
    return "\n".join(result)


class ListExplorer(InterestingTypeExplorer):
  def explore(self):
    for item in self.typ:
      type_explorer = TypeExplorer(item, None, self.depth + 1, self.indent, self)
      if type_explorer.is_interesting():
        self.interesting.append(type_explorer)
      else:
        self.boring.append(type_explorer)

  def __str__(self):
    result = []
    type_str = "{}".format(self.name).strip()
    result.append("{}{} [".format(self.indent_str(), type_str))
    for type_explorer in self.interesting:
      result.append(str(type_explorer))
    if len(self.boring) > 0:
      prefix = "A"
      if len(self.interesting) > 0:
        prefix = "And a"
      result.append("{}{} list of {}".format(self.indent_str(self.depth + 1), prefix, self.unique_boring_type_pretty_names_to_sentence()))
    result.append("{}]".format(self.indent_str()))
    return "\n".join(result)





