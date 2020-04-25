import csv
import argparse

arg = argparse.ArgumentParser(description='Functions that read from and write to csv files')
arg.add_argument("-p","--path")
arg.add_argument("-f", "--file file_name")
def print_file_content(file):
    with open(file) as obj:
        csv_reader = csv.reader(obj, delimiter=',')
        for row in csv_reader:
            print(row)
print_file_content("readertest.csv")
#1B
#def write_list_to_file(file, lis_touple):
#    with open(file, 'w') as obj:
#       for touple in lis_touple:
#          obj.write(touple)
#touples=  {("touples1"),("touples2"),("touples3"),("touples4")}
#write_list_to_file("writetest.csv", touples)
#print_file_content("writetest.csv")
#1Ba
def write_list_to_file(file, strings):
     with open(file, 'w') as obj:
            for string in strings:
                obj.write(string)
write_list_to_file("writetest.csv", "Hello there! General Kenobiiii...")
print_file_content("writetest.csv")

#1C
def read_csv(file):
    lines = []
    with open(file) as csv_file:
        readfile = csv.reader(csv_file)
        for line in readfile:
            lines.append(line)
    return lines
print(read_csv("readertest.csv"))

if __name__ == "__main__":

    parse = arg.parse_args()
    if parse.f:
        print_file_content(parse.path)
