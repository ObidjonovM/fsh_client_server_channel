from .. import crud


class DepartmentTable:

    @staticmethod
    def insert(dept_info):
        return crud.insert('departments', dept_info)


    @staticmethod
    def get(dept_id):
        return crud.get('departments', {'dept_id' : dept_id})


    @staticmethod
    def get_all():
        return crud.get_all('departments')


    @staticmethod
    def get_ids_names():
        return crud.get_ids_names('departments', 'dept_id', 'name')


    @staticmethod
    def get_names_by_ids(depts_ids):
        result = crud.get_columns_by_ids(
            'departments',
            ['dept_id', 'name'],
            'dept_id',
            depts_ids
        )

        if result['data'] != []:
            names_ids={}
            data = result['data']
            data_len = len(data['dept_id'])
            for i in range(data_len):
                names_ids[data['dept_id'][i]] = data['name'][i]

            result['data'] = names_ids

        return result


    @staticmethod
    def update(dept_info):
        return crud.update('departments', dept_info, 'dept_id')


    @staticmethod
    def delete(dept_id):
        return crud.delete('departments', {'dept_id' : dept_id})