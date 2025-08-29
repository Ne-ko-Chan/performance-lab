import sys


def build_path(n: int, m: int) -> list[int]:
    path = []
    current = 1
    while True:
        path.append(current)
        current = (current + m - 1) % n
        if current == 0:
            current = n
        else:
            current = current % n
        if current == 1:
            break
    return path

def main():
    if len(sys.argv) != 5:
        print("Wrong number of arguments: need 4 integers")
        sys.exit(1)

    try:
        path1 = build_path(int(sys.argv[1]), int(sys.argv[2]))
        path2 = build_path(int(sys.argv[3]), int(sys.argv[4]))
    except Exception as e:
        print("Error: ", e)
        sys.exit(1)

    path = path1+path2
    print(''.join([str(n) for n in path]))

if __name__ == "__main__":
    main()
