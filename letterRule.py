from dragonfly import MappingRule, Key, Text


class LetterRule(MappingRule):
    exported = True
    mapping = {
        'ach': Key('a', static=True),
        'bik': Key('b', static=True),
        'kaj': Key('c', static=True),
        'daf': Key('d', static=True),
        'ish': Key('e', static=True),
        'fick': Key('f', static=True),
        'goeff': Key('g', static=True),
        'hash': Key('h', static=True),
        'jack': Key('j', static=True),
        'kif': Key('k', static=True),
        'laam': Key('l', static=True),
        'meem': Key('m', static=True),
        'noon': Key('n', static=True),
        'paf': Key('p', static=True),
        'queue': Key('q', static=True),  # queue
        'rij': Key('r', static=True),
        'saad': Key('s', static=True),
        'tenj': Key('t', static=True),
        'vazz': Key('v', static=True),
        'wek': Key('w', static=True),  # doubleu
        'ex': Key('x', static=True),  # ex
        'wise': Key('y', static=True),  # waay
        'zed': Key('z', static=True),
        'esh': Key('e', static=True),
        'you': Key('u', static=True),  # you
        'osh': Key('o', static=True),
        'ice': Key('i', static=True),

        'zero': Key('0'),
        'one': Key('1'),
        'two': Key('2'),
        'three': Key('3'),
        'four': Key('4'),
        'five': Key('5'),
        'six': Key('6'),
        'seven': Key('7'),
        'eight': Key('8'),
        'nine': Key('9'),

        'jet': Key('space'),
        'soot': Key("win:up, alt:up, escape"),

        'tab': Key('tab'),

        'amphi': Key('ampersand'),
        'quote': Key('apostrophe'),
        '[single] quote': Key('squote'),
        'saar': Key('asterisk'),
        'atsi': Key('at'),
        'bash': Key('backslash'),
        'tick': Key('backtick'),
        'bar': Key('bar'),
        'cart': Key('caret'),
        'colx': Key('colon'),
        'kooch': Key('comma'),
        'dollar': Key('dollar'),
        '(dot|period)': Key('dot'),
        'duote': Key('dquote'),
        'moss': Key('equal'),
        'bang': Key('exclamation'),
        'sharp': Key('hash'),
        'hyph': Key('hyphen'),
        'pers': Key('percent'),
        'pulse': Key('plus'),
        'kess': Key('question'),
        # Getting Invalid key name: 'semicolon'
        'semi': Text(";"),
        'sash': Key('slash'),

        'tilde': Key('tilde'),
        'zoor': Key('underscore'),
        # 'escape':Key('escape'),
        'langle': Key('langle'),
        'lace': Key('lbrace'),
        'lack': Key('lbracket'),
        'laip': Key('lparen'),
        'rangle': Key('rangle'),
        'race': Key('rbrace'),
        'rack': Key('rbracket'),
        'raip': Key('rparen'),
    }