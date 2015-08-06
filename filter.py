# read manifest - test_name,characterist1,characterist2,...
manifest = []
with open('manifest', 'r') as f:
    for line in f:
       if not line.startswith("#") and not line.strip() == "":
           manifest.append(line.strip())

# extract test characteristics - {"test_name", "characterist1,characterist2,..."}
tests = {}
for test in manifest:
    temp = test.split(",")
    tests[temp[0]] = temp[1:]

# filter keywords in args.filters
import sys
import argparse
parser = argparse.ArgumentParser(description="Runner for guided Web API tests.")
parser.add_argument("-f", "--filters", action="store",help="filters for tests to run")
args = parser.parse_args(sys.argv[1:])

# get filter right - {"key", True/False}
filters = {}
cur = 0
str = args.filters
selected = []
if str is not None:
    for i in range(len(str)):
        if i != cur and (str[i] == "+" or str[i] == "-"):
            filters[str[cur+1:i]] = (str[cur] == "+")
            cur = i
    filters[str[cur+1:i+1]] = (str[cur] == "+")
    print filters

    for test in tests:
        true = True
        characterists = tests[test]
        if len(characterists) == 0:
            true = False
        has_key = False
        for c in characterists:
            if filters.has_key(c):
                true = true & filters[c]
                has_key = True
        if true and has_key:
            selected.append(test)
else:
   selected = tests.keys()

print selected
