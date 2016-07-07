from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = ['gcodeLexer']

class gcodeLexer(RegexLexer):
    name = 'g-code'
    aliases = ['gcode']
    filenames = ['*.gcode']
    
    tokens = {
        'root': [
            (r'^;.*$', Comment),
            (r'\s;.*', Comment.Multiline, 'blockcomment'),
            (r'^[gmGM]\d{1,4}\s',Name.Builtin), # M or G commands
            (r'([^gGmM])([+-]?\d*[.]?\d+)', bygroups(Keyword,Number)),
            (r'\s', Text.Whitespace),
            (r'.*\n', Text),
        ],
        'blockcomment': [
            (r'.*;.*$', Comment.Multiline, '#pop'),
            (r'^.*\n', Comment.Multiline),
            (r'.', Comment.Multiline),
        ]
    }
    
