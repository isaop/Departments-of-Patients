from Infrastructure.repo import DepartmentRepository
from domain.department import Department
from domain.patient import Patient


def test_dep():
    p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
    p2 = Patient("Amalia", "Postolache", 6030405060708, "fever")
    p3 = Patient("Cosmin", "Pop", 2803377263546, "covid")
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

    assert d.getId() == 12
    assert d.getName() == "department1"
    assert d.getNoBeds() == 9
    assert d.getPatientList() == [p1,p2,p3]
    d.setName("department2")
    assert d.getName() == "department2"
    d.setNoBeds(18)
    assert d.getNoBeds() == 18
    d.setPatientList([p2,p1,p4])
    assert d.getPatientList() == [p2,p1,p4]

    assert d1.getId() == 44
    assert d1.getName() == "neurology"
    assert d1.getNoBeds() == 17
    assert d1.getPatientList() == [p4]
    d1.setName("department2")
    assert d1.getName() == "department2"
    d1.setNoBeds(99)
    assert d1.getNoBeds() == 99
    d1.setPatientList([p2, p1])
    assert d1.getPatientList() == [p2, p1]

    assert d2.getId() == 23
    assert d2.getName() == "surgery"
    assert d2.getNoBeds() == 10
    assert d2.getPatientList() == [p5,p6]
    d2.setName("dep")
    assert d2.getName() == "dep"
    d2.setNoBeds(34)
    assert d2.getNoBeds() == 34
    d2.setPatientList([])
    assert d2.getPatientList() == []
test_dep()

def test_getNoPatients():
    p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
    p2 = Patient("Amalia", "Postolache", 6030405060708, "fever")
    p3 = Patient("Cosmin", "Pop", 2803377263546, "covid")
    p4 = Patient("Oana", "Popa", 6020304050607, "gastr")
    p5 = Patient("Ioana", "Man", 6072716346278, "d")
    p6 = Patient("Ale", "Gal", 1661234567899, "fracture")
    p7 = Patient("Paul","Bota", 1762434245167,"g")
    p8 = Patient("Catalin","Maier",6045555555555,"a")
    p9 = Patient("Alin","Pisa",60102899288903,"fever")
    d = Department(12, "department1", 9, [])
    d.addPatient(p1)
    d.addPatient(p2)
    d.addPatient(p3)
    d1 = Department(44, "neurology", 17, [])
    d1.addPatient(p4)
    d2 = Department(23, "surgery", 10, [])
    d2.addPatient(p5)
    d2.addPatient(p6)
    d3 = Department(11,"dep3",20,[])
    d3.addPatient(p7)
    d3.addPatient(p8)
    d4 = Department(21,"dep4",16,[])
    d4.addPatient(p9)
    assert d.getNoPatients() == 3
    assert d1.getNoPatients() == 1
    assert d2.getNoPatients() == 2
    assert d3.getNoPatients() == 2
    assert d4.getNoPatients() == 1

    assert d.getNoPatientsAboveLimit(18) == 3
    assert d1.getNoPatientsAboveLimit(21) == 1
    assert d2.getNoPatientsAboveLimit(1) == 2
    assert d3.getNoPatientsAboveLimit(60) == 2
    assert d4.getNoPatientsAboveLimit(80) == 1

    assert d.getPatientGivenIndex(0) == p1
    assert d1.getPatientGivenIndex(0) == p4
    assert d2.getPatientGivenIndex(1) == p6
    assert d3.getPatientGivenIndex(1) == p8
    assert d4.getPatientGivenIndex(0) == p9
test_getNoPatients()

def test_updatePatientGivenIndex():
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

    d.updatePatientGivenIndex(1,"Eee","Pppp","dis")
    assert p2.getFirst() == "Eee"
    assert p2.getLast() == "Pppp"
    assert p2.getDisease() == "dis"
    d1.updatePatientGivenIndex(0, "Alex", "Pppp", "dis1")
    assert p4.getFirst() == "Alex"
    assert p4.getLast() == "Pppp"
    assert p4.getDisease() == "dis1"
    d2.updatePatientGivenIndex(1, "Alexandra", "Ppop", "dis3")
    assert p6.getFirst() == "Alexandra"
    assert p6.getLast() == "Ppop"
    assert p6.getDisease() == "dis3"
    d3.updatePatientGivenIndex(1, "Marc", "Pop", "fever")
    assert p8.getFirst() == "Marc"
    assert p8.getLast() == "Pop"
    assert p8.getDisease() == "fever"
    d4.updatePatientGivenIndex(0, "Alin", "Al", "cdis")
    assert p9.getFirst() == "Alin"
    assert p9.getLast() == "Al"
    assert p9.getDisease() == "cdis"
test_updatePatientGivenIndex()

def test_deletePatientGivenIndex():
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

    assert len(d.getPatientList()) == 3
    d.deletePatientGivenIndex(2)
    assert len(d.getPatientList()) == 2
    d.deletePatientGivenIndex(0)
    assert len(d.getPatientList()) == 1
    d.deletePatientGivenIndex(0)
    assert len(d.getPatientList()) == 0

    assert len(d1.getPatientList()) == 1
    d1.deletePatientGivenIndex(0)
    assert len(d1.getPatientList()) == 0

    assert len(d2.getPatientList()) == 2
    d2.deletePatientGivenIndex(1)
    assert len(d2.getPatientList()) == 1
    d2.deletePatientGivenIndex(0)
    assert len(d2.getPatientList()) == 0

    assert len(d3.getPatientList()) == 2
    d3.deletePatientGivenIndex(1)
    assert len(d3.getPatientList()) == 1
    d3.deletePatientGivenIndex(0)
    assert len(d3.getPatientList()) == 0

    assert len(d4.getPatientList()) == 1
    d4.deletePatientGivenIndex(0)
    assert len(d4.getPatientList()) == 0
test_deletePatientGivenIndex()


