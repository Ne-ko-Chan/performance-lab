import sys


def min_moves_to_single_number(nums: list[int]):
    if not nums:
        return 0

    # Find median number
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
        median = nums[n // 2]
    else:
        median = (nums[n // 2 - 1] + nums[n // 2]) // 2

    # Count moves amount
    moves = 0
    for num in nums:
        moves += abs(num - median)

    return moves


def main():
    if len(sys.argv) < 2:
        print("Wrong number of parameters. Usage: python task4.py <path/to/file>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, "r") as file:
            nums = [int(line.strip()) for line in file if line.strip()]

        moves = min_moves_to_single_number(nums)

        if moves <= 20:
            print(moves)
        else:
            print(
                "20 ходов недостаточно для приведения всех элементов массива к одному числу"
            )

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
