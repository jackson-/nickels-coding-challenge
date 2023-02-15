import argparse

def find_combination(fare, gaavos):
    # Base case: the fare is zero, so we've found a combination that matches
    if fare == 0:
        return []

    # Base case: there are no gaavos left to check
    if not gaavos:
        return None

    # Try each possible gaavo and see if it leads to a solution
    for i, gaavo in enumerate(gaavos):
        # Make a copy of the remaining gaavos, excluding the current one
        remaining_gaavos = gaavos[:i] + gaavos[i+1:]

        # Check if the current gaavo can be used in the solution
        if gaavo <= fare:
            result = find_combination(fare - gaavo, remaining_gaavos)
            if result is not None:
                return [gaavo] + result

    # No combination found
    return None

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('fare', type=int, help='the fare amount')
    parser.add_argument('gaavos', type=int, nargs='+', help='the list of Gaavo pieces')
    args = parser.parse_args()

    # Find the combination of gaavos that matches the fare
    combination = find_combination(args.fare, args.gaavos)
    if combination is None:
        print('No combination of gaavos can match the fare.')
    else:
        print('Combination:', combination)

if __name__ == '__main__':
    main()
