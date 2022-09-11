##PyCribbage

PyCribbage is a Python application for simulating a card game called Cribbage. 

An overview of the rules of the game and the terminology used can be found [here] (https://www.theukrules.co.uk/rules/children/games/cards/cribbage.html)

## Installation

Download this repo to use this library. You can use Poetry to install the necessary dependencies. After downloading the repo and changing into the directory:

```bash
poetry install
```

Alternatively, you may may mainly install the dependencies in pyproject.toml using your preferred package manager

## Usage

To play an interactive game launch main.py and follow the on screen prompts

```bash
python pycribbage/main.py
```

The prompts will ask for information on which methods to use. The methods are split into the two parts of a cribbage game, The Show and The Play. 

Currently your opponent can use either a random choice during the game or a repeatable choice (useful for replaying the same game). 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
