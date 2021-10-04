"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
notTmList = set()
telemarketers = set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        notTmList.add(text[0])
        notTmList.add(text[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        telemarketers.add(call[0])
        notTmList.add(call[1])


# setNotTele = notTmList
# setTelmarketers = telemarketers
ans = []
for num in list(telemarketers):
    if not num in notTmList:
        ans.append(num)

ans.sort()
print("These numbers could be telemarketers: ")
for phone in ans:
    print(phone)
len(123)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

#  Big o : time: o[nlogn] and space: o[n]
#  time complexity worst case nlogn because of built in sorting python 