#important: in order to import things from pip
# a virtual environment must be created and activated first
# py -m venv venv
# then activate: ./vevn/Scripts/activate

import pyjokes

print(pyjokes.get_joke())  # This will print a random joke