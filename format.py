# ---------------------------- formating stuff ---------------------------
# Format: some_words
from dragonfly import MappingRule, Key, Mimic, IntegerRef, Dictation, RuleRef, Text, Function


def format_score(dictation):  # Function name must start with
    text = str(dictation)  # Get written-form of dictated text.
    words = [word.lower() for word in text.split(" ")];
    formatted_text = "_".join(words)  # Put underscores between words
    Text(formatted_text).execute()


# Format: Some Words
def format_title(dictation):
    text = str(dictation)
    words = [word.capitalize() for word in text.split(" ")]
    Text(" ".join(words)).execute()


def format_jake(dictation):
    text = str(dictation)
    words = [word.lower() for word in text.split(" ")]
    Text(" ".join(words)).execute()


# Format: SomeWords
def format_studley(dictation):
    text = str(dictation)
    words = [word.capitalize() for word in text.split(" ")]
    Text("".join(words)).execute()


# Format: somewords
def format_one_word(dictation):
    text = str(dictation)
    words = [word.lower() for word in text.split(" ")];
    Text("".join(words)).execute()  # Format: somewords


# Format: SOMEWORDS
def format_upper_one_word(dictation):
    text = str(dictation)
    words = [word.upper() for word in text.split(" ")]
    Text("".join(words)).execute()


def format_dotword(dictation):
    text = str(dictation)
    words = [word.lower() for word in text.split(" ")];
    Text(".".join(words)).execute()


def format_upper_score(dictation):
    text = str(dictation)
    words = [word.upper() for word in text.split(" ")]
    print words
    Text("_".join(words)).execute()


def format_jive(dictation):
    text = str(dictation)
    words = [word.lower() for word in text.split(" ")];
    Text("-".join(words)).execute()


# Format: someWords
def format_java_method(dictation):
    text = str(dictation)
    words = text.split(" ")
    print words[0].lower()
    Text(words[0].lower() + "".join(w.capitalize() for w in words[1:])).execute()


# _ - ' ' '' '.'
# score hyphen jout nothing dot
# z h j n d

# ac_bc Ac_Bc AC_BC    ac_Bc
# kochik title bozorg camel
# k t b c
class FormatRule(MappingRule):
    mapping = {
        "zake <dictation>": Function(format_score),  # some_other_words
        "say <dictation>": Function(format_jake),  # some of the words
        "hake <dictation>": Function(format_jive),  # some-other-words
        "dake <dictation>": Function(format_dotword),  # some.other.words
        "jait <dictation>": Function(format_title),  # Some Of The Words
        "nate <dictation>": Function(format_studley),  # SomeOfTheWords
        "nake  <dictation>": Function(format_one_word),  # someotherwords
        "nabe <dictation>": Function(format_upper_one_word),  # SOMEOTHERWORDS
        "zabe <dictation>": Function(format_upper_score),  # SOME_OTHER_WORDS
        "nace <dictation>": Function(format_java_method)  # someOtherWords
    }
    extras = [Dictation("dictation")]


