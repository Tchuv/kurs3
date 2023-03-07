from function import filter_data, last_data, format_data
from function import get_data


def main():
    val = 5
    filtered_empty_from = True
    data = get_data()
    data = filter_data(data, filtered_empty_from)
    data = last_data(data, val)
    data = format_data(data)
    for row in data:
        print(row, end="\n\n")


if __name__ == "__main__":
    main()
