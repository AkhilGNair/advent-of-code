from pathlib import Path


passports = Path("input.txt").read_text().strip().split("\n\n")

EYE_COLOURS = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def validate_byr(str_data):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    int_data = int(str_data)
    return len(str_data) == 4 and int_data >= 1920 and int_data <= 2002


def validate_iyr(str_data):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    int_data = int(str_data)
    return len(str_data) == 4 and int_data >= 2010 and int_data <= 2020


def validate_eyr(str_data):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    int_data = int(str_data)
    return len(str_data) == 4 and int_data >= 2020 and int_data <= 2030


def validate_hgt(str_data):
    # hgt (Height) - a number followed by either cm or in:
    # - If cm, the number must be at least 150 and at most 193.
    # - If in, the number must be at least 59 and at most 76.
    num, unit = str_data[:-2], str_data[-2:]

    try:
        num = int(num)
    except ValueError:
        return False

    if unit == "cm":
        return num >= 150 and num <= 193
    elif unit == "in":
        return num >= 59 and num <= 76
    else:
        return False


def validate_hcl(str_data):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    sym, code = str_data[:1], str_data[1:]

    try:
        int(code, 16)
    except ValueError:
        return False

    return sym == "#"


def validate_ecl(str_data):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    return str_data in EYE_COLOURS


def validate_pid(str_data):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    try:
        int(str_data)
    except ValueError:
        return False

    return len(str_data) == 9


def validate_cid(str_data):
    # cid (Country ID) - ignored, missing or not.
    return True


_REQUIRED_FIELDS = {
    "byr": validate_byr,
    "iyr": validate_iyr,
    "eyr": validate_eyr,
    "hgt": validate_hgt,
    "ecl": validate_ecl,
    "hcl": validate_hcl,
    "pid": validate_pid,
    "cid": validate_cid,
}


def validate(data):
    fields = data.replace("\n", " ").split(" ")
    document = dict(prop.split(":") for prop in fields)

    for required, validator in _REQUIRED_FIELDS.items():
        val = document.get(required)
        if not val:
            if required != "cid":
                return False
        valid_field = validator(val)
        if not valid_field:
            print(required, val)
            return False

    return True


print(sum(validate(passport) for passport in passports))
