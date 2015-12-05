##Setup Clout

**Prereqs**
- Python 2.7


Note: /path/to/social = wherever you have it on your host

To set up the Python module:
`export PYTHONPATH=$PYTHONPATH:/path/to/social`

To enter CLI:
`python /path/to/social/clout/commands.py`
ctrl+d to exit
Commands below in [About](##about).


To run tests:
`python /path/to/social/clout/tests/test_main.py`

##About Clout
Create a CLI tool which shows a graph of people and their "popularity", where popularity is the number of followers a person has, including number of followers or followers, etc.

Add a relationship by entering: `<person_a> follows <person_b>`
See the popularity of a person by entering: `clout <person>`
See the popularity of all person by entering: `clout`

Note:
- A person can have an unlimited number of followers.
- A person can only follow one person.
- A person can change who they follow.
- A person may not follow her/himself.