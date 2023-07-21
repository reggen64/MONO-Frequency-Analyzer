#!//usr/bin/env python3

import sys
from tabulate import tabulate
from string import ascii_lowercase

usage_msg = "Usage: "+ sys.argv[0] +" (-f/-s/-sf) [file]"
help_msg = usage_msg + "\n" +\
        "Examples:\n" +\
        "  To find frequency of letters in the file named 'text.txt', do: \n" +\
        "  $ python "+ sys.argv[0] +" -f text.txt\n" +\
        "  For substitution based on frequency use -s. For both use -sf or -fs."

if len(sys.argv) < 2 or len(sys.argv) > 4:
    print(usage_msg)
    sys.exit(1)


alphabets=ascii_lowercase
most_used='etaoinsrhldcumfpgwybvkxjqz'
var1=0
var2=0

if(sys.argv[1] == '-s'):
    var2=1
elif(sys.argv[1] == '-f'):
    var1=1
elif(sys.argv[1] == '-sf' or sys.argv[1] == '-fs'):
    var1=1
    var2=1
elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print(help_msg)
    sys.exit(1)
else:
    print("Unrecognized first argument: "+ sys.argv[1])
    print("Please use '-s', '-f', '-sf/-fs' or '-h'.")

if(len(sys.argv)<3):
    input_file=input("Please enter file name:-")
    with open(input_file) as f:
        input_text = f.read()
else:
    with open(sys.argv[2]) as f:
        input_text = f.read()

original_text = input_text
#k
#change input_text to all lowercase and remove all misc. characters to analyse
input_text=input_text.replace('\n', '').replace(' ', '')
input_text=''.join(ch for ch in input_text if ch.isalpha())
input_text=input_text.lower()

def freq(ch):
    return input_text.count(ch)

    #create list countaining count of characters in l3
count=[]
for i in alphabets:
    count.append(input_text.count(i))

    #sort the alphabets according to above
ordered_alphabets=list(alphabets)
ordered_alphabets.sort(key=freq, reverse=True)


def frequency(var1):
    if(var1==1):
        count.sort(reverse=True)
        percentage=[]
        for i in count:
            percentage.append("{:.2f}".format((i*100)/len(input_text))+'%')
        finalist = [list(a) for a in zip(ordered_alphabets, count, percentage, most_used)]
        print(tabulate(finalist, headers=["Alphabet", "Count", "Percentage", "Expected Substitution"], stralign="center"))

        print('\n\nSo, assuming direct correlation between char and frequency, following substitution should be made:\n')
        print(''.join(map(str, ordered_alphabets)), " = ", most_used, '\n')

def substitution(var1, var2):
    original = original_text
    if(var2==1 and var1==0):
        print('\n\nAssuming direct correlation between char and frequency, following substitution should be made:\n')
        print(''.join(map(str, ordered_alphabets)), " = ", most_used, '\n')
        #print after substitution
        for i in alphabets:
            original=original.replace(i, most_used[ordered_alphabets.index(i)])
            original=original.replace(i.upper(), most_used[ordered_alphabets.index(i)].upper())
        print(original)
    elif(var2 == 1 and var1==1):
        #print after substitution
        for i in alphabets:
            original=original.replace(i, most_used[ordered_alphabets.index(i)])
            original=original.replace(i.upper(), most_used[ordered_alphabets.index(i)].upper())
        print(original)

frequency(var1)
substitution(var1, var2)
