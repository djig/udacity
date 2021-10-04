"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    l = len(texts)
    if l < 1:
        print('no input')
    row = texts[0] #firstRow
    print("First record of texts, "+ row[0] +" texts "+ row[1] +" at time "+ row[2])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    l = len(calls)
    i = 0
    if l < 1:
        print('no input')
    row = calls[l-1] #lastRow
    print("Last record of calls, "+ row[0] +" calls "+ row[1] +" at time "+ row[2] + ", lasting "+ row[3] + " seconds")

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
#  Big o : time: o[1] and space: o[1]
#  worst case will be constant because We are accessing only two rows first and last all the time.