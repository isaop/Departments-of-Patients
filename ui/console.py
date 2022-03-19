from Infrastructure.repo import DepartmentRepository
from Infrastructure.utils import permute
from domain.department import Department
from domain.patient import Patient


class DepUI:
    def __init__(self,prepo):
        self.__repo = prepo

    @staticmethod
    def printMenu():
        mess = "Menu: \n"
        mess += "\t 1 - Get all departments \n"
        mess += "\t 2 - Add a department to the repository \n"
        mess += "\t 3 - Get a department at a given index \n"
        mess += "\t 4 - Update department given index \n"
        mess += "\t 5 - Delete department by index\n "
        mess += "\t 6 - Sort the patients in a given department by personal numerical code \n"
        mess += "\t 7 - Sort departments by the number of patients \n"
        mess += "\t 8 - Sort departments  by the  number  of  patients having  the  age  above  a  given  limit\n"
        mess += "\t 9 - Sort  departments  by  the  number  of  patients  and  the  patients  in  a  department alphabetically  \n"
        mess += "\t 10 - Identify departments where there are patients under a given age \n"
        mess += "\t 11 - Identify  patients  from  a  given  department  for  which  the  first  name  or  last  name contain a given string \n"
        mess += "\t 12 - Identify department/departments where there are patients with a given first name\n"
        mess += "\t 13 - Form groups  of k patients  from  the  same  department  and  the  same  disease \n"
        mess += "\t 14 - Form  groups  of k departments having  at  most p patients  suffering  from  the  same disease \n"

        print(mess)


    def printDepartments(self):
        print("Department list is: ")
        for dep in self.__repo.getData():
            print(dep)

    @staticmethod
    def readPatient():
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        try:
            cnp = int(input("Enter personal numerical code: "))
        except ValueError as e:
            print("Value error.. ")
            print(e)
        disease = input("Enter disease: ")
        try:
            return Patient(first_name,last_name,cnp,disease)
        except ValueError as e:
            print("Value error.. ")
            print(e)
    @staticmethod
    def readDepartment():

        try:
            id = int(input("Enter id of department: "))
        except:
            id = 0
        try:
            name = input("Enter name of department: ")
        except:
            name = "NoName"
        try:
            no_beds = int(input("Enter number of beds: "))
        except:
            no_beds = 0
        patientsList = []
        n = int(input("Enter number of patients: "))
        for i in range(n):
            try:
                currentPatient = DepUI.readPatient()
            except ValueError as e:
                print("Value Error ... ")
                print(e)
            patientsList.append(currentPatient)
        return Department(id,name,no_beds,patientsList)

    def start(self):
        while True:
            DepUI.printMenu()
            option = input("Enter option: ")
            if option == "1":
                self.printDepartments()
            elif option == "2":
                dep = DepUI.readDepartment()
                try:
                    self.__repo.addDepartments(dep)
                except ValueError as ex:
                    print("Value error...")
                    print(ex)
            elif option == "3":
                try:
                    given_index = int(input("Give an index: "))
                    print(self.__repo.getDepartmentByIndex(given_index))
                except ValueError as e:
                    print("Error...")
                    print(e)
            elif option == "4":
                try:
                    given_index = int(input("Enter index: "))
                    new_name = input("Enter new name: ")
                    new_no_beds = int(input("Enter the new number of beds: "))
                    new_patients_list = []
                    n = int(input("Enter new number of patients: "))
                    for i in range(n):
                        currentPatient = DepUI.readPatient()
                        new_patients_list.append(currentPatient)
                    self.__repo.updateDepartmentByIndex(given_index, new_name, new_no_beds, new_patients_list)
                except ValueError as e:
                    print("Error...")
                    print(e)
            elif option == "5":
                try:
                    given_index = int(input("Give an index: "))
                    self.__repo.deleteDepartmentByIndex(given_index)
                except ValueError as e:
                    print("Error...")
                    print(e)
            elif option == "6":
                try:
                    given_index = int(input("Enter index of department: "))
                    self.__repo.sortPatByCNPGivenIndex(given_index)
                except ValueError as e:
                    print("Error...")
                    print(e)
            elif option == "7":
                self.__repo.sortDepByNoPatients()
            elif option == "8":
                limit = int(input("Enter age limit: "))
                self.__repo.sortDepByPatientsLimit(limit)
            elif option == "9":
                self.__repo.sortDepByNoPatients()
                self.__repo.sortPatientsByFirstName()
                self.__repo.sortPatientsByLastName()
            elif option == "10":
                age = int(input("Enter limit age: "))
                deps = self.__repo.mySearchByAge(age)
                for dep in deps:
                    print(dep)
            elif option == "11":
                try:
                    given_index = int(input("Enter index of department: "))
                except ValueError as e:
                    print("Error...")
                    print(e)
                given_string = input("Enter string: ")
                for patient in self.__repo.mySearchGivenString(given_index,given_string):
                    print(patient)
            elif option == "12":
                given_first_name = input("Enter first name: ")
                deps = self.__repo.searchByFirstName(given_first_name)
                for dep in deps:
                    print(dep)
            elif option == "13":
                try:
                    given_index = int(input("Enter index of department: "))
                except ValueError as e:
                    print("Error...")
                    print(e)
                disease = input("Enter disease: ")
                k = int(input("Enter k: "))
                print(self.__repo.myFormGroupsSameDisease(k,given_index,disease))
            elif option == "14":
                disease = input("Enter disease: ")
                p = int(input("Enter p: "))
                k = int(input("Enter k: "))
                lst = self.__repo.formGroupsAtMostP(disease,p)
                print(permute(k,lst))


            elif option == "0":
                print("Exit...")
                break
            else:
                print("Option unknown!")



