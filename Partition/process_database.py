import argparse
import functools

def compare(set1, set2):
    length = min(len(set1), len(set2))
    for i in range(length):
        if set1[i] < set2[i]:
            return -1
        elif set1[i] > set2[i]:
            return 1
    if len(set1) < len(set2):
        return -1
    else:
        return 1

def clean_database(database): 
    # map tokens to 0, 1, 2,...
    token_dict = dict()
    new_token_id = 0
    for a_set in database:
        for token in a_set:
            if token not in token_dict.keys():
                token_dict[token] = new_token_id
                new_token_id += 1
    print("num. tokens: " + str(new_token_id))
    new_database = []
    for a_set in database:
        new_database.append([token_dict[token] for token in a_set])
    return new_database

def sort_database(database):
    database = sorted(database, key=functools.cmp_to_key(compare))
    return database

def read_database(path):
    database = []
    with open(path, "r", encoding="utf-8") as read_file:
        while True:
            line = read_file.readline()
            if not line:
                break
            temp_line = [int(v) for v in line.strip().split(" ")]
            temp_line.sort()
            database.append(temp_line)
    return database

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input dataset file.")
    parser.add_argument("--output", required=True, help="Path to output dataset file.")
    return parser.parse_args()

def main():
    args = parse_args()
    database = read_database(args.input)
    database = clean_database(database)
    database = sort_database(database)

    with open(args.output, 'w', encoding="utf-8") as write_file:
        for _set in database:
            write_file.write(' '.join([str(v) for v in _set]) + "\n")

if __name__ == "__main__":
    main()
