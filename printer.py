#

import json


def format_json(string):
    return format_item(
                json.loads(string))


def format_for(*args):
    def decorator(function):
        for type in args:
            globals()["_format_%s" % type.__name__] = function

        return function

    return decorator


def format_item(item):
    try:
        return globals()["_format_%s" % type(item).__name__](item)
    except KeyError:
        raise TypeError, "Item has unrecognised type: %s" % type(item)


def indent_item(string):
    return string.replace("\n", "\n    ")


@format_for(dict)
def format_dictionary(item):
    retval = "{\n"

    for k in item:
        retval += "    %s: " % format_item(k)
        retval += indent_item(
                    format_item(
                        item.get(k)))
        retval += ",\n"

    retval += "}"

    return retval


@format_for(list)
def format_list(item):
    retval = "[\n"

    for v in item:
        retval += "    %s,\n" % indent_item(
                                    format_item(v))

    retval += "]"

    return retval


@format_for(str, unicode)
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


@format_for(int, float)
def format_number(item):
    return str(item)


@format_for(type(None))
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

