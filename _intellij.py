from dragonfly import *

import shared


class IntelijRule(MappingRule):
    mapping = {
        "zi fixi": Key("a-enter/2"),
        "zi format": Key("ac-l"),
        "zi terminal": Key("a-f12"),
        "zi callgraph": Key("ac-h"),
        "zi resize": Key("ctrl:down"),
        "zi go to file": Key("c-p"),
        "zi version control": Key("a-9"),
        "zi search everywhere": Key("cs-f"),
        "zi replace": Key("c-r")
    }


grammar = Grammar("intelijey")
grammar.add_rule(IntelijRule())
grammar.load()
print "_intellij loaded"


def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
