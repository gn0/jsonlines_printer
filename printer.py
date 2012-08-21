#

import json


def format_json(string):
    item = json.loads(string)

    return format_item(item)


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


def format_dict(item):
    def indent_item(string):
        return string.replace("\n", "\n    ")

    retval = "{\n"

    for k in item:
        retval += "    %s: " % format_item(k)

        formatted_item = format_item(item[k])
        formatted_item = indent_item(formatted_item)

        retval += formatted_item
        retval += ",\n"

    retval += "}"

    return retval


def format_list(item):
    def indent_item(string):
        return string.replace("\n", "\n    ")

    retval = "[\n"

    for v in item:
        formatted_item = format_item(v)
        formatted_item = indent_item(formatted_item)

        retval += "    %s,\n" % formatted_item

    retval += "]"

    return retval


def format_string(item):
    if "\n" in item:
        # Multiline

        retval = "\n"
        retval += "\"\"\"\n"
        retval += "%s\n" % item
        retval += "\"\"\""

        retval = retval.replace("\n", "\n    ")

        return retval

    return "\"%s\"" % item.replace("\\", "\\\\").replace("\"", "\\\"")


def format_int(item):
    return str(item)


def format_float(item):
    return str(item)


def format_none(item):
    return "None"

