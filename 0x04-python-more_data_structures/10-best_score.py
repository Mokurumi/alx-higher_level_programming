#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    sorted_scores = sorted(a_dictionary.items(),
            key = lambda x: x[1], reverse = True)
    return sorted_scores[0][0]
