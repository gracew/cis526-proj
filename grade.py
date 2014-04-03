#!/usr/bin/env python
import optparse
import sys

optparser = optparse.OptionParser()
optparser.add_option("-r", "--ref", dest="ref", help="")
optparser.add_option("-t", "--test", dest="test", help="")
opts = optparser.parse_args()[0]

ref  = [line.strip() for line in open(opts.ref).readlines()]
test = [line.strip() for line in open(opts.test).readlines()]
grade = 0.0

if len(ref) != len(test):
    sys.stderr.write("ERROR: input file & reference file are different lengths")
    sys.exit(1)

for (r, t) in zip(ref, test):
    if r == t:
	grade += 1

print "Percentage of correctly identified sentences", (grade / len(ref))
