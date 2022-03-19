from Infrastructure.repo import DepartmentRepository
from domain.department import Department
from domain.patient import Patient


class DepartmentController():
    '''
        Controller class
    '''

    def __init__(self, department_repository: DepartmentRepository = DepartmentRepository()):
        '''
        Description: Constructor
        '''
        self.__department_repository = department_repository

    def __str__(self) -> str:
        '''
        Description: returns string representation of the controller
        '''
        return str(self.__department_repository)

    def addDepartments(self, patient: Patient):
        '''
        Description: Adds a department to the repository
        '''
        self.__department_repository.addDepartments(patient)

    def getDepartments(self):
        '''
        Description: returns the list from the repository
        '''
        return self.__department_repository.getDepartments()

    def getDepartment(self):
        '''
        Description: Returns repository
        '''
        return self.__department_repository

    def getDepartmentByIndex(self, given_index: int):
        '''
        Description: returns department, given its index
        :param given_index: positive number, lower than the length of the repository
        :return: It returns a department at a given index
        '''
        return self.__department_repository.getDepartmentByIndex(given_index)

    def deleteDepartmentByIndex(self,given_index:int):
        '''
        Description: Deletes a department, given its index
        :param given_index: positive number, lower than the length of the repository
        '''
        return self.__department_repository.deleteDepartmentByIndex(given_index)

    def updateDepartmentByIndex(self, given_index: int , new_name: str,new_no_beds: int,new_patients_list):
        '''
        Description: updates a departemnt, given its index
        :param given_index: positive number, lower than the length of the repository
        :param new_dep :
        '''
        return self.__department_repository.updateDepartmentByIndex(given_index,new_name,new_no_beds,new_patients_list)

    def sortPatByCNPGivenIndex(self, given_index: int):
        '''
        Description: updates a vector, given its name_id
        :param given_name_id:
        '''
        return self.__department_repository.sortPatByCNPGivenIndex(given_index)

    def sortDepByNoPatients(self):
        '''
        Description: Deletes a point, given its name_id
        :param given_name_id
        '''
        return self.__department_repository.sortDepByNoPatients()
    def sortDepByPatientsLimit(self,limit: int):
        '''
        Description: plots vectors to a chart
        :return:
        '''
        return self.__department_repository.sortDepByPatientsLimit(limit)
    def sortPatientsByFirstName(self):
        '''
        Description: Gets the vector which represents the sum of all vectors
        :return: vectors which represent the sum of all vectors
        '''
        return self.__department_repository.sortPatientsByFirstName()
    def sortPatientsByLastName(self):
        '''
        Description: Update all vectors having a given type by setting their colour to the same given value
        :param given_type:
        :param given_color:
        :return: the updated list
        '''
        self.__department_repository.sortPatientsByLastName()
    def mySearchByAge(self,age: int):
        '''
        :param age:
        :return:
        '''
        self.__department_repository.mySearchByAge(age)
    def mySearchGivenString(self,given_index: int,given_string: str):
        '''

        :param given_index:
        :param given_string:
        :return:
        '''
        self.__department_repository.mySearchGivenString(given_index,given_string)
    def searchByFirstName(self,given_first_name: str):
        '''

        :param given_first_name:
        :return:
        '''
        self.__department_repository.searchByFirstName(given_first_name)