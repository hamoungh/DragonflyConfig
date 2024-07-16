from dragonfly import *

class VSCodeRule(MappingRule):
    mapping = {
        "always on top": Key("w-t"),
        "pilot": Key("a-left"),
        "zi callgraph": Text("Not directly available in VS Code"),
        "zi command": Key("c-s-p"),
        "zi comment": Key("c-slash"),
        "zi exe": Key("c-f5"),
        "zi file": Key("c-p"),
        "zi find": Key("c-f"),
        "zi find everywhere": Key("c-s-f"),
        "zi find process": Text("Get-Process | Where-Object {$_.Name -like '*'} | Format-Table Name, Id, CPU"),
        "zi fixi": Key("c-dot"),
        "zi fold all": Key("c-k, c-0"),
        "zi format": Key("s-a-f"),
        "zi go in": Key("c-c/25") +Pause("20")+ Text("cd ") + Key("c-v/25") + Text(" && ls") + Key("enter/2"),
        "zi go to": Key("c-g"),
        "zi go up":  Text("cd .. && ls") + Key("enter/2"),
        "zi imports": Key("c-s-o"),
        "zi list":  Text("ls") + Key("enter"),
        "zi project": Key("c-b"),
        "zi replace": Key("c-h"),
        "zi replace everywhere": Key("c-s-h"),
        "zi resize": Key("c-backslash"),
        "zi run": Key("end, s-home, c-c/25") + Pause("20") + Key("c-backtick/25") + Pause("20") + Key("c-v/25") + Pause("20") + Key("enter"),
        "zi source control": Key("c-s-g"),
        "zi structure": Key("c-s-o"),
        "zi surround with": Key("c-k, c-s"),
        "zi terminal": Key("c-backtick"),
        "zi type hierarchy": Key("c-t"),
        "zi usage": Key("s-f12"),
    }

grammar = Grammar("vscode")
grammar.add_rule(VSCodeRule())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None