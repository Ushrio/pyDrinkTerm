# PyDrinkTerm
This is a very simple Python drink tracker. It simply takes in a user's name,
the alcohol percentage of their drink, volume of their drink, and any comments they
have. Then outputs that information to a .csv file.

This information can then be used to plot out data and graphs for deeper analysis.

## How to Run
This program uses pipenv for dependency management. Simply install pipenv and then
run the following commands.
```
pipenv install
```
This will install the required dependencies.

```
pipenv shell
```
This command will start up a shell with the virtual environment that pipenv has
configured. From that shell simply run the following command and follow the prompts
to begin.
```
python src/app.py
```
