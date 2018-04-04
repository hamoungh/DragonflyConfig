from time import sleep

from dragonfly import *;  # CompoundRule,MappingRule,Key,IntegerRef,Grammer;

from format import FormatRule
import shared


# ------------------------- repeating formatting and keystrokes---------------------------------

alternatives = []
alternatives.append(shared.keystroke)
alternatives.append(RuleRef(rule=FormatRule()))
alternatives.append(shared.letter)
# alternatives.append(RuleRef(rule=VimKeystrokeRule()))

class RepeatRule(CompoundRule):
    single_action = Alternative(alternatives)
    sequence = Repetition(single_action, min=1, max=16, name="sequence")

    spec = "<sequence> [[[and] repeat [that]] <n> times]"
    extras = [
        sequence,  # Sequence of actions defined above.
        IntegerRef("n", 1, 100),  # Times to repeat the sequence.
    ]
    defaults = {
        "n": 1,  # Default repeat count.
    }

    def _process_recognition(self, node, extras):
        release = Key("shift:up, ctrl:up")
        sequence = extras["sequence"]  # A sequence of actions.
        count = extras["n"]  # An integer repeat count.
        for i in range(count):
            for action in sequence:
                action.execute()
            sleep(0.05)
        release.execute()

