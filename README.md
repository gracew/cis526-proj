cis526-proj
===========
Topic: Language Identification
Team: Vivian Huang, Grace Wang

Objective function: `grade.py`
Default: `identify.py`
Baseline: `ngram.py`
Extensions: `compression.py`, `dunning.py`

All data can be found in the `data/` directory. The training data can be found
in `data/train`; each file contains 9000 sentences. Each file in the
`data/test_data` directory contains 1000 sentences that are different from the
training data. 

To create the dev and test sets (test used for leaderboard scoring), run
`create_test_data.py`. By default, it will create `dev_input` and `test_input`
files containing 500 sentences each. The 500 sentences can come from any of the
15 languages contained in the `test_data` directory. To specify specific
languages, use the `--lang` flag and separate the language names with commas,
e.g. `python create_test_data.py --lang english,spanish,french`.
