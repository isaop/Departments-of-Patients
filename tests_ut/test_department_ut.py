import unittest
from domain.department import Department
from domain.patient import Patient

class TestDep(unittest.TestCase):
    def test_dep(self):
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

        self.assertEqual(d.getId() , 12)
        self.assertEqual(d.getName() , "department1")
        self.assertEqual(d.getNoBeds() , 9)
        self.assertEqual(d.getPatientList() , [p1, p2, p3])
        d.setName("department2")
        self.assertEqual(d.getName() , "department2")
        d.setNoBeds(18)
        self.assertEqual(d.getNoBeds() , 18)
        d.setPatientList([p2, p1, p4])
        self.assertEqual(d.getPatientList() , [p2, p1, p4])

        self.assertEqual(d1.getId() , 44)
        self.assertEqual(d1.getName() , "neurology")
        self.assertEqual(d1.getNoBeds() , 17)
        self.assertEqual(d1.getPatientList() , [p4])
        d1.setName("department2")
        self.assertEqual(d1.getName() , "department2")
        d1.setNoBeds(99)
        self.assertEqual(d1.getNoBeds() , 99)
        d1.setPatientList([p2, p1])
        self.assertEqual(d1.getPatientList() , [p2, p1])

        self.assertEqual(d2.getId() , 23)
        self.assertEqual(d2.getName() , "surgery")
        self.assertEqual(d2.getNoBeds() , 10)
        self.assertEqual(d2.getPatientList() , [p5, p6])
        d2.setName("dep")
        self.assertEqual(d2.getName() , "dep")
        d2.setNoBeds(34)
        self.assertEqual(d2.getNoBeds() , 34)
        d2.setPatientList([])
        self.assertEqual(d2.getPatientList() , [])


    def test_getNoPatients(self):
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
        self.assertEqual(d.getNoPatients() , 3)
        self.assertEqual(d1.getNoPatients() , 1)
        self.assertEqual(d2.getNoPatients() , 2)
        self.assertEqual(d3.getNoPatients() , 2)
        self.assertEqual(d4.getNoPatients() , 1)

        self.assertEqual(d.getNoPatientsAboveLimit(18) , 3)
        self.assertEqual(d1.getNoPatientsAboveLimit(21) , 1)
        self.assertEqual(d2.getNoPatientsAboveLimit(1) , 2)
        self.assertEqual(d3.getNoPatientsAboveLimit(60) , 2)
        self.assertEqual(d4.getNoPatientsAboveLimit(80) , 1)

        self.assertEqual(d.getPatientGivenIndex(0) , p1)
        self.assertEqual(d1.getPatientGivenIndex(0) , p4)
        self.assertEqual(d2.getPatientGivenIndex(1) , p6)
        self.assertEqual(d3.getPatientGivenIndex(1) , p8)
        self.assertEqual(d4.getPatientGivenIndex(0) , p9)


    def test_updatePatientGivenIndex(self):
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

        d.updatePatientGivenIndex(1, "Eee", "Pppp", "dis")
        self.assertEqual(p2.getFirst() , "Eee")
        self.assertEqual(p2.getLast() , "Pppp")
        self.assertEqual(p2.getDisease() , "dis")
        d1.updatePatientGivenIndex(0, "Alex", "Pppp", "dis1")
        self.assertEqual(p4.getFirst() , "Alex")
        self.assertEqual(p4.getLast() , "Pppp")
        self.assertEqual( p4.getDisease() , "dis1")
        d2.updatePatientGivenIndex(1, "Alexandra", "Ppop", "dis3")
        self.assertEqual(p6.getFirst() ,"Alexandra")
        self.assertEqual(p6.getLast() , "Ppop")
        self.assertEqual(p6.getDisease() , "dis3")
        d3.updatePatientGivenIndex(1, "Marc", "Pop", "fever")
        self.assertEqual(p8.getFirst() ,"Marc")
        self.assertEqual(p8.getLast() , "Pop")
        self.assertEqual(p8.getDisease() , "fever")
        d4.updatePatientGivenIndex(0, "Alin", "Al", "cdis")
        self.assertEqual(p9.getFirst() , "Alin")
        self.assertEqual(p9.getLast() , "Al")
        self.assertEqual(p9.getDisease() , "cdis")


    def test_deletePatientGivenIndex(self):
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

        self.assertEqual(len(d.getPatientList()) , 3)
        d.deletePatientGivenIndex(2)
        self.assertEqual(len(d.getPatientList()) , 2)
        d.deletePatientGivenIndex(0)
        self.assertEqual(len(d.getPatientList()) , 1)
        d.deletePatientGivenIndex(0)
        self.assertEqual(len(d.getPatientList()) , 0)

        self.assertEqual(len(d1.getPatientList()) , 1)
        d1.deletePatientGivenIndex(0)
        self.assertEqual(len(d1.getPatientList()) , 0)

        self.assertEqual(len(d2.getPatientList()) , 2)
        d2.deletePatientGivenIndex(1)
        self.assertEqual(len(d2.getPatientList()) , 1)
        d2.deletePatientGivenIndex(0)
        self.assertEqual(len(d2.getPatientList()) , 0)

        self.assertEqual(len(d3.getPatientList()) , 2)
        d3.deletePatientGivenIndex(1)
        self.assertEqual(len(d3.getPatientList()) , 1)
        d3.deletePatientGivenIndex(0)
        self.assertEqual(len(d3.getPatientList()) , 0)

        self.assertEqual(len(d4.getPatientList()) , 1)
        d4.deletePatientGivenIndex(0)
        self.assertEqual(len(d4.getPatientList()) , 0)

if __name__ == "__main__":
    import sys;sys.argv=['','Test.testName']
    unittest.main()

