from dragonfly import RuleRef, Repetition, Grammar, MappingRule, Function
import logging

from keystroke import KeystrokeRule
from letterRule import LetterRule
from windowss import WindowsKeyRule4

import shared
import _intellij
import _vscode

from repeatt import RepeatRule

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("dragonfly.ide_context")

shared.letter = RuleRef(rule=LetterRule(), name='letter')
shared.keystroke = RuleRef(rule=KeystrokeRule(), name='keystroke')
shared.letter_sequence = Repetition(shared.letter, min=1, max=32, name='letter_sequence')

class IDEContext(MappingRule):
    def __init__(self):
        self.current_context = "vscode"  # Default to IntelliJ
        logger.info(f"IDEContext initialized. Current context: {self.current_context}")
        
        mapping = {
            "use intellij": Function(lambda: self.switch_context("intellij")),
            "use visual studio": Function(lambda: self.switch_context("vscode")),
        }
        
        super(IDEContext, self).__init__(mapping=mapping)

    def switch_context(self, context):
        logger.info(f"Attempting to switch context from {self.current_context} to {context}")
        
        if context == self.current_context:
            logger.info(f"Already in {context} context. No switch necessary.")
            return

        if context == "intellij":
            _vscode.grammar.disable()
            _intellij.grammar.enable()
            logger.info("Disabled VS Code grammar and enabled IntelliJ grammar")
        elif context == "vscode":
            _intellij.grammar.disable()
            _vscode.grammar.enable()
            logger.info("Disabled IntelliJ grammar and enabled VS Code grammar")
        else:
            logger.warning(f"Unknown context: {context}. No switch performed.")
            return

        self.current_context = context
        logger.info(f"Successfully switched to {context} context")
        print(f"Switched to {context} context")  # This will be visible in the Dragonfly window

normalGrammar = Grammar("normal grammar")
normalGrammar.add_rule(IDEContext())
normalGrammar.add_rule(RepeatRule())
normalGrammar.add_rule(WindowsKeyRule4())

normalGrammar.load()
logger.info("Grammar loaded")
print("Grammar loaded")

def unload():
    global normalGrammar
    if normalGrammar: 
        normalGrammar.unload()
        logger.info("Grammar unloaded")
    normalGrammar = None