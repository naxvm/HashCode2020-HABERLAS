

process = lambda l: list(map(int, l.split()))

def parse(file):
    with open(file, 'r') as f:
        lines_raw = f.readlines()
    lines = list(map(process, lines_raw))
    info = {}

    info['total_books'] = lines[0][0]
    info['total_libraries'] = lines[0][1]
    info['total_days'] = lines[0][2]

    info['books'] = {}
    for idx, score in enumerate(lines[1]):
        info['books'][idx] = score

    info['libraries'] = {}
    line_ix = 2
    library_idx = 0
    while line_ix < len(lines):
        if len(lines[line_ix]) == 0:
            break
        print('line_ix', line_ix)
        _, treg, rate = lines[line_ix]

        line_ix += 1

        books = lines[line_ix]
        info['libraries'][library_idx] = {
            'treg': treg,
            'rate': rate,
            'books': books}
        line_ix += 1
        library_idx += 1


    return info['books'], info['libraries'], info['total_days']



if __name__ == '__main__':
    d = parse('input_data/b_read_on.txt')