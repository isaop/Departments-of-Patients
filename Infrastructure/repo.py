from Infrastructure.utils import mySort, permute
from Infrastructure.utils import mySearch
from domain.department import Department


class DepartmentRepository:
    def __init__(self):
        '''
        Constructor
        '''
        self.__depList = []

    def listSize(self):
        return len(self.__depList)

    def getData(self):
        return self.__depList

    def __str__(self):
        '''
        Provides a string representation of the list of departments
        '''
        mess = " "
        if len(self.__depList) == 0:
            mess = "Empty list"
        else:
            for dep in self.__depList:
                mess += str(dep)
                mess += "\n"
        return mess

    def addDepartments(self, department : Department):
        '''
        Description: adds a department to the repository
        :param : department, of type Department
        '''
        for dep in self.__depList:
            if dep.getId() == department.getId():
                raise ValueError("Invalid ID!")
        try:
            self.__depList.append(department)
        except ValueError as e:
            print("Error...")
            print(e)
    def getDepartments(self):
        '''
        Description: getter method
        :return: returns all the departments
        '''
        return self.__depList
    def getDepartmentByIndex(self,given_index):
        '''
        Description: gets a department at a given index
        :param given_index:
        :return: department
        '''
        if given_index < 0 or given_index >= len(self.__depList):
            raise ValueError("Choose another index!")
        return self.__depList[given_index]

    def deleteDepartmentByIndex(self,given_index):
        '''
        Description: Deletes a department at a given index
        :param given_index:
        '''
        if given_index < 0 or given_index >= len(self.__depList):
            raise ValueError("Choose another index!")
        del(self.__depList[given_index])
    def updateDepartmentByIndex(self,given_index,new_name,new_no_beds,new_patients_list):
        '''
        Description: updates a department at a given index
        :param given_index:
        :param new_name:
        :param new_no_beds:
        :param new_patients_list:
        '''
        self.__depList[given_index].setName(new_name)
        self.__depList[given_index].setNoBeds(new_no_beds)
        self.__depList[given_index].setPatientList(new_patients_list)

    def sortPatByCNPGivenIndex(self,given_index):
        '''
        Description: sorts patients in a given department by index
        :param given_index:
        :return:
        '''
        if given_index < 0 or given_index >= len(self.__depList):
            raise ValueError("Choose another index!")
        self.__depList[given_index].sortPatientsByCNP()

    def sortDepByNoPatients(self):
        '''
        Description: sorts departments by number of patients
        '''
        return mySort(self.__depList,lambda x,y: x.getNoPatients() < y.getNoPatients())
    def sortDepByPatientsLimit(self,limit):
        '''
        Description: sorts departments by number of patients above a given age
        :param limit:
        '''
        return mySort(self.__depList,lambda x,y: x.getNoPatientsAboveLimit(limit) < y.getNoPatientsAboveLimit(limit))
    def sortPatientsByFirstName(self):
        '''
        Descrioption: sorts patients by their first name
        '''
        for dep in self.__depList:
            dep.sortPatientsFirstName()
    def sortPatientsByLastName(self):
        '''
        Description: sorts patients by their last name
        :return:
        '''
        for dep in self.__depList:
            dep.sortPatientsLastName()
    def mySearchByAge(self, age):
        '''
        Description: search function for patients under a given age
        :param age:
        :return: list of patients
        '''
        deps = []
        for dep in self.__depList:
            list = mySearch(dep.getPatientList(), lambda x: x.getAge() <= age )
            if len(list) != 0 :
                deps.append(dep)
        return deps
    def mySearchGivenString(self,given_index,given_string):
        '''
        Description: search function for patients which have a given strin in their first name
        :param given_index:
        :param given_string:
        :return: list of patients
        '''
        if given_index < 0 or given_index >= len(self.__depList):
            raise ValueError("Choose another index!")
        return self.__depList[given_index].searchByString(given_string)
    def searchByFirstName(self,given_first_name):
        '''
        Description: search function for patients given a first name
        :param given_first_name:
        :return: list of patients
        '''
        deps = []
        for dep in self.__depList:
            with_name = mySearch(dep.getPatientList(), lambda x: x.getFirst() == given_first_name)
            if len(with_name) != 0:
                deps.append(dep)
        return deps

    def myFormGroupsSameDisease(self,s,given_index,disease):
        '''
        Description: forms permutations of groups of patients with same disease
        :param s:
        :param given_index:
        :param disease:
        :return:
        '''
        lst = self.__depList[given_index].formGroupsSameDisease(disease)
        return permute(s, lst)
    def formGroupsAtMostP(self,disease,p):
        '''
        Description: forms group of departments with the number of patients with same disease lower than p
        :param disease:
        :param p:
        :return: list of departments
        '''
        lst = []
        for dep in self.__depList:
            if dep.howManyPatients(disease,p) == True:
                lst.append(dep)

