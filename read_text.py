import re
import gzip

def read_gz(inn):
    text = []
    record = False
    with gzip.open(inn, 'rt', encoding='UTF-8') as f:
        for line in f:            
            if line.startswith('Content-Length:'):
                record = True
                continue
            elif line.startswith('WARC/1.0'):
                record = False
                yield ''.join(text).strip()
                text = []
            if record == True:
                text.append(line)

if __name__ == '__main__':
    for t in read_gz('./gz/00000.wet.gz'):
        print(len(t), t[:20])
        input()
