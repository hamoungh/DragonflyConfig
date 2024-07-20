from dragonfly import *

import shared



class IntelijRule(MappingRule):
    mapping = {
        "zi fixi": Key("a-enter/2"),
        "zi format": Key("ac-l/25"),
        "zi terminal": Key("a-f12"),
        "zi callgraph": Key("ac-h"),
        "zi type hierarchy": Key("c-h"),
        "zi resize": Key("ctrl:down "),
        "zi file": Key("cs-n"),
        "zi project": Key("a-1"),
        "zi structure": Key("a-7"),
        "zi source control": Key("a-9"),
        "zi search everywhere": Key("cs-f"),
        "zi find everywhere": Key("cs-f"),
        "zi find": Key("c-f"),
        "zi search": Key("c-f"),
        "zi replace": Key("c-r"),
        "zi replace everywhere": Key("cs-r"),
        "zi fold all": Key("cs-minus"),
        "zi go to": Key("ac-b/25:1/25"),
        "zi usage": Key("as-7"),
        "zi surround with": Key("ca-t"),
        "zi go in": Key("c-c/25")+Pause("40")+Text("cd ")+Pause("40")+Key("c-v/25")+Text(";ls")+Pause("40")+Key("enter/2"),
        "zi list": Text("ls") + Key("enter"),
        "zi go up": Text("cd ..") +Text(";ls")+Key("enter/2"),
        "zi find process": Text("ps aux|grep "),
        "zi comment": Key("c-slash"),
        "zi run": Key("home/25, s-end/25, c-c/25")+Pause("20")+Key("a-f12")+Pause("20")+Key("c-v/25")+Pause("20")+Key("enter"),
        "zi command": Key("cs-p"),
        "zi imports": Key("ca-o"),
        "zi exe": Key("as-e"),
        "always on top": Key("w-t")
    }


grammar = Grammar("intelijey")
grammar.add_rule(IntelijRule())
grammar.load()
grammar.disable() 


def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
