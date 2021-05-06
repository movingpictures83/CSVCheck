import sys

class CSVCheckPlugin:
    def input(self, filename):
       self.infile = open(filename, 'r')

    def run(self):
       self.firstline = self.infile.readline()

    def output(self, filename):
       outfile =open(filename, 'w')
       x = self.firstline.count(',')
       z = x
       for line in self.infile:
          y = line.count(',')
          if (x != y):
             z = y
       if (x == z):
           outfile.write("VALID CSV FILE WITH "+str(x)+" COLS")
       else:
           outfile.write("INVALID CSV FILE: "+str(x)+" NOT EQUAL "+str(z))
