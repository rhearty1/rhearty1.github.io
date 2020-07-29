import glob, os
NUM_LINES_TO_SKIP_FIRST = 2
NUM_LINES_TO_SKIP_LAST = 2
dirname = 'inputs'
os.chdir(dirname)
filenames = glob.glob("*.txt")
for filename in filenames:
    print(filename)
print('Overwriting output.txt...')
with open('../output.txt', 'w', encoding="utf-8") as outfile:
    for filename in filenames:
        with open(filename, encoding="utf-8") as infile:
            data = infile.read().splitlines(True)
            if filename == filenames[0]: # handle first file, leave header
                print(filename, 'is first in array. Removing footer lines only...')
                for line in data[0:-NUM_LINES_TO_SKIP_LAST]:
                    outfile.write(line)
            elif filename == filenames[-1]: # handle last file, leave footer
                print(filename, 'is last in array. Removing header lines only...')
                for line in data[NUM_LINES_TO_SKIP_FIRST:]:
                    outfile.write(line)
            else: # business as usual, skip first and last two lines
                for line in data[NUM_LINES_TO_SKIP_FIRST:-NUM_LINES_TO_SKIP_LAST]:
                    outfile.write(line)
