import sys
sys.path.append('..')
import model_utils as utls


class ErrorLogsTable:


    @staticmethod
    def insert_log(log_info):
        sql = '''
		INSERT INTO error_logs
                (call_path, function_name, line_number, error_name, description, date_added)
		VALUES (%(call_path)s, %(function_name)s, %(line_number)s, %(error_name)s, %(description)s, %(date_added)s) 
              '''

        query_params = {
		'sql' : sql,
		'sql_params' : log_info,
		'fetchable' : False
        }

        return utls.execute_query(query_params)



    @staticmethod
    def get_log_info(log_id):
        pass


    @staticmethod
    def get_log_info_all():
        col_names = utls.get_column_names('error_logs')
        sql = '''SELECT * FROM error_logs'''

        query_params = {
            'sql' : sql,
            'sql_params' : None,
            'fetchable' : True
        }

        result = utls.execute_query(query_params)
        if result['success']:
            result['data'] = utls.list_tuples2tuple_lists(result['data'])
            result['data'] = utls.keyval_tuples2dict(col_names, result['data'])

        return result


    @staticmethod
    def update_log_info(log_info):
        pass


    @staticmethod
    def delete_log(log_id):
        pass
