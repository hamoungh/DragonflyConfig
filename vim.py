from dragonfly import Key, MappingRule, Dictation, IntegerRef, Text, CompoundRule, Grammar

import repeatt

gvim_other_rule = MappingRule(
    name="gvim_tabulators",
    mapping={
        # window navigation commands
        "window left": Key("c-w,h"),
        "window right": Key("c-w,l"),
        "window up": Key("c-w,k"),
        "window down": Key("c-w,j"),

        # window creation commands
        "window split": Key("c-w,s"),
        "window vertical split": Key("c-w,v"),
        # tabulator navigation commands
        "tabulator next": Key("g,t"),
        "tabulator previous": Key("g,T")

    },
    extras=[
    ]
)

gvim_navigation_rule = MappingRule(
    name="gvim_navigation",
    mapping={
        "go first line": Key("g,g"),
        "go last line": Key("G"),
        "go old": Key("c-o"),

        "cursor top": Key("s-h"),
        "cursor middle": Key("s-m"),
        "cursor (low | bottom)": Key("s-l"),

        # line navigation
        "go <line>": Key("colon") + Text("%(line)s\n"),

        # searching
        "search <text>": Key("slash") + Text("%(text)s\n"),
        "search this": Key("asterisk"),
        "back search <text>": Key("question") + Text("%(text)s\n"),

    },
    extras=[
        Dictation("text"),
        IntegerRef("n", 1, 50),
        IntegerRef("line", 1, 10000)
    ]
)


class NormalEnabler(CompoundRule):
    spec = "vim"
    def _process_recognition(self, node, extras):
        vimGrammar.disable()
        print "vim enabled"



vimGrammar = Grammar("vim grammar")
vimGrammar.add_rule(NormalEnabler())
vimGrammar.load()

