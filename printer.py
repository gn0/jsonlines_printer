#

import json


def format_json(string):
    return format_item(
                json.loads(string))


def format_item(item):
    item_type = type(item)

    if item_type == dict:
        return format_dict(item)

    if item_type == list:
        return format_list(item)

    if item_type in (str, unicode):
        return format_string(item)

    if item_type == int:
        return format_int(item)

    if item_type == float:
        return format_float(item)

    if item is None:
        return format_none(item)

    raise TypeError, "Item has unknown type: %s" % item_type


def indent_item(string):
    return string.replace("\n", "\n    ")


def format_dict(item):
    retval = "{\n"

    for k in item:
        retval += "    %s: " % format_item(k)
        retval += indent_item(
                    format_item(
                        item.get(k)))
        retval += ",\n"

    retval += "}"

    return retval


def format_list(item):
    retval = "[\n"

    for v in item:
        retval += "    %s,\n" % indent_item(
                                    format_item(
                                        item.get(k)))

    retval += "]"

    return retval


def format_string(item):
    def is_multiline():
        return "\n" in item

    def multiline_format():
        retval = "\n"
        retval += "\"\"\"\n"
        retval += "%s\n" % item
        retval += "\"\"\""

        return indent_item(retval)

    def inline_format():
        return "\"%s\"" % (item.replace("\\", "\\\\")
                               .replace("\"", "\\\""))

    if is_multiline():
        return multiline_format()
    else:
        return inline_format()


def format_int(item):
    return str(item)


def format_float(item):
    return str(item)


def format_none(item):
    return "None"


if __name__ == "__main__":
    import sys
    import codecs
    import locale
    import fileinput

    sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

    for line in fileinput.input():
        print format_json(line)

