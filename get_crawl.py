import utils

from extract_zh import ZhCalc
from ZhConverter.zhhanz_conv import ZhhanzMan

def dump_text(url, out, fmt='%05d.txt', max_size=None, fid=1, max_fid=2500):
    utils.mkdir(out)
    fn = utils.join(out, fmt)

    if max_size is None:
        max_size = 4 * 1024 * 1024

    zm = ZhhanzMan()
    zc = ZhCalc()

    fout = utils.openfile(fn % fid, 'w')
    records = []

    for text in extract_text(url):
        prop = zc.calc(text)
        if zc.calc(text) > 1e-2:
            records.append(prop)
            fout.write(zm.s2t(text))

        ft = fout.tell()
        progress = (ft / max(ft, max_size)) * 100
        print(end=f'FID: {fid}/{max_fid}, File Size: {progress:5.2f}%\r')

        if fout.tell() >= max_size:
            fout.close()
            fid += 1
            if fid > max_fid:
                break
            fout = utils.openfile(fn % fid, 'w')

    fout.close()

    with open('statistic.pkl', 'wb') as pkl:
        import pickle as pk
        pk.dump(records, pkl)

def extract_text(url):
    prefix = 'https://commoncrawl.s3.amazonaws.com/'

    with utils.opengz(utils.read_url(url)) as f:
        for i, line in enumerate(f):
            url = f'{prefix}{line.strip()}'
            print(f'Processing {url}')
            for text in read_wet(url):
                yield text

def read_wet(url, skip=2):
    text = []
    record = False

    with utils.opengz(utils.read_url(url)) as f:
        for line in f:
            if line.startswith('Content-Length:'):
                record = True
                continue
            elif line.startswith('WARC/1.0'):
                record = False
                if skip <= 0:
                    yield ''.join(text).strip()
                skip -= 1
                text = []

            if record == True:
                text.append(line)

if __name__ == "__main__":
    url = 'https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2020-10/wet.paths.gz'
    out = './dump'
    dump_text(url, out)
