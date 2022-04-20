"""We have an existing dictionary that maps US states to their capitals.
1. Print the state capital of Idaho
2. Print all states.
3. Print all capitals.
4. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...'
5. Ensure the string you created in 4. is alphabetically sorted by state
7. Now we want to add the reverse look up, given the name of a capital what state
is it in?
Implement the function def get_state(capital): below so it returns the state.
GOTCHAS: What happens if two states have the same capital name, how do you
handle that?

"""
import sys

import pytest

STATES_CAPITALS = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas': 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne',
    'Andrey' : 'City',
}

# 1. Print the state capital of Idaho
def capital_of_Idaho():
    state1 = "Idaho"
    state_capital1 = STATES_CAPITALS[state1]

    print(f"1. State capital of {state1} - {state_capital1}")


#2. Print all states
def all_states():
    print (f"2. US states:")
    for key in STATES_CAPITALS.keys():
        print (f" {key}")

#3. Print all capitals.
def all_capitals():
    print (f"3. US state capitals:")
    for value in STATES_CAPITALS.values():
        print (f" {value}")

#4. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...'
def states_capitals_string():
    single_string=""
    print (f"4. String: state -> state capitals:")
    for key, value in STATES_CAPITALS.items():
        single_string = single_string + (f", {key} -> {value}")
    print (single_string[2:])

#5. Ensure the string you created in 4. is alphabetically sorted by state
def states_capitals_string_sorted():

    STATES_CAPITALS_sorted = dict(sorted(STATES_CAPITALS.items(), key=lambda x: x[0]))

    single_string=""
    print (f"5. Sorted string: state -> state capitals:")
    for key, value in STATES_CAPITALS_sorted.items():
        single_string = single_string + (f", {key} -> {value}")
    print (single_string[2:])

#7. Now we want to add the reverse look up, given the name of a capital what state is it in?
def get_state(capital):
    state_string=""
    for key, value in STATES_CAPITALS.items():
        if value == capital:
            state_string = state_string + (f", {key}")
    print (f"{capital} is the capital of the {state_string[2:]}")
    return state_string[2:]


def test_state_to_capital():
    assert 'Cheyenne' == STATES_CAPITALS['Wyoming']


def test_state_to_capital_unknown():
    with pytest.raises(KeyError):
        STATES_CAPITALS['']


def test_capital_to_state():
    assert 'Wyoming' == get_state('Cheyenne')


def test_capital_to_state_unknown():
    with pytest.raises(KeyError):
        get_state('')


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    sys.exit(main())



# capital_of_Idaho()
# all_states()
# all_capitals()
# states_capitals_string()
# states_capitals_string_sorted()
# get_state('City')