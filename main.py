from utils import get_data, get_filtered_data, get_last_data, get_formatted_data


def main():
    """
    Функция основного кода программы, выводит информацию о транзакциях
    """
    OPERATIONS_URL = "https://api.npoint.io/965a8959441d23a36a83"
    COUNT_LAST_VALUES = 80
    FILTERED_EMPTY_FROM = True

    data, info = get_data(OPERATIONS_URL)
    if not data:
        exit(info)
    print(info, end="\n\n")

    data = get_filtered_data(data, FILTERED_EMPTY_FROM)
    data = get_last_data(data, COUNT_LAST_VALUES)
    data = get_formatted_data(data)


    for row in data:
        print(row)

if __name__ == "__main__":
    main()