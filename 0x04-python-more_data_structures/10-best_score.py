#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    fk = list(a_dictionary.keys())[0]
    bs = a_dictionary[fk]
    for key, value in a_dictionary.items():
        if value > bs:
            bs = value
            fk = key
    return (fk)
