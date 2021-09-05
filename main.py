#testls
import os
from posixpath import join
import time
import csv
import tempfile;

mytime = time.time()

def question1():
    for x in range(100):
        if x % 3 == 0 and x % 5 == 0:
            print("fizzbuzz")
        if x % 3 == 0:
            print ("fezz")
        if x % 5 == 0:
            print("buzz")

    print(f"time it took = {time.time() - mytime}")

#part 2 starts
#The above is the formula for the volume of a sphere. Given a number R as input, return the volume of a sphere with radius R.

#question1();
def calculateSphere(R):
  pi = 3.14159
  result = (4/3) * pi

  R = R **(1./3.)
  result = result * R
  return result


print(calculateSphere(20))
csvPath = "/home/anwaryus/hw3/hw3/dummpy.csv";

#
list = []
with open(csvPath, newline='') as csvfile:
    line = csv.reader(csvfile, delimiter=',')
    
    for row in line:
        list.append(row)

list.pop(0)

#question 4
def convertCsvToString(path):
    s = "";
    with open(path, newline='') as csvfile:
        line = csv.reader(csvfile, delimiter=',')
        
        for row in line:
            for col in row:
                s += col + ',';
            s += '\n';

    return s;

csvToString = convertCsvToString(csvPath);

print(csvToString)
def convertCsvTobj(StringCSV):
    skipfirstline = False;

    lines = StringCSV.split('\n')
    titles = ["Title", []]
    author = ["Author", []]
    _id = ["ID", []]
    pages = ["Pages", []]
    
    for col in lines:
        if(skipfirstline == True):
            row = col.split(",")

            if(len(row) > 2):
                titles[1].append(row[0]);
                author[1].append(row[1]);
                _id[1].append(row[2]);
                pages[1].append(row[3]);

        else:
            skipfirstline = True;


    grid = titles + author + _id + pages;
    return grid;

grid = convertCsvTobj(csvToString);

#print(grid);

def generateTemp(grid):
    tmp = tempfile.NamedTemporaryFile()
    # Open the file for writing.
    with open(tmp.name, 'w') as file:
        s = "";
        i = 0;
        while i < len(grid):
            s+= str(grid[i]) + ",";
            i = i+2;
        s = s + '\n'
        i = 0;

        while i < len(grid[1]):
            s += grid[1][i] + ',' + grid[3][i] +","+ grid[5][i] + ',' + grid[7][i] +   ' \n';
            i+=1;
        file.write(s)

    mygrid = "";
    with open(tmp.name) as file:
        #mygrid = convertCsvTobj(file);
        for line in file:
            mygrid += line;
    

    #print(mygrid);
    return convertCsvTobj(mygrid);

gridobj = generateTemp(grid);
print(gridobj)