eregex:
file to test:
dictionary.txt

command to get the correct words
cat dictionary.txt | egrep '(.)\1.*(.\1{2,})'

file holding the words:
p2_result.txt

just the command:
cat /usr/share/dict/words | egrep '(.)\1.*(.\1{2,})'

how to run program:
javascript
javascript version:
v9.11.0
node file_name

python 3
python3 file_name


Brandon W.
David T.
Nathan K.
