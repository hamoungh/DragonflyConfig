
from dragonfly import MappingRule, Key, Mimic, IntegerRef, Dictation, RuleRef, Text, Mouse


class KeystrokeRule(MappingRule):
    release = Key("shift:up, ctrl:up")

    mapping = {
        "[<n>] up": Key("up/2:%(n)d"),
        "[<n>] down": Key("down/2:%(n)d"),
        "[<n>] left": Key("left/2:%(n)d"),
        "[<n>] right": Key("right/2:%(n)d"),
        "[<n>] pop": Key("pgup/2:%(n)d"),
        "[<n>] pen": Key("pgdown/2:%(n)d"),
        "<n> up (page | pages)": Key("pgup/2:%(n)d"),
        "<n> down (page | pages)": Key("pgdown/2:%(n)d"),
        "<n> left (word | words)": Key("c-left/2:%(n)d"),
        "<n> right (word | words)": Key("c-right/2:%(n)d"),
        "home": Key("home"),
        "end": Key("end"),
        "doc home": Key("c-home"),
        "doc end": Key("c-end"),
        "follow": Key("ctrl:down") + Mouse("left") + Key("ctrl:up"),

        #	"soot": 						Key("escape"),
        #	"[<n>] joot":                      release + Key("space/2:%(n)d"),
        "[<n>] slap": release + Key("enter/2:%(n)d"),
        "[<n>] tab": Key("tab/2:%(n)d"),
        "[<n>] dij": release + Key("del/2:%(n)d"),
        "ditch [<n> | this] (line|lines)": release + Key("home, s-down/2:%(n)d, del"),
        "[<n>] boot": release + Key("backspace/2:%(n)d"),
        "pop up": release + Key("apps"),

        "pinj": release + Key("c-v"),
        "duplicate <n>": release + Key("c-c, c-v:%(n)d"),
        "copy": release + Key("c-c"),
        "thatsy": release + Key("c-c"),
        "cut": release + Key("c-x"),
        "select all": release + Key("c-a"),
        #   "[hold] appsj":                     Key("apps:down"),
        #	"appsup":               d      Key("apps:up,"),
        "[hold] shi": Key("shift:down"),
        "shiffup": Key("shift:up"),
        "[hold] zoo": Key("ctrl:down"),
        "contup": Key("ctrl:up"),
        "[hold] az": Key("alt"),
        "altup": Key("alt:up"),
        "release [all]": release,
        "tux": Key("c-a"),
        "amplify": Key("c-plus"),

        #     "say <text>":                       release + Text("%(text)s"),
        "mimic <text>": release + Mimic(extra="text"),

        "efyek": Key("f1"),
        "efdouce": Key("f2"),
        "efse": Key("f3"),
        "efchar": Key("f4"),
        "efpanj": Key("f5"),
        "efshish": Key("f6"),
        "efhaf": Key("f7"),
        "efhash": Key("f8"),
        "efnoh": Key("f9"),
        "efdah": Key("f10"),
        "efyazdah": Key("f11"),
        "efdavazdah": Key("f12"),
        "efsizdah": Key("f13"),
        "efcharda": Key("f14"),
        "efpoonza": Key("f15"),
        "inteli jey": Text("intellij")


    }
    extras = [
        IntegerRef("n", 1, 100),
        Dictation("text"),
        Dictation("text2"),
    ]
    defaults = {
        "n": 1,
    }
