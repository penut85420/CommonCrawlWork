import io
import os
import gzip
import requests

def download(url, out):
    with open(out, 'wb') as f:
        f.write(requests.get(url).content)

def read_url(url):
    return io.BytesIO(requests.get(url).content)

def opengz(path):
    return gzip.open(path, 'rt', encoding='UTF-8')

def mkdir(path):
    os.makedirs(path, exist_ok=True)

def join(*args):
    return os.path.join(*args)

def openfile(path, mode):
    return open(path, mode, encoding='UTF-8')

if __name__ == "__main__":
    # url = 'https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2020-10/wet.paths.gz'
    # for line in opengz(read_url(url)):
    #     print(line)
    #     input()

    print(join('a', 'b', 'c'))
