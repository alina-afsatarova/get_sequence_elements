def get_sequence_elements(n):
    sequence = ''
    for i in range(1, n+1):
        sequence += str(i) * i
        if len(sequence) >= n:
            return sequence[:n]


if __name__ == '__main__':
    n = int(input())
    print(get_sequence_elements(n))
