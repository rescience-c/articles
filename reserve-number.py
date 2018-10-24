#! /usr/bin/env python3
# -----------------------------------------------------------------------------
# Copyright 2018 ReScience C - BSD two-clauses licence
#
# This script reserves a new article number
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    import yaml
    import argparse

    # Argument parsing
    parser = argparse.ArgumentParser(description='Article number reservation')
    parser.add_argument('--volume', action='store', required=True,
                        help="Volume number")
    parser.add_argument('--update', action='store_true', 
                        default=False, help="Wheter to update volumes.yaml")
    args = parser.parse_args()
    
    # Open volume counter files
    with open("volumes.yaml") as file:
        data = yaml.load(file.read())

    # Search for the given volume, creates it if necessary
    key = "volume " + str(args.volume)
    if key not in data.keys():
        data[key] = 1
    else:
        data[key] += 1

    number = data[key]
    print("Request for a new article number for {0}".format(key))
    print("Article No: {0}".format(number))

    # Save result (if update is true)
    if args.update:
        with open("volumes.yaml",'w') as file:
            yaml.dump(data, file, default_flow_style=False)
        print(
            '''"volumes.yaml" has been updated, don't forget to commit the change''')
    else:
        print('"volumes.yaml" has NOT been updated')


