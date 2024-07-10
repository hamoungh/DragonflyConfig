from dragonfly import RuleRef, Repetition, CompoundRule, Dictation, IntegerRef, Grammar, MappingRule, Key

from keystroke import KeystrokeRule
from letterRule import LetterRule
from windowss import WindowsKeyRule4

import shared



shared.letter = RuleRef(rule=LetterRule(), name='letter')
shared.keystroke = RuleRef(rule=KeystrokeRule(), name='keystroke')
shared.letter_sequence = Repetition(shared.letter, min=1, max=32, name='letter_sequence')

from repeatt import RepeatRule


normalGrammar = Grammar("normal grammar")
normalGrammar.add_rule(RepeatRule())
normalGrammar.add_rule(WindowsKeyRule4())
normalGrammar.load()


def unload():
    global normalGrammar
    if normalGrammar: normalGrammar.unload()
    normalGrammar = None
