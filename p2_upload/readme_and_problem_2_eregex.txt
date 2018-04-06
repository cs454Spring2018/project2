eregex:
file to test:
dictionary.txt

command to get the correct words
cat dictionary.txt | egrep '(.)\1.*(.\1{2,})'

file holding the words:
p2_result.txt

how to run program:
javascript
node file_name

python 3
python3 file_name


Brandon W.
David T.
Nathan K.
