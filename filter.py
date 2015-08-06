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
for i in range(len(str)):
    if i != cur and (str[i] == "+" or str[i] == "-"):
        filters[str[cur+1:i]] = (str[cur] == "+")
        cur = i
filters[str[cur+1:i+1]] = (str[cur] == "+")
print filters


selected = []
for test in tests:
    run = True
    characterists = tests[test]
    for c in characterists:
        if filters.has_key(c):
            if not filters[c]:
                run = False
                break
    if run:
        selected.append(test)

print selected
