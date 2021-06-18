import psycopg2 as pg2

import sys
sys.path.append('..')
import model_utils as utls



class EmployeesTypeTable:
    
    @staticmethod
    def insert_type(conn_info, type_info):
        conn = None
        cur = None
        inserted = False
        
        try:
            conn = pg2.connect(conn_info)
            cur = conn.cursor()
            cur.execute('''
		INSERT INTO employee_type 
                (emp_type_name, description, date_added, date_modified)
                VALUES (%(emp_type_name)s, %(description)s, %(date_added)s, %(date_modified)s)''', 
                type_info)
            conn.commit()
            inserted = True
        
        except pg2.Error as e:
            conn.rollback()
            print(e)
            # TODO: the error needs to be saved to log table
        
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

        return inserted


    @staticmethod
    def get_type_info(conn_info, type_id):
        conn = None
        cur = None
        type_info = None

        col_names = utls.get_column_names(conn_info, 'employee_type')

        try:
            conn = pg2.connect(conn_info)
            cur = conn.cursor()
            cur.execute('''
		SELECT * FROM employee_type WHERE emp_type_id=%s''', 
                str(type_id))
            type_info = utls.keyval_tuples2dict(col_names, cur.fetchone())
        
        except pg2.Error as e:
            print(e)
            # TODO: the error needs to be saved to log table
        
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

        return type_info


    @staticmethod
    def get_type_info_all(conn_info):
        conn = None
        cur = None
        type_info_all = None

        col_names = utls.get_column_names(conn_info, 'employee_type')

        try:
            conn = pg2.connect(conn_info)
            cur = conn.cursor()
            cur.execute('''SELECT * FROM employee_type''')
            records = utls.list_tuples2tuple_lists(cur.fetchall())
            type_info_all = utls.keyval_tuples2dict(col_names, records)

        except pg2.Error as e:
            print(e)
            # TODO: the error needs to be saved to log table

        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

        return type_info_all

        

    @staticmethod
    def update_type_info(conn_info, type_info):
        conn = None
        cur = None
        updated = False
        
        try:
            conn = pg2.connect(conn_info)
            cur = conn.cursor()
            cur.execute('''
		UPDATE employee_type SET
			emp_type_name = %(emp_type_name)s,
                        description = %(description)s,
                        date_modified = %(date_modified)s
                WHERE emp_type_id = %(emp_type_id)s''', 
                type_info)
            conn.commit()
            updated = True
        
        except pg2.Error as e:
            conn.rollback()
            print(e)
            # TODO: the error needs to be saved to log table
        
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

        return updated
        


    @staticmethod
    def delete_type(conn_info, type_id):
        conn = None
        cur = None
        deleted = False
        
        try:
            conn = pg2.connect(conn_info)
            cur = conn.cursor()
            cur.execute('''
		DELETE FROM employee_type
		WHERE emp_type_id = %s''', 
                str(type_id))
            conn.commit()
            deleted = True
        
        except pg2.Error as e:
            conn.rollback()
            print(e)
            # TODO: the error needs to be saved to log table
        
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

        return deleted
