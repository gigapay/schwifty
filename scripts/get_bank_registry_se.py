#!/usr/bin/env python
import json


def process():

    # Just fill this one with more data and we will be able to include them in the translations
    banks_info = {
        "Avanza Bank": {
            "bank_codes": range(9550, 9569),
            "bic": "SWEDSESS"
        },
        "Citibank International Plc, Sweden Branch": {
            "bank_codes": range(9040, 9049),
            "bic": "CITISESX"
        }
    }
    return [
        {
            "country_code": "SE",
            "primary": True,
            "bic": banks_info[bank]["bic"],
            "bank_code": bank_code,
            "name": bank,
            "short_name": bank,
        }
        for _, bank in enumerate(banks_info)
        for bank_code in banks_info[bank]["bank_codes"]
        if bank_code != ""
    ]


if __name__ == "__main__":
    with open("../schwifty/bank_registry/manual_se.json", "w") as fp:
        json.dump(process(), fp, indent=2)
