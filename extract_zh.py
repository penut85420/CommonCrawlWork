import re

class ZhCalc:
    def __init__(self):
        self.zh_ptn = re.compile(f'[{self.get_all_zh()}]')

    def calc(self, ss):
        zh_num = self.zh_ptn.findall(ss)
        return len(zh_num) / len(ss)

    def get_all_zh(self):
        return join([ch for ch in self.get_plain()])

    def get_plain(self):
        zh_range = [
            '2E80–2EFF', '2F00–2FDF', '3100–312F',
            '3190–319F', '31A0–31BF', '31C0–31EF',
            '3200–32FF', '3400–4DBF', '4E00–9FFF',
        ]
        
        int16 = lambda x: int(x, base=16)
        
        for zhs in zh_range:
            b, e = map(int16, zhs.split('–'))
            yield join(self.range_chr(b, e))

    def range_chr(self, b, e):
        return [chr(i) for i in range(b, e)]

def join(arr):
    return ''.join(arr)

if __name__ == "__main__":
    zc = ZhCalc()

    ss = input()
    while ss:
        print(zc.calc(ss))
        ss = input()
