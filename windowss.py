
from dragonfly import *;

import shared


# ------------------------ shortened stuff - -------------------
avaz = False

class WindowsKeyRule1(CompoundRule):
    spec = "woonj"
    extras = []

    def _process_recognition(self, node, extras):
        global avaz
        if avaz == False:
            Key("win:down").execute()
            Key("tab").execute()
            avaz = True
        else:
            Key("win:up").execute()
            avaz = False


class WindowsKeyRule3(CompoundRule):
    spec = "wanj"
    extras = []

    def _process_recognition(self, node, extras):
        Key("alt:down").execute()
        Key("tab").execute()


class WindowsKeyRule4(MappingRule):
    mapping = {
        "woonj": Mimic("list", "all", "windows")
    }
    extras = []


#
# class WindowsKeyRule2(CompoundRule):
#     spec = "winj <letterOrKeystroke>"
#     extras = [Alternative(children=[keystroke, letter], name='letterOrKeystroke')]
#
#     def _process_recognition(self, node, extras):
#         Key("win:down").execute()
#         ksr = extras["letterOrKeystroke"]
#         ksr.execute()
#         Key("win:up").execute()




