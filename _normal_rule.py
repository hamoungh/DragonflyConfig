from dragonfly import RuleRef, Repetition, CompoundRule, Dictation, IntegerRef, Grammar, MappingRule, Key

from keystroke import KeystrokeRule
from letterRule import LetterRule
from windowss import WindowsKeyRule4

import shared





shared.letter = RuleRef(rule=LetterRule(), name='letter')
shared.keystroke = RuleRef(rule=KeystrokeRule(), name='keystroke')
shared.letter_sequence = Repetition(shared.letter, min=1, max=32, name='letter_sequence')

from repeatt import RepeatRule

# def executeLetter(letter):
#     letter.execute()
#
#
# def executeLetterSequence(letter_sequence):
#     for letter in letter_sequence:
#         letter.execute()

# ---------------------------------------------------------------------------
# NormalMode

# class IntellijEnabler(CompoundRule):
#     spec = "intelijey"
#     def _process_recognition(self, node, extras):
#         # normalGrammar.disable()
#         intellij.intelijGrammar.enable()
#         print "vim disabled"



#--
# class TerminalEnabler(CompoundRule):
#     spec = "terminal"
#     def _process_recognition(self, node, extras):
#         termi.grammar.enable()
#         print "vim disabled"
#
# nice terminal grammar = Grammar("terminal")
# grammar.add_rule(TerminalRule())
# grammar.load()
# print "terminal loaded"
#
# def unload():
#   global grammar
#   if grammar: grammar.unload()
#   grammar = None
#--
# normalGrammar.add_rule(TerminalEnabler())

# not_gvim_context = ~AppContext(executable="vim" ) &  ~AppContext(title="vim")
# normalGrammar =  Grammar("normal grammar", context=not_gvim_context)
normalGrammar = Grammar("normal grammar")
normalGrammar.add_rule(RepeatRule())
#normalGrammar.add_rule(shared.gvim_other_rule)
#normalGrammar.add_rule(shared.gvim_navigation_rule)
# normalGrammar.add_rule(WindowsKeyRule1())
#normalGrammar.add_rule(WindowsKeyRule2())

normalGrammar.add_rule(WindowsKeyRule4())



# normalGrammar.add_rule(WindowsKeyRule3())

# normalGrammar.add_rule(InsertModeEnabler())
# normalGrammar.add_rule(InsertModeCommands())
# normalGrammar.add_rule(ExModeEnabler())
# normalGrammar.add_rule(KeystrokeRule())

normalGrammar.load()
print "grammer loaded"


def unload():
    # global vimGrammar
    #  if vimGrammar: vimGrammar.unload()
    #  vimGrammar = None
    global normalGrammar
    if normalGrammar: normalGrammar.unload()
    normalGrammar = None
