from io import TextIOWrapper
import sys
import string


def point_position(
    center: tuple[int, int], radius: tuple[int, int], point: tuple[int, int]
) -> int:
    # count distance according to formula
    # got formula from canonical equation
    # for ellipse: x^2/a^2 + y^2/b^2 = 1
    distance = (point[0] - center[0]) ** 2 / radius[0] ** 2 + (
        point[1] - center[1]
    ) ** 2 / radius[1] ** 2
    if abs(distance - 1) < sys.float_info.min:
        return 0
    if distance - 1 > 0:
        return 2
    else:
        return 1


def read_point(file: TextIOWrapper) -> tuple[int, int]:
    line = file.readline()
    line = line.strip(string.whitespace)
    coords = line.split(" ")
    if len(coords) != 2:
        raise Exception("wrong amount of arguments in line")

    return (int(coords[0]), int(coords[1]))


def main():
    if len(sys.argv) != 3:
        print("Wrong number of arguments. Needs to be 2 file paths")
        sys.exit(1)

    with open(sys.argv[1], "r") as ellipse_file:
        try:
            center = read_point(ellipse_file)
            radius = read_point(ellipse_file)
        except Exception as e:
            print("Error: ", e)
            sys.exit(1)

    with open(sys.argv[2], "r") as points_file:
        for line in points_file:
            coords = line.split(" ")

            if len(coords) != 2:
                raise Exception("wrong amount of arguments in line")
            print(point_position(center, radius, (int(coords[0]), int(coords[1]))))


if __name__ == "__main__":
    main()
