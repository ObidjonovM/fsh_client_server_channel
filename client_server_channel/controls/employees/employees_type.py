from client_server_channel.models import EmployeesTypeTable
from .. import control_utils as utls
from datetime import datetime


class EmployeeTypeC:

    @staticmethod
    def add(name, desc):
        now = datetime.now()
        add_result = EmployeesTypeTable.insert_type({
		'emp_type_name' : name,
		'description' : desc,
		'date_added' : now,
		'date_modified' : now
	})

        return {
            'success' : add_result['success'],
            'log_code' : utls.record_log(add_result, 'add', 'crud_logs')
        }
           
 
    @staticmethod
    def get(type_id):
        get_result = EmployeesTypeTable.get_type_info(type_id)
        
        return {
            'success' : get_result['success'],
            'data' : get_result['data'],
            'log_code' : utls.record_log(get_result, 'get', 'crud_logs')
        }


    @staticmethod
    def get_all():
        get_all_result = EmployeesTypeTable.get_type_info_all()

        return {
            'success' : get_all_result['success'],
            'data' : get_all_result['data'],
            'log_code' : utls.record_log(get_all_result, 'get_all','crud_logs')
        }


    @staticmethod
    def update(type_info):
        type_info['date_modified'] = datetime.now()
        update_result = EmployeesTypeTable.update_type_info(type_info)
        
        return {
            'success' : update_result['success'],
            'log_code' : utls.record_log(update_result, 'update', 'crud_logs')
        }


    @staticmethod
    def delete(type_id):
        get_result = EmployeesTypeTable.get_type_info(type_id)
        log_code = utls.record_log(get_result, 'delete', 'crud_clogs')
        if get_result['data'] != []:
            delete_result = EmployeesTypeTable.delete_type(type_id)
            return {
                'success' : delete_result['success'],
                'log_code' : utls.record_log(delete_result, 'delete', 'crud_logs')
            }
        
        return {
            'success' : False,
            'log_code' : log_code,
            'comment' : 'DOES NOT EXIST'   
        }


