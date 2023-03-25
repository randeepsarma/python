# website to learn :"https://regexr.com"
import re

pattern = r"[a-z]+ython"
text = """Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions; you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2), but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of python.sython

There are also Python interpreter and IDE bundles available, such as Thonny. Other options can be found at IntegratedDevelopmentEnvironments.

At some stage, you'll want to edit and save your program code. Take a look at HowToEditPythonCode for some advice and recommendations.

Learning Python
Next, read a tutorial and try some simple experiments with your new Python interpreter.

If you have never programmed before, see BeginnersGuide/NonProgrammers for a list of suitable tutorials.

If you have previous programming experience, consult BeginnersGuide/Programmers, which lists more advanced tutorials.

If English isn't your first language, you might be more comfortable with a tutorial that's been translated into your language. Consult python.org's list of Non-English resources.

Most tutorials assume that you know how to run a program on your computer. If you are using Windows and need help with this, see How do I Run a Program Under Windows."""

pattern = r"[a-zA-Z]+ython"
# match = re.search(pattern, text)

matches = re.finditer(pattern, text)
for match in matches:
    # print(match)
    print(match.span())
    print(text[match.span()[0] : match.span()[1]])
