#!/usr/bin/env python3

import argparse
import json
import pathlib
import random

HERE = pathlib.Path(__file__).parent

DATA_PATH = HERE / "data.json"
DATA = json.loads(DATA_PATH.read_text()) or {}


def main(args):
    selected_data = DATA.get(args.contains, [])
    if not selected_data:
        return print(f'NO data for "{args.contains}" or no file {DATA_PATH.resolve()}')
    rindex = random.randint(0, len(selected_data))
    print(selected_data[rindex].strip())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Select a random sentence containing given word from data.json "
    )
    parser.add_argument(
        "-c", "--contains", type=str, choices=DATA.keys(), required=True
    )
    args = parser.parse_args()
    main(args)
