import sys
sys.path.insert(1, '..\\..')

import unittest
import datetime
from AutomationTools import *

DATABASE_NAME = "postgres"
SERVER_USERNAME = "postgres"
SERVER_PASSWORD = "CassiAdmin!"
SERVER_IP = "127.0.0.1"
SERVER_PORT = "5432"
SQL_COMMAND_SELECT_ALL_FIELDS = "SELECT * FROM playground WHERE type = 'swing'"
SQL_COMMAND_SELECT_ALL_FIELDS_RESULT = [(2, 'swing', 'yellow', 'northwest', datetime.date(2018, 8, 16))]
SQL_COMMAND_CHECK_TABLE_EXISTS = "SELECT * FROM pg_tables WHERE tablename = 'student_record'"

TABLE_NAME_NEW = "student_record"
TABLE_FIELDS_NEW = [
        {'field_name': 'NAME', 'field_type': 'TEXT', 'options': ['NOT NULL']},
        {'field_name': 'AGE', 'field_type': 'INT', 'options': ['NOT NULL']},
        {'field_name': 'COURSE', 'field_type': 'CHAR(50)'},
        {'field_name': 'DEPARTMENT', 'field_type': 'CHAR(50)'},
    ]

TABLE_NAME = "playground"

TABLE_FIELDS_ALL = "*"
TABLE_FIELDS_1 = ["type", "color"]
TABLE_FIELDS_2 = ["color", "COUNT(*)"]
TABLE_FIELDS_3 = ["type", "color", "location", "install_date"]
TABLE_FIELDS_4 = "type"

TABLE_VALUES_3 = ['monkey_bar', 'white', 'south', '2019-12-12']
TABLE_VALUES_4 = "monkey_bar"
TABLE_VALUES_5 = "seesaw"

TABLE_FILTER = "color = 'yellow'"
TABLE_FILTER_2 = "type = 'monkey_bar' AND location = 'south'"
TABLE_FILTER_4 = "type = 'seesaw'"
TABLE_FILTER_5 = "type = 'monkey_bar'"

TABLE_GROUP_BY = ["color"]

TABLE_ORDER_BY = ["install_date"]

SELECT_FROM_TABLE_FILTER_ORDER_RESULT = [('seesaw', 'yellow'), ('swing', 'yellow')]
SELECT_FROM_TABLE_GROUP_BY_RESULT = [('yellow', 2), ('blue', 1)]
SELECT_FROM_TABLE_INSERT_RESULT = [('monkey_bar', 'white')]
SELECT_FROM_TABLE_UPDATE_RESULT = [('monkey_bar',)]

def test_decorator(func):
    def print_test_description(*func_args, **func_kwargs):
        print('================')
        print(f'Executing {func.__name__}'.upper())
        print('================')
        return func(*func_args, **func_kwargs)
    return print_test_description

