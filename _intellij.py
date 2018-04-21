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
        "zi source control": Key("a-9"),
        "zi search everywhere": Key("cs-f"),
        "zi find everywhere": Key("cs-f"),
        "zi find": Key("c-f"),
        "zi search": Key("c-f"),
        "zi replace": Key("c-r"),
        "zi fold all": Key("cs-minus"),
        "zi go to": Key("ca-b")

    }



grammar = Grammar("intelijey")
grammar.add_rule(IntelijRule())
grammar.load()
print "_intellij loaded"

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
