from function import filter_data, last_data, format_data
from function import get_data


def main():
    VAL = 5
    FILTERED_EMPTY_FROM = True
    data = get_data()
    data = filter_data(data, FILTERED_EMPTY_FROM)
    data = last_data(data, VAL)
    data = format_data(data)
    for row in data:
        print(row, end="\n\n")


if __name__ == "__main__":
    main()