class UnitTestPostgreSQL(unittest.TestCase):
    @test_decorator
    def test_execute_sql_command(self):
        '''
        Test for execute_sql_command() method
        '''
        postgresql_tool = PostgreSQLTools(DATABASE_NAME, SERVER_USERNAME, SERVER_PASSWORD, SERVER_IP, SERVER_PORT)
        resp = postgresql_tool.execute_sql_command(SQL_COMMAND_SELECT_ALL_FIELDS)
        self.assertEqual(resp, SQL_COMMAND_SELECT_ALL_FIELDS_RESULT, f"Execute SQL command failed or yielded incorrect value. Expected {SQL_COMMAND_SELECT_ALL_FIELDS_RESULT} got {resp}.")
    
    @test_decorator
    def test_create_delete_table(self):
        '''
        Test for create_table() and delete_table() method
        '''
        postgresql_tool = PostgreSQLTools(DATABASE_NAME, SERVER_USERNAME, SERVER_PASSWORD, SERVER_IP, SERVER_PORT)
        postgresql_tool.create_table(TABLE_NAME_NEW, TABLE_FIELDS_NEW)
        
        resp = postgresql_tool.execute_sql_command(SQL_COMMAND_CHECK_TABLE_EXISTS)
        self.assertEqual(len(resp), 1, 'Table not created.')
        
        postgresql_tool.delete_table(TABLE_NAME_NEW)
        resp = postgresql_tool.execute_sql_command(SQL_COMMAND_CHECK_TABLE_EXISTS)
        self.assertEqual(len(resp), 0, 'Table not deleted.')
    
    @test_decorator
    def test_select_from_table_filter_order(self):
        '''
        Test for select_from_table() method with filtering and ordering clause
        '''        
        postgresql_tool = PostgreSQLTools(DATABASE_NAME, SERVER_USERNAME, SERVER_PASSWORD, SERVER_IP, SERVER_PORT)
        resp = postgresql_tool.select_from_table(TABLE_NAME, TABLE_FIELDS_1, filter = TABLE_FILTER, order_by = TABLE_ORDER_BY, desc = True)
        self.assertEqual(resp, SELECT_FROM_TABLE_FILTER_ORDER_RESULT, f"Execute SQL command failed or yielded incorrect value. Expected {SELECT_FROM_TABLE_FILTER_ORDER_RESULT} got {resp}.")
        
    @test_decorator
    def test_select_from_table_group_by(self):
        '''
        Test for select_from_table() method with group_by clause
        '''        
        postgresql_tool = PostgreSQLTools(DATABASE_NAME, SERVER_USERNAME, SERVER_PASSWORD, SERVER_IP, SERVER_PORT)
        resp = postgresql_tool.select_from_table(TABLE_NAME, TABLE_FIELDS_2, grouping = TABLE_GROUP_BY)
        self.assertEqual(resp, SELECT_FROM_TABLE_GROUP_BY_RESULT, f"Execute SQL command failed or yielded incorrect value. Expected {SELECT_FROM_TABLE_FILTER_ORDER_RESULT} got {resp}.")        
        
    @test_decorator
    def test_insert_delete_from_table(self):
        '''
        Test for insert_into_table() and delete_from_table() method
        '''
        postgresql_tool = PostgreSQLTools(DATABASE_NAME, SERVER_USERNAME, SERVER_PASSWORD, SERVER_IP, SERVER_PORT)
        postgresql_tool.insert_into_table(TABLE_NAME, TABLE_FIELDS_3, TABLE_VALUES_3)
        resp = postgresql_tool.select_from_table(TABLE_NAME, TABLE_FIELDS_1, filter = TABLE_FILTER_2)
        self.assertEqual(resp, SELECT_FROM_TABLE_INSERT_RESULT, f"Entry unsuccessfully added to table.")
        
        postgresql_tool.delete_from_table(TABLE_NAME, TABLE_FILTER_2)
        resp = postgresql_tool.select_from_table(TABLE_NAME, TABLE_FIELDS_1, filter = TABLE_FILTER_2)
        self.assertEqual(resp, [], f"Entry unsuccessfully deleted. Expected [] got {resp}.")
    
    @test_decorator
    def test_update_table(self):
        '''
        Test for update_table() method
        '''
        postgresql_tool = PostgreSQLTools(DATABASE_NAME, SERVER_USERNAME, SERVER_PASSWORD, SERVER_IP, SERVER_PORT)
        postgresql_tool.update_table(TABLE_NAME, TABLE_FIELDS_4, TABLE_VALUES_4, TABLE_FILTER_4)
        resp = postgresql_tool.select_from_table(TABLE_NAME, TABLE_FIELDS_4, filter = TABLE_FILTER_5)
        self.assertEqual(resp, SELECT_FROM_TABLE_UPDATE_RESULT, f"Unable to update record. Expected {SELECT_FROM_TABLE_UPDATE_RESULT}, got {resp}.")
        
        postgresql_tool.update_table(TABLE_NAME, TABLE_FIELDS_4, TABLE_VALUES_5, TABLE_FILTER_5)
        resp = postgresql_tool.select_from_table(TABLE_NAME, TABLE_FIELDS_4, filter = TABLE_FILTER_5)
        self.assertEqual(resp, [], f"Unable to update record. Expected [], got {resp}.")
        
if __name__ == '__main__':
    unittest.main()