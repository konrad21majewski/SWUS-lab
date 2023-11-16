file_data = {
    "cbr": {
        "avgIPDT": {
            "B10": [
                (1050, 0.000206803),
                (1080, 0.000185114),
                (1095, 0.000207183),
            ],
            "B30": [
                (3050, 0.00020668),
                (3080, 0.000185977),
                (3095, 0.000170091),
            ],
            "B100": [
                (10050, 0.000204663),
                (10080, 0.000203402),
                (10095, 0.000172319),
            ],
        },
        "minIPDT": {
            "B10": [
                (1050, 0.000134),
                (1080, 0.000128),
                (1095, 0.000127),
            ],
            "B30": [
                (3050, 0.000133),
                (3080, 0.000128),
                (3095, 0.000127),
            ],
            "B100": [
                (10050, 0.000132),
                (10080, 0.000128),
                (10095, 0.000127),
            ],
        },
        "IPDV95": {
            "B10": [
                (1050, 0.000213),
                (1080, 0.000165),
                (1095, 0.000114),
            ],
            "B30": [
                (3050, 0.000236),
                (3080, 0.000142),
                (3095, 0.000112),
            ],
            "B100": [
                (10050, 0.000228),
                (10080, 0.000147),
                (10095, 0.000116),
            ],
        },
        "IPLR": {
            "B10": [
                (1050, 0),
                (1080, 0),
                (1095, 0.0011749),  # Filled IPLR value from cbr1095.txt
            ],
            "B30": [
                (3050, 0),
                (3080, 0),
                (3095, 0),
            ],
            "B100": [
                (10050, 0),
                (10080, 6.94083e-05),  # Filled IPLR value from cbr10080.txt
                (10095, 0),
            ],
        },
        # Add other types as needed
    },
    "pois": {
        "avgIPDT": {
            "B10": [
                (1050, 0.000196387),
                (1080, 0.000343655),
                (1095, 0.000783808),
            ],
            "B30": [
                (3050, 0.00019833),
                (3080, 0.000330042),
                (3095, 0.000798656),
            ],
            "B100": [
                (10050, 0.000198388),
                (10080, 0.000327627),
                (10095, 0.000783853),
            ],
        },
        "minIPDT": {
            "B10": [
                (1050, 0.000128),
                (1080, 0.000127),
                (1095, 0.000126),
            ],
            "B30": [
                (3050, 0.000127),
                (3080, 0.000126),
                (3095, 0.000127),
            ],
            "B100": [
                (10050, 0.000127),
                (10080, 0.000126),
                (10095, 0.000127),
            ],
        },
        "IPDV95": {
            "B10": [
                (1050, 0.000205),
                (1080, 0.00022),
                (1095, 0.000229),
            ],
            "B30": [
                (3050, 0.00022),
                (3080, 0.000998),
                (3095, 0.00206),
            ],
            "B100": [
                (10050, 0.000229),
                (10080, 0.000998),
                (10095, 0.002053),
            ],
        },
        "IPLR": {
            "B10": [
                (1050, 0),
                (1080, 0.000782411),
                (1095, 0.0139232),  # IPLR value not provided in pois1095.txt
            ],
            "B30": [
                (3050, 0),
                (3080, 0.000658667),
                (3095, 0.0150862),  # Filled IPLR value from pois3095.txt
            ],
            "B100": [
                (10050, 0),
                (10080, 0.000303035),  # Filled IPLR value from pois10080.txt
                (10095, 0.0147503),  # Filled IPLR value from pois10095.txt
            ],
        },
        #
    }
}
def get_data(origin, data_type):
    result = {}

    for buffer in file_data[origin][data_type]:
        key = buffer
        values = [(file[0], file[1]) for file in file_data[origin][data_type][buffer]]
        result[key] = values

    return result

if __name__ == "__main__":

    origin = "pois"
    data_type = "IPLR"

    result = get_data(origin, data_type)

    # for key, values in result.items():
    #     print(f"{key}: {values}")

    print(result)