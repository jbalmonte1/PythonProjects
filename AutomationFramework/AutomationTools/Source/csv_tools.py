'''
Created on 7 Apr 2020

@author: jalmonte
'''

import csv
import pandas

class CSVToolsBuiltIn():
    def load_using_builtin(self, csv_file):
        self.fd = open(csv_file, "r")
        self.reader = csv.DictReader(self.fd)
    
    def print_all_rows(self):
        for record in self.reader:
            print(record)
            
    def print_record_by_column(self, key):
        for record in self.reader:
            print(f'{key}: {record[key]}')
            
    def __del__(self):
        self.fd.close()
        
class PandasTools():
    def load_using_pandas(self, csv_file, chunksize = None):
        if chunksize:
            self._chunksize = chunksize
            self.df = pandas.read_csv(csv_file, chunksize = self._chunksize)
        else:
            self.df = pandas.read_csv(csv_file)
    
    def print_data_type(self):
        if self._chunksize:
            for d in self.df:
                print(d.dtypes)
        else:
            print(self.df.dtypes)