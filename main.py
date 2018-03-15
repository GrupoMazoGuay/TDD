import sys
from sample.strings_example import StringsExamples

if __name__ == "__main__":
    args = sys.argv[1:]
    print("Concat strings %s %s..." % (args[0], args[1]))
    concated_strings = StringsExamples.concat_strings(args[0], args[1])
