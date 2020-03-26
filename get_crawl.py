import os
import argparse
import requests

def main(inn, out):
    out = './gz'
    os.makedirs(out, exist_ok=True)
    prefix = 'https://commoncrawl.s3.amazonaws.com/'

    with open(inn, 'r', encoding='UTF-8') as f:
        for i, line in enumerate(f):
            url = f'{prefix}{line.strip()}'
            r = requests.get(url)
            with open(os.path.join(out, f'{i:05d}.wet.gz'), 'wb') as fout:
                fout.write(r.content)
            if i == 5:
                break

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True)
    parser.add_argument('-o', '--output', required=True)
    args = parser.parse_args()

    main(args.input, args.output)
