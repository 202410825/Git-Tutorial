import os
import struct

def input_scores():
    s = []
    i = 1
    while (True):
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    total = 0
    for n in s:
        total += n
    return total / len(s)

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

def write_scores_to_file(scores, filename):
    with open(filename, 'wb') as file:
        for score in scores:
            file.write(struct.pack('i', score))

def read_scores_from_file(filename):
    scores = []
    with open(filename, 'rb') as file:
        while True:
            data = file.read(4)
            if not data:
                break
            score = struct.unpack('i', data)[0]
            scores.append(score)
    return scores

def main():
    filename = 'score.bin'
    if os.path.exists(filename):
        print("[파일 읽기]")
        scores = read_scores_from_file(filename)
        print("[점수 출력]")
        print(f"개인점수: {' '.join(map(str, scores))}")
        avg = get_average(scores)
        print(f"평균: {avg:.1f}")
    else:
        print('[점수 입력]')
        scores = input_scores()
        print('\n[점수 출력]\n개인점수: ', end='')
        show_scores(scores)
        avg = get_average(scores)
        print(f'평균: {avg:.1f}')
        write_scores_to_file(scores, filename)

if __name__ == "__main__":
    main()
