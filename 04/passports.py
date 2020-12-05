import re

class Passport:
    birth_year = None
    issue_year = None
    expiration_year = None
    height = None
    hair_color = None
    eye_color = None
    passport_id = None
    country_id = None

def passport_generator(unformatted_passport):
    formatted_passport = Passport()
    # Birth Year
    if re.search(r".*?byr:(.*?)( |$).*", unformatted_passport):
        formatted_passport.birth_year = int(re.search(r".*?byr:(.*?)( |$).*", unformatted_passport).group(1))
    # Issue Year
    if re.search(r".*?iyr:(.*?)( |$).*", unformatted_passport):
        formatted_passport.issue_year = int(re.search(r".*?iyr:(.*?)( |$).*", unformatted_passport).group(1))
    # Expiration Year
    if re.search(r".*?eyr:(.*?)( |$).*", unformatted_passport):
        formatted_passport.expiration_year = int(re.search(r".*?eyr:(.*?)( |$).*", unformatted_passport).group(1))
    # Height
    if re.search(r".*?hgt:(.*?)( |$).*", unformatted_passport):
        formatted_passport.height = str(re.search(r".*?hgt:(.*?)( |$).*", unformatted_passport).group(1))
    # Hair Color
    if re.search(r".*?hcl:(.*?)( |$).*", unformatted_passport):
        formatted_passport.hair_color = str(re.search(r".*?hcl:(.*?)( |$).*", unformatted_passport).group(1))
    # Eye Color
    if re.search(r".*?ecl:(.*?)( |$).*", unformatted_passport):
        formatted_passport.eye_color = str(re.search(r".*?ecl:(.*?)( |$).*", unformatted_passport).group(1))
    # Passport ID
    if re.search(r".*?pid:(.*?)( |$).*", unformatted_passport):
        formatted_passport.passport_id = str(re.search(r".*?pid:(.*?)( |$).*", unformatted_passport).group(1))
    # Country ID
    if re.search(r".*?cid:(.*?)( |$).*", unformatted_passport):
        formatted_passport.country_id = str(re.search(r".*?cid:(.*?)( |$).*", unformatted_passport).group(1))
    return (formatted_passport)


def passport_validity_checker(passport, field):
    if (field == "byr"):
        if(not (passport.birth_year >= 1920 and passport.birth_year <= 2002)):
            return False
    elif ((field == "iyr")):
        if(not (passport.issue_year >= 2010 and passport.issue_year <= 2020)):
            return False
    elif ((field == "eyr")):
        if(not (passport.expiration_year >= 2020 and passport.expiration_year <= 2030)):
            return False
    elif ((field == "hgt")):
        if (not re.search(r"^[0-9]*(cm|in)$", passport.height)):
            return False
        if(passport.height[-2:] == "in"):
            if(not (int(passport.height[:-2])>=59 and int(passport.height[:-2])<=76)):
                return False
        elif(passport.height[-2:] == "cm"):
            if(not (int(passport.height[:-2])>=150 and int(passport.height[:-2])<=193)):
                return False
    elif ((field == "hcl")):
        if (not re.search(r"^#[0-9a-f]{6}$", passport.hair_color)):
            return False
    elif ((field == "ecl")):
        if (not re.search(r"^(amb|blu|brn|gry|grn|hzl|oth)$", passport.eye_color)):
            return False
    elif ((field == "pid")):
        if (not re.search(r"^[0-9]{9}$", passport.passport_id)):
            return False
    return True

# Process the data - each item in passports is a full passports, newlines replaced with spaces
input = open('./input.txt')
read_file = input.read()
raw_passports = read_file.split("\n\n")
processed_passports = []
for i in raw_passports:
    i = i.replace('\n', ' ')
    processed_passports.append(passport_generator(i))

passports_with_all_fields = []
num_of_invalid_passports = 0
for i in processed_passports:
    if (not (i.birth_year and i.issue_year and i.expiration_year and i.height and i.hair_color and i.eye_color and i.passport_id)):
        num_of_invalid_passports += 1
    else:
        passports_with_all_fields.append(i)
print("Part 1 - Number of valid passports: ", len(processed_passports) - num_of_invalid_passports)

num_of_invalid_passports = 0
for i in passports_with_all_fields:
    if(not 
        (passport_validity_checker(i, "byr")
        and
        passport_validity_checker(i, "iyr")
        and
        passport_validity_checker(i, "eyr")
        and
        passport_validity_checker(i, "hgt")
        and
        passport_validity_checker(i, "hcl")
        and
        passport_validity_checker(i, "ecl")
        and
        passport_validity_checker(i, "pid"))
    ):
        num_of_invalid_passports += 1
print("Part 2 - Number of valid passports: ", len(passports_with_all_fields) - num_of_invalid_passports)

test_passport = Passport()
test_passport.birth_year = 2002
test_passport.issue_year = 2021
test_passport.expiration_year = 2032
test_passport.height = "191cm"
test_passport.hair_color = "123abc"
test_passport.eye_color = "way"
test_passport.passport_id = "0123456789"

print(passport_validity_checker(test_passport, "pid"))