'''
Created on 8 Sept 2020

@author: jalmonte
'''

import psycopg2
from pip._vendor.distlib import database
from psycopg2._psycopg import OperationalError


class PostgreSQLTools():
    def __init__(self, database, username, password, ip, port):
        '''
        initializes connection to remote database
        '''
        self._dbconnection = ''
        self._cursor = ''
        try:
            self._dbconnection = psycopg2.connect(database = database, user = username, password = password, host = ip, port = port)
            self._cursor = self._dbconnection.cursor()
    
            print(f'Database connection to {ip}:{port} successfully established')
        except OperationalError:
            print(f'Failed to establish connection to {ip}:{port}')
            quit()
    
    def __del__(self):
        '''
        automatically closes connection to remote database
        '''
        if self._dbconnection:
            self._dbconnection.close()
    
    def execute_sql_command(self, command):
        '''
        executes a given sql command
        '''
        print(f'Executing PostgreSQL command: {command}')
        self._cursor.execute(command)
        if command.find('SELECT') != -1:
            return self._cursor.fetchall()
        else:
            self._dbconnection.commit()
        
    def _table_field_builder(self, fields):
        '''
        builder for fields when creating a table
        input should be a list of dictionaries with keys <field_name>, <field_type>, and a list of <options>
        example: [{'field_name': 'Name', 'field_type': 'TEXT'}, 'options': ['NOT NULL']]
        '''
        res = []
        for field in fields:
            if 'options' in field.keys():
                options = [field['options']] if not isinstance(field['options'], list) else field['options']
                res.append(f"{field['field_name']} {field['field_type']} {' '.join(options)}")
            else:
                res.append(f"{field['field_name']} {field['field_type']}")
        
        return f"({', '.join(res)});"
    
    def create_table(self, table_name, fields):
        '''
        creates a table in database
        '''
        _fields_builder = self._table_field_builder(fields)
        _command = f'CREATE TABLE {table_name} {_fields_builder};'
        self.execute_sql_command(_command)
        
    def delete_table(self, table_name):
        '''
        deletes a table in database
        '''
        _command = f'DROP TABLE IF EXISTS {table_name};'
        self.execute_sql_command(_command)
        
    def select_from_table(self, table_name, fields, filter = None, grouping = None, order_by = None, desc = False):
        '''
        retries data from table given a set of filter, grouping, and order
        e.g. query: SELECT name, age FROM student_record WHERE age > 18 ORDER BY name DESC;
             select_from_table("student_record", ['name', 'age'], filter = "age > 18 AND 'age < 60", order_by = "name", desc = True)
        e.g. query: SELECT age, COUNT(*) FROM student_record GROUP BY age ORDER BY age;
             select_from_table("student_record", ['age', 'COUNT(*)'], grouping = "age", order_by = "age")
        '''
        table_name = [table_name] if not isinstance(table_name, list) else table_name
        fields = [fields] if not isinstance(fields, list) else fields
        
        _table_name_clause = ', '.join(table_name)
        _fields_clause = ', '.join(fields)
        
        _command = f"SELECT {_fields_clause} FROM {_table_name_clause}"
        if filter:
            _command = f"{_command} WHERE {filter}"
        if grouping:
            grouping = [grouping] if not isinstance(grouping, list) else grouping
            _grouping_clause = ', '.join(grouping)
            _command = f"{_command} GROUP BY {_grouping_clause}"
        if order_by:
            _order_by_clause = ', '.join(order_by)
            if desc:
                _command = f"{_command} ORDER BY {_order_by_clause} DESC"
            else:
                _command = f"{_command} ORDER BY {_order_by_clause}"
        _command = f"{_command};"
        
        return self.execute_sql_command(_command)
    
    def insert_into_table(self, table_name, fields, values):
        '''
        inserts a new row to the table given by fields and its corresponding values
        e.g. command: INSERT INTO playground (type, color, location, install_date) VALUES ('monkey_bar', 'white', 'south', '2019-12-12');
             insert_into_table('playground', ['type', 'color', 'location', 'install_date'], ['monkey_bar', 'white', 'south', '2019-12-12'])
        '''
        fields = [fields] if not isinstance(fields, list) else fields
        values = [values] if not isinstance(values, list) else values
        
        _fields_clause = '({})'.format(', '.join(fields))
        _values_clause = '({})'.format(', '.join([f"\'{val}\'" for val in values]))
        
        _command = f"INSERT INTO {table_name} {_fields_clause} VALUES {_values_clause}"
        self.execute_sql_command(_command)
        
    def delete_from_table(self, table_name, filter):
        '''
        deletes selected row(s) from table identified by filter(s)
        e.g. command: DELETE FROM playground WHERE type = 'monkey_bar';
             delete_from_table("playground", "type = 'monkey_bar' AND location = 'south'");
        '''
        _command = f"DELETE FROM {table_name} WHERE {filter}"
        self.execute_sql_command(_command)
        
    def update_table(self, table_name, field, value, filter):
        '''
        updates a single value from row(s) in a table identified by filter(s)
        e.g. command: UPDATE playground SET type = 'monkey_bar' WHERE color = 'yellow' AND location = 'northwest';
             update_table("playground", "type", "monkey_bar", "color = 'yellow' AND location = 'northwest'"); 
        '''
        _command = f"UPDATE {table_name} SET {field} = '{value}' WHERE {filter}"
        self.execute_sql_command(_command)