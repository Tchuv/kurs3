from function import last_data, format_data, filter_data


def test_last_data(test_data):
    data = last_data(test_data, val=2)
    assert data[0]['date'] == '2023-06-30T02:08:58.425572'
    assert len(data) == 2


def test_filter_data(test_data, filtered_empty_from=False):
    assert len(filter_data(test_data, filtered_empty_from=True)) == 2


def test_format_data(test_data):
    data = format_data(test_data[:1])
    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199-> Счет **9589\n31957.58, руб.']
