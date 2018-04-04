from dragonfly import RuleRef, Repetition, CompoundRule, Dictation, IntegerRef, Grammar, MappingRule, Key

import windowss
import shared

import keystroke
import letterRule



shared.letter = RuleRef(rule=letterRule.LetterRule(), name='letter')
shared.keystroke = RuleRef(rule=keystroke.KeystrokeRule(), name='keystroke')
shared.letter_sequence = Repetition(shared.letter, min=1, max=32, name='letter_sequence')
import repeatt

# def executeLetter(letter):
#     letter.execute()
#
#
# def executeLetterSequence(letter_sequence):
#     for letter in letter_sequence:
#         letter.execute()

# ---------------------------------------------------------------------------
# NormalMode
class VimKeystrokeRule(MappingRule):
    exported = False

    mapping = {
        "bala [<n>]": Key("k:%(n)d"),
        "poiin [<n>]": Key("j:%(n)d"),
        "chap [<n>]": Key("h:%(n)d"),
        "ross [<n>]": Key("l:%(n)d"),
    }
    extras = [
        shared.letter,
        shared.letter_sequence,
        IntegerRef("n", 1, 100),
        Dictation("text"),
        Dictation("text2"),
    ]
    defaults = {
        "n": 1,
    }

class NormalEnabler(CompoundRule):
    spec = "vim"

    def _process_recognition(self, node, extras):
        # vimGrammar.disable()
        print "vim enabled"


class VimEnabler(CompoundRule):
    spec = "vim"

    def _process_recognition(self, node, extras):
        # normalGrammar.disable()
        # vimGrammar.enable()
        print "vim disabled"

#vimGrammar = Grammar("vim grammar")
#vimGrammar.add_rule(NormalEnabler())
# vimGrammar.load()



# not_gvim_context = ~AppContext(executable="vim" ) &  ~AppContext(title="vim")
# normalGrammar =  Grammar("normal grammar", context=not_gvim_context)
normalGrammar = Grammar("normal grammar")
normalGrammar.add_rule(repeatt.RepeatRule())
#normalGrammar.add_rule(shared.gvim_other_rule)
#normalGrammar.add_rule(shared.gvim_navigation_rule)
# normalGrammar.add_rule(WindowsKeyRule1())
#normalGrammar.add_rule(WindowsKeyRule2())

aa=windowss.WindowsKeyRule4()
normalGrammar.add_rule(aa)

normalGrammar.add_rule(windowss.IntelijFixIt())

# normalGrammar.add_rule(WindowsKeyRule3())

# normalGrammar.add_rule(InsertModeEnabler())
# normalGrammar.add_rule(InsertModeCommands())
# normalGrammar.add_rule(ExModeEnabler())
# normalGrammar.add_rule(KeystrokeRule())
# normalGrammar.add_rule(VimEnabler())
normalGrammar.load()
print "grammer loaded"


def unload():
    # global vimGrammar
    #  if vimGrammar: vimGrammar.unload()
    #  vimGrammar = None
    global normalGrammar
    if normalGrammar: normalGrammar.unload()
    normalGrammar = None
