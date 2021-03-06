import unittest

from Infrastructure.repo import DepartmentRepository
from domain.department import Department
from domain.patient import Patient


class TestDepRepo(unittest.TestCase):
    def test_listSize(self):
        repo = DepartmentRepository()
        repo1 = DepartmentRepository()
        repo2 = DepartmentRepository()
        repo3 = DepartmentRepository()
        repo4 = DepartmentRepository()

        p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
        p2 = Patient("Amalia", "Postolache", 6030405060708, "fever")
        p3 = Patient("Cosmin", "Pop", 2803377263546, "covid")
        p4 = Patient("Oana", "Popa", 6020304050607, "gastr")
        p5 = Patient("Ioana", "Man", 6072716346278, "d")
        p6 = Patient("Ale", "Gal", 1661234567899, "fracture")
        p7 = Patient("Paul", "Bota", 1762434245167, "g")
        p8 = Patient("Catalin", "Maier", 6045555555555, "a")
        p9 = Patient("Alin", "Pisa", 60102899288903, "fever")
        d = Department(12, "department1", 9, [])
        d.addPatient(p1)
        d.addPatient(p2)
        d.addPatient(p3)
        d1 = Department(44, "neurology", 17, [])
        d1.addPatient(p4)
        d2 = Department(23, "surgery", 10, [])
        d2.addPatient(p5)
        d2.addPatient(p6)
        d3 = Department(11, "dep3", 20, [])
        d3.addPatient(p7)
        d3.addPatient(p8)
        d4 = Department(21, "dep4", 16, [])
        d4.addPatient(p9)
        repo.addDepartments(d)
        repo.addDepartments(d1)
        repo.addDepartments(d2)
        repo.addDepartments(d3)
        repo.addDepartments(d4)
        repo1.addDepartments(d3)
        repo1.addDepartments(d4)
        repo2.addDepartments(d2)
        repo3.addDepartments(d1)
        repo4.addDepartments(d)
        self.assertEqual(repo.listSize() , 5)
        self.assertEqual(repo1.listSize() , 2)
        self.assertEqual(repo2.listSize() , 1)
        self.assertEqual(repo3.listSize() , 1)
        self.assertEqual(repo4.listSize() , 1)


    def test_getDepartments(self):
        repo = DepartmentRepository()
        repo1 = DepartmentRepository()
        repo2 = DepartmentRepository()
        repo3 = DepartmentRepository()
        repo4 = DepartmentRepository()
        p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
        p2 = Patient("Amalia", "Postolache", 6030405060708, "fever")
        p3 = Patient("Cosmin", "Pop", 2803377263546, "covid")
        p4 = Patient("Oana", "Popa", 6020304050607, "gastr")
        p5 = Patient("Ioana", "Man", 6072716346278, "d")
        p6 = Patient("Ale", "Gal", 1661234567899, "fracture")
        p7 = Patient("Paul", "Bota", 1762434245167, "g")
        p8 = Patient("Catalin", "Maier", 6045555555555, "a")
        p9 = Patient("Alin", "Pisa", 60102899288903, "fever")
        d = Department(12, "department1", 9, [])
        d.addPatient(p1)
        d.addPatient(p2)
        d.addPatient(p3)
        d1 = Department(44, "neurology", 17, [])
        d1.addPatient(p4)
        d2 = Department(23, "surgery", 10, [])
        d2.addPatient(p5)
        d2.addPatient(p6)
        d3 = Department(11, "dep3", 20, [])
        d3.addPatient(p7)
        d3.addPatient(p8)
        d4 = Department(21, "dep4", 16, [])
        d4.addPatient(p9)
        repo.addDepartments(d)
        repo.addDepartments(d1)
        repo.addDepartments(d2)
        repo.addDepartments(d3)
        repo.addDepartments(d4)
        repo1.addDepartments(d3)
        repo1.addDepartments(d4)
        repo2.addDepartments(d2)
        repo3.addDepartments(d1)
        repo4.addDepartments(d)
        self.assertEqual(repo.getDepartments() , [d, d1, d2, d3, d4])
        self.assertEqual(repo1.getDepartments() , [d3, d4])
        self.assertEqual(repo2.getDepartments() , [d2])
        self.assertEqual(repo3.getDepartments() , [d1])
        self.assertEqual(repo4.getDepartments() , [d])


    def test_getDepartmentByIndex(self):
        repo = DepartmentRepository()
        repo1 = DepartmentRepository()
        repo2 = DepartmentRepository()
        repo3 = DepartmentRepository()
        repo4 = DepartmentRepository()
        p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
        p2 = Patient("Amalia", "Postolache", 6030405060708, "fever")
        p3 = Patient("Cosmin", "Pop", 2803377263546, "covid")
        p4 = Patient("Oana", "Popa", 6020304050607, "gastr")
        p5 = Patient("Ioana", "Man", 6072716346278, "d")
        p6 = Patient("Ale", "Gal", 1661234567899, "fracture")
        p7 = Patient("Paul", "Bota", 1762434245167, "g")
        p8 = Patient("Catalin", "Maier", 6045555555555, "a")
        p9 = Patient("Alin", "Pisa", 60102899288903, "fever")
        d = Department(12, "department1", 9, [])
        d.addPatient(p1)
        d.addPatient(p2)
        d.addPatient(p3)
        d1 = Department(44, "neurology", 17, [])
        d1.addPatient(p4)
        d2 = Department(23, "surgery", 10, [])
        d2.addPatient(p5)
        d2.addPatient(p6)
        d3 = Department(11, "dep3", 20, [])
        d3.addPatient(p7)
        d3.addPatient(p8)
        d4 = Department(21, "dep4", 16, [])
        d4.addPatient(p9)
        repo.addDepartments(d)
        repo.addDepartments(d1)
        repo.addDepartments(d2)
        repo.addDepartments(d3)
        repo.addDepartments(d4)
        repo1.addDepartments(d3)
        repo1.addDepartments(d4)
        repo2.addDepartments(d2)
        repo3.addDepartments(d1)
        repo4.addDepartments(d)

        self.assertEqual(repo.getDepartmentByIndex(4) , d4)
        self.assertEqual(repo1.getDepartmentByIndex(1) , d4)
        self.assertEqual(repo2.getDepartmentByIndex(0) , d2)
        self.assertEqual(repo3.getDepartmentByIndex(0) , d1)
        self.assertEqual(repo4.getDepartmentByIndex(0) , d)


    def test_deleteDepartmentByIndex(self):
        repo = DepartmentRepository()
        repo1 = DepartmentRepository()
        repo2 = DepartmentRepository()
        repo3 = DepartmentRepository()
        repo4 = DepartmentRepository()
        p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
        p2 = Patient("Amalia", "Postolache", 6030405060708, "fever")
        p3 = Patient("Cosmin", "Pop", 2803377263546, "covid")
        p4 = Patient("Oana", "Popa", 6020304050607, "gastr")
        p5 = Patient("Ioana", "Man", 6072716346278, "d")
        p6 = Patient("Ale", "Gal", 1661234567899, "fracture")
        p7 = Patient("Paul", "Bota", 1762434245167, "g")
        p8 = Patient("Catalin", "Maier", 6045555555555, "a")
        p9 = Patient("Alin", "Pisa", 60102899288903, "fever")
        d = Department(12, "department1", 9, [])
        d.addPatient(p1)
        d.addPatient(p2)
        d.addPatient(p3)
        d1 = Department(44, "neurology", 17, [])
        d1.addPatient(p4)
        d2 = Department(23, "surgery", 10, [])
        d2.addPatient(p5)
        d2.addPatient(p6)
        d3 = Department(11, "dep3", 20, [])
        d3.addPatient(p7)
        d3.addPatient(p8)
        d4 = Department(21, "dep4", 16, [])
        d4.addPatient(p9)
        repo.addDepartments(d)
        repo.addDepartments(d1)
        repo.addDepartments(d2)
        repo.addDepartments(d3)
        repo.addDepartments(d4)
        repo1.addDepartments(d3)
        repo1.addDepartments(d4)
        repo2.addDepartments(d2)
        repo3.addDepartments(d1)
        repo4.addDepartments(d)

        self.assertEqual(repo.listSize() , 5)
        repo.deleteDepartmentByIndex(4)
        self.assertEqual(repo.listSize() , 4)
        repo.deleteDepartmentByIndex(2)
        self.assertEqual(repo.listSize() , 3)
        repo.deleteDepartmentByIndex(0)
        self.assertEqual(repo.listSize(), 2)
        repo.deleteDepartmentByIndex(0)
        self.assertEqual(repo.listSize() , 1)
        repo.deleteDepartmentByIndex(0)
        self.assertEqual(repo.listSize() , 0)


    def test_updateDepartmentByIndex(self):
        repo = DepartmentRepository()
        p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
        p2 = Patient("Amalia", "Postolache", 6030405060708, "fever")
        p3 = Patient("Cosmin", "Pop", 2803377263546, "covid")
        p4 = Patient("Oana", "Popa", 6020304050607, "gastr")
        p5 = Patient("Ioana", "Man", 6072716346278, "d")
        p6 = Patient("Ale", "Gal", 1661234567899, "fracture")
        p7 = Patient("Paul", "Bota", 1762434245167, "g")
        p8 = Patient("Catalin", "Maier", 6045555555555, "a")
        p9 = Patient("Alin", "Pisa", 60102899288903, "fever")
        d = Department(12, "department1", 9, [])
        d.addPatient(p1)
        d.addPatient(p2)
        d.addPatient(p3)
        d1 = Department(44, "neurology", 17, [])
        d1.addPatient(p4)
        d2 = Department(23, "surgery", 10, [])
        d2.addPatient(p5)
        d2.addPatient(p6)
        d3 = Department(11, "dep3", 20, [])
        d3.addPatient(p7)
        d3.addPatient(p8)
        d4 = Department(21, "dep4", 16, [])
        d4.addPatient(p9)
        repo.addDepartments(d)
        repo.addDepartments(d1)
        repo.addDepartments(d2)
        repo.addDepartments(d3)
        repo.addDepartments(d4)
        repo.updateDepartmentByIndex(0, "dep1", 22, [p6, p7])
        self.assertEqual(d.getName() , "dep1")
        self.assertEqual(d.getNoBeds() , 22)
        self.assertEqual(d.getPatientList() , [p6, p7])
        repo.updateDepartmentByIndex(1, "dep2", 66, [p1])
        self.assertEqual(d1.getName() , "dep2")
        self.assertEqual(d1.getNoBeds() , 66)
        self.assertEqual(d1.getPatientList() , [p1])


    def test_sortPatByCNPGivenIndex(self):
        repo = DepartmentRepository()
        p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
        p2 = Patient("Amalia", "Postolache", 6030405060708, "fever")
        p3 = Patient("Cosmin", "Pop", 2803377263546, "covid")
        p4 = Patient("Oana", "Popa", 6020304050607, "gastr")
        p5 = Patient("Ioana", "Man", 6072716346278, "d")
        p6 = Patient("Ale", "Gal", 1661234567899, "fracture")
        p7 = Patient("Paul", "Bota", 1762434245167, "g")
        p8 = Patient("Catalin", "Maier", 6045555555555, "a")
        p9 = Patient("Alin", "Pisa", 60102899288903, "fever")
        d = Department(12, "department1", 9, [])
        d.addPatient(p1)
        d.addPatient(p2)
        d.addPatient(p3)
        d1 = Department(44, "neurology", 17, [])
        d1.addPatient(p4)
        d2 = Department(23, "surgery", 10, [])
        d2.addPatient(p5)
        d2.addPatient(p6)
        d3 = Department(11, "dep3", 20, [])
        d3.addPatient(p7)
        d3.addPatient(p8)
        d4 = Department(21, "dep4", 16, [])
        d4.addPatient(p9)
        repo.addDepartments(d)
        repo.addDepartments(d1)
        repo.addDepartments(d2)
        repo.addDepartments(d3)
        repo.addDepartments(d4)
        repo.sortPatByCNPGivenIndex(0)
        self.assertEqual(d.getPatientList() , [p1, p3, p2])
        repo.sortPatByCNPGivenIndex(1)
        self.assertEqual(d1.getPatientList() , [p4])
        repo.sortPatByCNPGivenIndex(2)
        self.assertEqual(d2.getPatientList() , [p6, p5])
        repo.sortPatByCNPGivenIndex(3)
        self.assertEqual(d3.getPatientList() , [p7, p8])
        repo.sortPatByCNPGivenIndex(4)
        self.assertEqual(d4.getPatientList() , [p9])


    def test_sortDepByNoPatients(self):
        repo = DepartmentRepository()
        p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
        p2 = Patient("Amalia", "Postolache", 6030405060708, "fever")
        p3 = Patient("Cosmin", "Pop", 2803377263546, "covid")
        p4 = Patient("Oana", "Popa", 6020304050607, "gastr")
        p5 = Patient("Ioana", "Man", 6072716346278, "d")
        p6 = Patient("Ale", "Gal", 1661234567899, "fracture")
        p7 = Patient("Paul", "Bota", 1762434245167, "g")
        p8 = Patient("Catalin", "Maier", 6045555555555, "a")
        p9 = Patient("Alin", "Pisa", 60102899288903, "fever")
        p10 = Patient("Oana", "Pop", 7463542345, "disease")
        d = Department(12, "department1", 9, [])
        d.addPatient(p1)
        d.addPatient(p2)
        d.addPatient(p3)
        d1 = Department(44, "neurology", 17, [])
        d1.addPatient(p4)
        d2 = Department(23, "surgery", 10, [])
        d2.addPatient(p5)
        d2.addPatient(p6)
        d3 = Department(11, "dep3", 20, [])
        d3.addPatient(p7)
        d3.addPatient(p8)
        d3.addPatient(p9)
        d3.addPatient(p10)
        d4 = Department(21, "dep4", 16, [])
        repo.addDepartments(d)
        repo.addDepartments(d1)
        repo.addDepartments(d2)
        repo.addDepartments(d3)
        repo.addDepartments(d4)

        repo.sortDepByNoPatients()
        self.assertEqual(repo.getDepartmentByIndex(0) , d4)
        self.assertEqual(repo.getDepartmentByIndex(1) , d1)
        self.assertEqual(repo.getDepartmentByIndex(2) , d2)
        self.assertEqual(repo.getDepartmentByIndex(3) , d)
        self.assertEqual(repo.getDepartmentByIndex(4) , d3)


    def test_sortDepByPatientsLimit(self):
        repo = DepartmentRepository()
        p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
        p2 = Patient("Amalia", "Postolache", 1770405060708, "fever")
        p3 = Patient("Cosmin", "Pop", 2783377263546, "covid")
        p4 = Patient("Oana", "Popa", 6020304050607, "gastr")
        p5 = Patient("Ioana", "Man", 6072716346278, "d")
        p6 = Patient("Ale", "Gal", 1661234567899, "fracture")
        d = Department(12, "department1", 9, [])
        d.addPatient(p1)
        d.addPatient(p2)
        d.addPatient(p3)
        d1 = Department(44, "neurology", 17, [])
        d1.addPatient(p4)
        d2 = Department(23, "surgery", 10, [])
        d2.addPatient(p5)
        d2.addPatient(p6)
        repo.addDepartments(d)
        repo.addDepartments(d1)
        repo.addDepartments(d2)
        repo.sortDepByPatientsLimit(21)
        self.assertEqual(repo.getDepartmentByIndex(0) , d1)
        self.assertEqual(repo.getDepartmentByIndex(1) , d2)
        self.assertEqual(repo.getDepartmentByIndex(2) , d)


    def test_sortPatientsByFirstName(self):
        repo = DepartmentRepository()
        p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
        p2 = Patient("Amalia", "Postolache", 1770405060708, "fever")
        p3 = Patient("Cosmin", "Pop", 2783377263546, "covid")
        p4 = Patient("Oana", "Popa", 6020304050607, "gastr")
        p5 = Patient("Ioana", "Man", 6072716346278, "d")
        p6 = Patient("Ale", "Gal", 1661234567899, "fracture")
        d = Department(12, "department1", 9, [])
        d.addPatient(p1)
        d.addPatient(p2)
        d.addPatient(p3)
        d1 = Department(44, "neurology", 17, [])
        d1.addPatient(p4)
        d2 = Department(23, "surgery", 10, [])
        d2.addPatient(p5)
        d2.addPatient(p6)
        repo.addDepartments(d)
        repo.addDepartments(d1)
        repo.addDepartments(d2)
        repo.sortDepByNoPatients()
        repo.sortPatientsByFirstName()
        repo.sortPatientsByLastName()
        self.assertEqual(repo.getDepartmentByIndex(0) , d1)
        self.assertEqual(repo.getDepartmentByIndex(1) , d2)
        self.assertEqual(repo.getDepartmentByIndex(2) , d)
        self.assertEqual(d1.getPatientList() , [p4])
        self.assertEqual(d2.getPatientList() , [p6, p5])
        self.assertEqual(d.getPatientList() , [p3, p1, p2])


    def test_mySearchByAge(self):
        repo = DepartmentRepository()
        p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
        p2 = Patient("Amalia", "Postolache", 1770405060708, "fever")
        p3 = Patient("Cosmin", "Pop", 2783377263546, "dis")
        p4 = Patient("Oana", "Popa", 6020304050607, "gastr")
        p5 = Patient("Ioana", "Man", 6072716346278, "d")
        p6 = Patient("Ale", "Gal", 1661234567899, "fracture")
        d = Department(12, "neurology", 4, [p1])
        d1 = Department(23, "dep", 55, [p4, p5])
        d2 = Department(43, "d", 23, [p2, p3])
        d3 = Department(45, "dep3", 15, [p6])
        repo.addDepartments(d)
        repo.addDepartments(d1)
        repo.addDepartments(d2)
        repo.addDepartments(d3)
        lst = repo.mySearchByAge(44)
        self.assertEqual(lst[0].getName() , "dep")
        self.assertEqual(lst[0].getId() , 23)
        self.assertEqual(lst[0].getNoBeds() , 55)
        self.assertEqual(lst[0].getPatientList() , [p4, p5])
        self.assertEqual(lst[1].getName() , "d")
        self.assertEqual(lst[1].getId() , 43)
        self.assertEqual(lst[1].getNoBeds() , 23)
        self.assertEqual(lst[1].getPatientList() , [p2, p3])


    def test_mySearchGivenString(self):
        repo = DepartmentRepository()
        p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
        p2 = Patient("Amalia", "Postolache", 1770405060708, "fever")
        p3 = Patient("Cosmin", "Pop", 2783377263546, "covid")
        p4 = Patient("Oana", "Popa", 6020304050607, "gastr")
        p5 = Patient("Ioana", "Man", 6072716346278, "d")
        d = Department(12, "department1", 9, [])
        d.addPatient(p1)
        d.addPatient(p2)
        d.addPatient(p3)
        d.addPatient(p4)
        d.addPatient(p5)
        repo.addDepartments(d)
        list = repo.mySearchGivenString(0, "Pop")
        self.assertEqual(list[0].getFirst() , "Maria")
        self.assertEqual(list[1].getFirst() , "Cosmin")
        self.assertEqual(list[2].getFirst() , "Oana")
        self.assertEqual(list[0].getLast() , "Popescu")
        self.assertEqual(list[1].getLast() , "Pop")
        self.assertEqual(list[2].getLast() , "Popa")


    def test_searchByFirstName(self):
        repo = DepartmentRepository()
        p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
        p2 = Patient("Amalia", "Postolache", 1770405060708, "fever")
        p3 = Patient("Maria", "Pop", 2783377263546, "covid")
        p4 = Patient("Oana", "Popa", 6020304050607, "gastr")
        p5 = Patient("Maria", "Man", 6072716346278, "d")
        d = Department(15, "department1", 4, [])
        d1 = Department(12, "department2", 9, [])
        d2 = Department(13, "department3", 5, [])
        d3 = Department(14, "department4", 10, [])
        d.addPatient(p1)
        d.addPatient(p2)
        d1.addPatient(p3)
        d2.addPatient(p4)
        d3.addPatient(p5)
        repo.addDepartments(d)
        repo.addDepartments(d1)
        repo.addDepartments(d2)
        repo.addDepartments(d3)
        name_repo = repo.searchByFirstName("Maria")
        self.assertEqual(name_repo[0].getName() , "department1")
        self.assertEqual(name_repo[1].getName() , "department2")
        self.assertEqual(name_repo[2].getName() , "department4")
        self.assertEqual(name_repo[0].getId() , 15)
        self.assertEqual(name_repo[1].getId() , 12)
        self.assertEqual(name_repo[2].getId() , 14)

if __name__ == "__main__":
    import sys;sys.argv=['','Test.testName']
    unittest.main()
