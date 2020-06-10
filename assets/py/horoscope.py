#!/usr/bin/python3

# Author: Sean Lasater

def main():
    import requests
    import json
    import pprint
    import argparse

    parser = argparse.ArgumentParser(description='Get your horoscope!')
    parser.add_argument('-s', '--sign', type=str, required='true', help='sign')
    args = parser.parse_args()

    your_sign = args.sign

    params = (
    ('sign', f'{your_sign}'),
    ('day', 'today'))

    r = requests.post('https://aztro.sameerkumar.website/', params=params)
    text_json = json.loads(r.text)
    print(pprint.pprint(text_json))

main()