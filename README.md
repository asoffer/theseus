# The Theseus Programming Language

<img src="/assets/logo.png" width="200" /> 

*Theseus* is a simple yet powerful programming language. There are two main ideas.

1. Theseus uses strings, nothing else. There are no numbers, booleans or
   functions. Everything is a string.
1. Theseus programs are self-modifying. Or maybe they just generate new Theseus
   programs. It's hard to say.

## Documentation

Theseus is simple enough that the entire documentation fits in this table:

| Command                | Action                                         |
| ---------------------- | ---------------------------------------------- |
| `print <string>`       | prints the contents of the string to `stdout`. |
| `import <string>`      | replaces the line itself with the contents of the file named by the string. |
| `<string> -> <string>` | Replaces every match of the left-hand side regular expression with the right-hand side |
| `exec`                 | Rerun the modified program |

