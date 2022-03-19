from Infrastructure.repo import DepartmentRepository
from domain.department import Department
from domain.patient import Patient


def test_listSize():
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
    assert repo.listSize() == 5
    assert repo1.listSize() == 2
    assert repo2.listSize() == 1
    assert repo3.listSize() == 1
    assert repo4.listSize() == 1
test_listSize()



def test_getDepartments():
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
    assert repo.getDepartments() == [d,d1,d2,d3,d4]
    assert repo1.getDepartments() == [d3,d4]
    assert repo2.getDepartments() == [d2]
    assert repo3.getDepartments() == [d1]
    assert repo4.getDepartments() == [d]
test_getDepartments()


def test_getDepartmentByIndex():
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

    assert repo.getDepartmentByIndex(4) == d4
    assert repo1.getDepartmentByIndex(1) == d4
    assert repo2.getDepartmentByIndex(0) == d2
    assert repo3.getDepartmentByIndex(0) == d1
    assert repo4.getDepartmentByIndex(0) == d
test_getDepartmentByIndex()


def test_deleteDepartmentByIndex():
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

    assert repo.listSize() == 5
    repo.deleteDepartmentByIndex(4)
    assert repo.listSize() == 4
    repo.deleteDepartmentByIndex(2)
    assert repo.listSize() == 3
    repo.deleteDepartmentByIndex(0)
    assert repo.listSize() == 2
    repo.deleteDepartmentByIndex(0)
    assert repo.listSize() == 1
    repo.deleteDepartmentByIndex(0)
    assert repo.listSize() == 0
test_deleteDepartmentByIndex()

def test_updateDepartmentByIndex():
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
    repo.updateDepartmentByIndex(0,"dep1",22,[p6,p7])
    assert d.getName() == "dep1"
    assert d.getNoBeds() == 22
    assert d.getPatientList() == [p6,p7]
    repo.updateDepartmentByIndex(1,"dep2",66,[p1])
    assert d1.getName() == "dep2"
    assert d1.getNoBeds() == 66
    assert d1.getPatientList() == [p1]
test_updateDepartmentByIndex()

def test_sortPatByCNPGivenIndex():
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
    assert d.getPatientList() == [p1,p3,p2]
    repo.sortPatByCNPGivenIndex(1)
    assert d1.getPatientList() == [p4]
    repo.sortPatByCNPGivenIndex(2)
    assert d2.getPatientList() == [p6,p5]
    repo.sortPatByCNPGivenIndex(3)
    assert d3.getPatientList() == [p7,p8]
    repo.sortPatByCNPGivenIndex(4)
    assert d4.getPatientList() == [p9]
test_sortPatByCNPGivenIndex()


def test_sortDepByNoPatients():
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
    p10 = Patient("Oana","Pop",7463542345,"disease")
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
    assert repo.getDepartmentByIndex(0) == d4
    assert repo.getDepartmentByIndex(1) == d1
    assert repo.getDepartmentByIndex(2) == d2
    assert repo.getDepartmentByIndex(3) == d
    assert repo.getDepartmentByIndex(4) == d3
test_sortDepByNoPatients()


def test_sortDepByPatientsLimit():
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
    assert repo.getDepartmentByIndex(0) == d1
    assert repo.getDepartmentByIndex(1) == d2
    assert repo.getDepartmentByIndex(2) == d
test_sortDepByPatientsLimit()





def test_sortPatientsByFirstName():
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
    assert repo.getDepartmentByIndex(0) == d1
    assert repo.getDepartmentByIndex(1) == d2
    assert repo.getDepartmentByIndex(2) == d
    assert d1.getPatientList() == [p4]
    assert d2.getPatientList() == [p6,p5]
    assert d.getPatientList() == [p3,p1,p2]
test_sortPatientsByFirstName()

def test_mySearchByAge():
    repo = DepartmentRepository()
    p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
    p2 = Patient("Amalia", "Postolache", 1770405060708, "fever")
    p3 = Patient("Cosmin", "Pop", 2783377263546, "dis")
    p4 = Patient("Oana", "Popa", 6020304050607, "gastr")
    p5 = Patient("Ioana", "Man", 6072716346278, "d")
    p6 = Patient("Ale", "Gal", 1661234567899, "fracture")
    d = Department(12,"neurology",4,[p1])
    d1 = Department(23,"dep",55,[p4,p5])
    d2 = Department(43,"d",23,[p2,p3])
    d3 = Department(45,"dep3",15,[p6])
    repo.addDepartments(d)
    repo.addDepartments(d1)
    repo.addDepartments(d2)
    repo.addDepartments(d3)
    lst = repo.mySearchByAge(44)
    assert lst[0].getName() == "dep"
    assert lst[0].getId() == 23
    assert lst[0].getNoBeds() == 55
    assert lst[0].getPatientList() == [p4,p5]
    assert lst[1].getName() == "d"
    assert lst[1].getId() == 43
    assert lst[1].getNoBeds() == 23
    assert lst[1].getPatientList() == [p2,p3]
test_mySearchByAge()




def test_mySearchGivenString():
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
    list = repo.mySearchGivenString(0,"Pop")
    assert list[0].getFirst() == "Maria"
    assert list[1].getFirst() == "Cosmin"
    assert list[2].getFirst() == "Oana"
    assert list[0].getLast() == "Popescu"
    assert list[1].getLast() == "Pop"
    assert list[2].getLast() == "Popa"
test_mySearchGivenString()




def test_searchByFirstName():
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
    assert name_repo[0].getName() == "department1"
    assert name_repo[1].getName() == "department2"
    assert name_repo[2].getName() == "department4"
    assert name_repo[0].getId() == 15
    assert name_repo[1].getId() == 12
    assert name_repo[2].getId() == 14
test_searchByFirstName()
