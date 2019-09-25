#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


def upperFirst(inputString):
    return ('{0}{1}'.format(inputString[0].upper(),
                            inputString[1:]) if inputString else '')


def preserveCamelCase(inputString):
    isLastCharLower = False
    isLastCharUpper = False
    isLastLastCharUpper = False

    output = inputString
    charPattern = re.compile(r'[a-zA-Z]')
    i = 0

    while i < len(output):
        character = output[i]

        if isLastCharLower and charPattern.match(character) \
                and character.upper() == character:

            output = '{0}-{1}'.format(output[0:i], output[i:])
            isLastCharLower = False
            isLastLastCharUpper = isLastCharUpper
            isLastCharUpper = True
            i += 1

        elif isLastCharUpper and isLastLastCharUpper \
                and charPattern.match(character) and character.lower() \
                == character:

            output = '{0}-{1}'.format(output[0:i - 1], output[i - 1:])
            isLastLastCharUpper = isLastCharUpper
            isLastCharUpper = False
            isLastCharLower = True

        else:
            isLastCharLower = character.lower() == character \
                and character.upper() != character
            isLastLastCharUpper = isLastCharUpper
            isLastCharUpper = character.upper() == character \
                and character.lower() != character

        i += 1

    return output


def camelcase(inputString, pascalCase=False):
    if type(inputString) is not str and type(inputString) is not list:
        raise TypeError('Expected the input to be `str | [str]`')

    if type(inputString) is list:
        output = '-'.join([x.strip() for x in inputString if x.strip()])
    else:
        output = inputString.strip()

    if len(output) == 0:
        return ''

    if len(output) == 1:
        return (output.upper() if pascalCase else output.lower())

    hasUpperCase = output != output.lower()

    if hasUpperCase:
        output = preserveCamelCase(output)

    # remove all special chars at the beginning of string
    output = re.sub(r'^[_.\- ]+', '', output).lower()

    # upper case all characters after delimiters
    output = re.sub(r'[_.\- ]+(\w|$)',
                    lambda x: x.groups()[0].upper(),
                    output)

    # upper case all charachters after digits
    output = re.sub(r'\d+(\w|$)',
                    lambda x: x.group().upper(),
                    output)

    return (upperFirst(output) if pascalCase else output)


if __name__ == "__main__":
    print('{0} => {1}'.format('fooBar', camelcase('fooBar')))
    print('{0} => {1}'.format('FOO-BAR', camelcase('FOO-BAR')))
