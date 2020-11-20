import random
import copy
from typing import List, Tuple
import argparse

def get_args():
    pass

def read_input(filename:str) -> List:
    """Reads a text file into a list, assumes the first row is a header row"""
    with open(filename, "r") as f:
        out = f.readlines()[1:]
    return list(filter(None, [x.strip().replace('\n','') for x in out]))

def match_santas(santas:List)-> List[Tuple[str,str]]:
    """randomly assigns a list of names into a set of unique pairs. Assumes all names in the input list are unique"""
    receivers = copy.deepcopy(santas)
    matched_pairs = []
    for santa in santas:
        recip = random.choice(receivers)
        while santa == recip:
            recip = random.choice(receivers)
            if santa == recip and len(recip)==1:
                print(f"Unable to find a match for {santa}")
                recip=""
                break
        matched_pairs.append(santa, recip)
        _ = receivers.pop(recip)
    return matched_pairs

def write_output(matched_pairs:List[Tuple[str,str]]) -> str:
    pass

def main():
    args = get_args()
    names = read_input(args.infile)
    matches = match_santas(names)
    print(write_output)

if __name__ == "__main__":
    main()