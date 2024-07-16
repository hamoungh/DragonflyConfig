from dragonfly import *

import shared


class IntelijRule(MappingRule):
    mapping = {
        "always on top": Key("w-t"),
        "pilot": Key("c-i"),
        "zi callgraph": Key("ac-h"),
        "zi command": Key("cs-p"),
        "zi comment": Key("c-slash"),
        "zi exe": Key("as-e"),
        "zi file": Key("cs-n"),
        "zi find": Key("c-f"),
        "zi find everywhere": Key("cs-f"),
        "zi find process": Text("ps aux|grep "),
        "zi fixi": Key("a-enter/2"),
        "zi fold all": Key("cs-minus"),
        "zi format": Key("ac-l/25"),
        "zi go in": Key("c-c/25")+Pause("20")+Text("cd ")+Key("c-v/25")+Text(";ls")+Key("enter/2"),
        "zi go to": Key("ac-b/25:1/25"),
        "zi go up": Text("cd ..") +Text(";ls")+Key("enter/2"),
        "zi imports": Key("ca-o"),
        "zi list": Text("dir") + Key("enter"),
        "zi project": Key("a-1"),
        "zi replace": Key("c-r"),
        "zi replace everywhere": Key("cs-r"),
        "zi resize": Key("ctrl:down "),
        "zi run": Key("home/25, s-end/25, c-c/25")+Pause("20")+Key("a-f12")+Pause("20")+Key("c-v/25")+Pause("20")+Key("enter"),
        "zi search": Key("c-f"),
        "zi search everywhere": Key("cs-f"),
        "zi source control": Key("a-9"),
        "zi structure": Key("a-7"),
        "zi surround with": Key("ca-t"),
        "zi terminal": Key("a-f12"),
        "zi type hierarchy": Key("c-h"),
        "zi usage": Key("as-7"),
    }


grammar = Grammar("intelijey")
grammar.add_rule(IntelijRule())
grammar.load()
grammar.disable() 


def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None