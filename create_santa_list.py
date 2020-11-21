import random
import copy
from typing import List, Tuple
import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Generate a secret santa list. Takes a csv file as input. Expects a header row, with two columns `name,group`')
    parser.add_argument('infile', help='Path to input file')
    return parser.parse_args()


def read_input(filename:str) -> List[Tuple]:
    """Reads a text file into a list, assumes the first row is a header row"""
    with open(filename, "r") as f:
        out = f.readlines()[1:]
    return list(filter(None, [tuple(x.strip().replace('\n','').split(',')) for x in out]))


def match_santas(santas:List[Tuple])-> List[Tuple[Tuple,Tuple]]:
    """randomly assigns a list of names into a set of unique pairs. Assumes all names in the input list are unique"""
    solution = False
    while not solution:
        receivers = copy.deepcopy(santas)
        matched_pairs = []
        for santa in santas:
            recip = random.choice(receivers)
            counter = 0
            max_count_reached = False
            while santa == recip or santa[1] == recip[1]:
                recip = random.choice(receivers)
                if len(recip)==1:
                    print(f"Unable to find a match for {santa}")
                    recip=("","")
                    break
                counter += 1
                if counter >= len(receivers):
                    print(f"Unable to find a match for {santa}")
                    max_count_reached = True
                    break
            if not max_count_reached:
                matched_pairs.append([santa, recip])
                _ = receivers.pop(receivers.index(recip))
            if len(matched_pairs)==len(santas):
                solution = True
    return matched_pairs


def write_output(matched_pairs:List) -> str:
    outlist = []
    for x in matched_pairs:
         outlist.append([x[0][0], x[0][1], x[1][0], x[1][1]])
    outstr=['gifter,gifter_group,receiver,receiver_group']
    outstr+=[','.join(x) for x in outlist]
    return '\n'.join(outstr)

def main():
    args = get_args()
    names = read_input(args.infile)
    matches = match_santas(names)
    print(write_output(matches))

if __name__ == "__main__":
    main()