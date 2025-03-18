#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#     "lark",
# ]
# ///

import ast
import os
import re
import sys
import time
from lark import Lark

PARSER = Lark(r"""
    program.1: command*

    command.1: exec | replace | print | other

    exec.1: "exec"
    replace.1: ESCAPED_STRING "->" ESCAPED_STRING
    print.1: "print" ESCAPED_STRING

    other: /.+/

    %import common.ESCAPED_STRING
    %import common.WS
    %ignore WS

    """, start='program')

def interpret(tree, text, debug):
    if debug:
        os.system("clear")
        print(text)
        time.sleep(0.3)

    for subtree in tree.children:
        for subtree in subtree.children:
            if subtree.data == "exec":
                return text
            if subtree.data == "print":
                print(ast.literal_eval(subtree.children[0].value))
            elif subtree.data == "replace":
                find = ast.literal_eval(subtree.children[0].value)
                replace = ast.literal_eval(subtree.children[1].value)
                text = re.sub(find, replace, text)
            else:
                raise Exception("Invalid command")
    return ""

def run(args, debug):
    program = open(args[0], 'r').read() + '\n'.join(args[1:]) + '\n'
    while len(program) != 0:
        tree = PARSER.parse(program)
        program = interpret(tree, program, debug)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "debug":
        debug = True
        args = args[1:]
    else:
        debug = False
    run(args, debug)
