import json
from datetime import datetime


def get_data():
    with open("operations.json", "r", encoding='utf-8') as read_file:
        data_get = json.load(read_file)
    return data_get


def filter_data(data, FILTERED_EMPTY_FROM=False):
    data = [x for x in data if "state" in x and x["state"] == 'EXECUTED']
    if FILTERED_EMPTY_FROM:
        data = [x for x in data if "from" in x]
    return data


def last_data(data, VAL):
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:VAL]


def format_data(data):
    formated_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]
        donor = row["from"].split()
        donor_bill = donor.pop(-1)
        donor_bill = f"{donor_bill[:4]} {donor_bill[4:6]}** **** {donor_bill[-4:]}"
        donor_info = ' '.join(donor)
        resident = row["to"].split()
        resident_bill = resident.pop(-1)
        resident_bill = f"**{resident_bill[-4:]}"
        resident_info = ' '.join(resident)
        amount = row["operationAmount"]["amount"]
        currency = row["operationAmount"]['currency']['name']
        formated_data.append(f"""\
{date} {description}
{donor_info} {donor_bill}-> {resident_info} {resident_bill}
{amount}, {currency}""")

    return formated_data
