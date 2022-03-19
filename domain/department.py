from Infrastructure.utils import mySort, mySearch
from domain.patient import Patient


class Department:
    def __init__(self,id, name, no_beds, patientList):
        '''
        Constructor
        '''
        self.__id = id
        self.__name = name
        self.__no_beds = no_beds
        self.__patientList = patientList

    def getId(self):
        '''
        Description: getter method
        :return: returns the first name
        '''
        return self.__id
    def getName(self):
        '''
        Description: getter method
        :return: returns the last name
        '''
        return self.__name
    def getNoBeds(self):
        '''
        Description: getter method
        :return: returns the personal numerical code
        '''
        return self.__no_beds
    def getPatientList(self):
        '''
        Description: getter method
        :return: returns list of patients
        '''
        return self.__patientList

    def setId(self,id):
        '''
        Description: setter method
        :param id:
        :return: sets the id
        '''
        self.__idd = id
    def setName(self,name):
        '''
        Description: setter method
        :param name:
        :return: sets the name
        '''
        self.__name = name
    def setNoBeds(self,no_beds):
        '''
        Description: setter method
        :param no_beds:
        :return: sets the number of beds
        '''
        self.__no_beds = no_beds
    def setPatientList(self,new_patients_list):
        '''
        Description: setter method
        :param new_patients_list:
        :return: sets the number of patients
        '''
        self.__patientList = new_patients_list
    def addPatient(self, patient: Patient):
        '''
        Description: adds a patient to the patient list
        :param patient: of type Patient
        '''
        for pat in self.__patientList:
            if pat.getCnp() == patient.getCnp():
                raise ValueError("Invalid personal numerical code!")
        self.__patientList.append(patient)
    def getNoPatients(self):
        return len(self.__patientList)
    def getNoPatientsAboveLimit(self,limit):
        nr = 0
        for patient in self.__patientList:
            almost_age = ((patient.getCnp()) // 10000000000) % 100
            if almost_age<=21 and almost_age>=0:
                age = 2000 + almost_age
            else:
                if almost_age >= 22:
                    age = 1900 + almost_age
            if age >= limit:
                nr+=1
        return nr
    def getAge(self):
        for patient in self.__patientList:
            almost_age = ((patient.getCnp()) // 10000000000) % 100
            if almost_age<=21 and almost_age>=0:
                age = 2000 + almost_age
            else:
                if almost_age >= 22:
                    age = 1900 + almost_age

    def getPatientGivenIndex(self, given_index):
        '''
        Description: returns patient, given index
        :param given_index: positive number, lower than length of patient list
        :return: It returns a patient at a given index
        '''
        if given_index < 0 or given_index > len(self.__patientList):
            raise ValueError("Wrong index!")
        return self.__patientList[given_index]
    def updatePatientGivenIndex(self,given_index,first,last,disease):
        '''
        Description: updates a patient, given its index
        :param given_index:
        :param first:
        :param last:
        :param disease:
        '''
        if given_index < 0 or given_index > len(self.__patientList):
            raise ValueError("Wrong index!")
        self.__patientList[given_index].setFirst(first)
        self.__patientList[given_index].setLast(last)
        self.__patientList[given_index].setDisease(disease)
    def deletePatientGivenIndex(self,given_index):
        '''
        Description: deletes a patient at a given index
        :param given_index:
        :return:
        '''
        if given_index < 0 or given_index > len(self.__patientList):
            raise ValueError("Wrong index!")
        del self.__patientList[given_index]
    def __str__(self):
        '''
        Provides a string representation of a department
        '''
        mess = "Department: " + self.__name + "\n" "            id: " + str(self.__id) + "\n" "            number of beds: " + str(self.__no_beds) + "\n" "            patients: "
        if len(self.__patientList) == 0:
            mess += "No patients"
        else:
            for patient in self.__patientList:
                mess += str(patient)
                mess += "\n"
                mess += "                      "
        return mess
    def sortPatientsByCNP(self):
        '''
        Description: sorts patients by cnp
        :return: sorted list
        '''
        return mySort(self.__patientList,lambda x,y: x.getCnp() < y.getCnp())
    def sortPatientsFirstName(self):
        '''
        Description: sorts patients by their first name
        :return: sorted list
        '''
        return mySort(self.__patientList, lambda x,y: x.getFirst() < y.getFirst())
    def sortPatientsLastName(self):
        '''
        Description: sorts patients by their last name
        :return: sorted list
        '''
        return mySort(self.__patientList, lambda x,y: x.getLast() < y.getLast())
    def searchByAge(self, age):
        '''
        Description: searches for patients under a given age
        :param age:
        :return: list of patients
        '''
        lst = mySearch(self.__patientList, lambda x: x.getAge() <= age)
        for el in lst:
            print(el)
    def searchByString(self,given_string):
        '''
        Description: Searches for patients with a given string in their name
        :param given_string:
        :return: list of patients
        '''
        return mySearch(self.__patientList, lambda x: given_string in x.getFirst() or given_string in x.getLast())
    def formGroupsSameDisease(self,disease):
        '''
        Description: forms a group of patients with a same given disease
        :param disease:
        :return: list of patients
        '''
        listSameDisease = []
        for patient in self.__patientList:
            if patient.getDisease() == disease:
                listSameDisease.append(patient)
        for el in listSameDisease:
            print(el)
    def howManyPatients(self,disease,p):
        '''
        Description: counts how many patients in a department have the same given disease
        :param disease:
        :param p:
        :return:
        '''
        listSameDisease = []
        for patient in self.__patientList:
            if patient.getDisease() == disease:
                listSameDisease.append(patient)
        return len(listSameDisease) < p

