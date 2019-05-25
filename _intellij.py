from dragonfly import *

import shared


class IntelijRule(MappingRule):
    mapping = {
        "zi fixi": Key("a-enter/2"),
        "zi format": Key("ac-l"),
        "zi terminal": Key("a-f12"),
        "zi callgraph": Key("ac-h"),
        "zi type hierarchy": Key("c-h"),
        "zi resize": Key("ctrl:down"),
        "zi file": Key("c-p"),
        "zi project": Key("a-1"),
        "zi structure": Key("a-7"),
        "zi source control": Key("a-9"),
        "zi search everywhere": Key("cs-f"),
        "zi find everywhere": Key("cs-f"),
        "zi find": Key("c-f"),
        "zi search": Key("c-f"),
        "zi replace": Key("c-r"),
        "zi fold all": Key("cs-minus"),
        "zi go to": Key("ca-b"),
        "zi usage": Key("as-7"),
        "zi surround with": Key("ca-t"),
        "zi go in": Key("c-c")+Text("cd ")+Key("c-v")+Text(";ls")+Key("enter/2"),
        "zi list": Text("ls") + Key("enter"),
        "zi go up": Text("cd ..") +Text(";ls")+Key("enter/2"),
        "zi find process": Text("ps aux|grep "),
        "zi door": Key("cs-quote"),
        "zi comment": Key("c-slash"),
        "zi run": Key("home, s-end, c-c")+Mouse("(0.5, 0.9), middle")+Key("enter"),
        "always on top": Key("w-t")
    }



grammar = Grammar("intelijey")
grammar.add_rule(IntelijRule())
grammar.load()
print "_intellij loaded"

def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
