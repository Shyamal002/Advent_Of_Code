"--- Day 4: Passport Processing ---"
import re
import string

__author__ = "Shyamal Akruvala"

def splitData(lines):
    pattern = r"(?:\r?\n){2,}"
    return re.split(pattern, lines.strip())

if __name__ == "__main__":
    print("--- Day 4: Passport Processing ---")

    with open("./2020/input/inputDay4.txt","r") as f:
        lines = f.readlines()

    passports=[]
    for record in splitData("".join(lines)):
        passports.append(record.replace(' ', '\n').split('\n'))
    
    # Part 1
    mandatoryFields=["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    validPassportCounter=0
    for passport in passports:
        fieldCheck = 0
        passportDict = {}
        for x in passport:
            passportDict[x.split(":")[0]] = x.split(":")[1]
        for field in mandatoryFields:
            if field in list(passportDict.keys()):
    #             print("Field {} is present".format(field))
                fieldCheck += 1
        if fieldCheck == 7:
            validPassportCounter += 1
    print("Part 1 - Valid count of passports is {}".format(validPassportCounter))

    # Part 2
    mandatoryFields=["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    validPassportCounter=0
    for passport in passports:
        fieldCheck = 0
        passportDict = {}
        for x in passport:
            passportDict[x.split(":")[0]] = x.split(":")[1]
        for field in mandatoryFields:
            if field in list(passportDict.keys()):
                fieldCheck += 1
        if fieldCheck == 7:
            if int(passportDict['byr']) >= 1920 and int(passportDict['byr']) <= 2002:
                if int(passportDict['iyr']) >= 2010 and int(passportDict['iyr']) <= 2020:
                    if int(passportDict['eyr']) >= 2020 and int(passportDict['eyr']) <= 2030:
                        if passportDict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                            if (passportDict["hcl"][0] == "#" and set(passportDict["hcl"][1:]).issubset(string.hexdigits)):
                                if len(passportDict["pid"]) == 9:
                                    if (passportDict["hgt"].strip()[-2:] == 'cm' and (int(passportDict["hgt"].strip()[:-2]) >= 150 and int(passportDict["hgt"].strip()[:-2]) <= 193)) or \
                                        (passportDict["hgt"].strip()[-2:] == 'in' and (int(passportDict["hgt"].strip()[:-2]) >= 59 and int(passportDict["hgt"].strip()[:-2]) <= 76)):
                                            validPassportCounter += 1
    print("Part 2 - Valid count of passports is {}".format(validPassportCounter))