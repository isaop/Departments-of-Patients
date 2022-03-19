import unittest
from unittest import TestCase

from Infrastructure.repo import DepartmentRepository
from app.controller import DepartmentController
from domain.department import Department
from domain.patient import Patient


class TestDepartmentController(TestCase):

    def setUp(self):
        p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
        p2 = Patient("Amalia", "Postolache", 1770405060708, "fever")
        p3 = Patient("Maria", "Pop", 2783377263546, "covid")
        p4 = Patient("Oana", "Popa", 6020304050607, "gastr")
        p5 = Patient("Ioana", "Man", 6072716346278, "d")
        p6 = Patient("Ale", "Gal", 1661234567899, "fracture")
        p7 = Patient("Paul", "Bota", 1762434245167, "g")
        p8 = Patient("Catalin", "Maier", 6045555555555, "a")
        d1 = Department(2, 'surgery', 22, [p1, p2])
        d2 = Department(3, 'neuro', 6, [p3])
        d3 = Department(3, "dep", 44, [p4, p5])
        d4 = Department(1,"dep11", 13,[p6,p7,p8])
        self.empty_controller = DepartmentController(DepartmentRepository())
        self.department_controller = DepartmentController(([d1]))
        self.d3dep_controller = DepartmentController(([d2,d3,d4]))
        self.d1dep = Department(7,"d",22,[p8])

    def testCreate(self):
        self.assertEqual(len(self.empty_controller.getDepartments()), 0)
        self.assertEqual(len(self.department_controller.getDepartments()), 1)
        self.assertEqual(len(self.d3dep_controller.getDepartments()), 3)

        self.assertEqual(str(self.empty_controller), "[]")
        self.assertEqual(str(self.department_controller),"[Department: surgery"
                                                         "            id: 2"
                                                         "            number of beds: 22"
                                                         "            patients: Patient: Maria Popescu, cnp: 2760321057060, with disease: disease"
                                                         "                      Patient: Amalia Postolache, cnp: 1770405060708, with disease: fever]")

    def testGetVectorGivenIndex(self):
        p1 = Patient("Maria", "Popescu", 2760321057060, "disease")
        p2 = Patient("Amalia", "Postolache", 1770405060708, "fever")
        p4 = Patient("Oana", "Popa", 6020304050607, "gastr")
        p5 = Patient("Ioana", "Man", 6072716346278, "d")
        d = self.department_controller.getDepartmentByIndex(0)
        self.assertEqual(d.getName(), "surgery")
        self.assertEqual(d.getId(), 2)
        self.assertEqual(d.getNoBeds(), 22)
        self.assertEqual(d.getPatientList(), [p1,p2])

        d1 = self.d3dep_controller.getDepartmentByIndex(1)
        self.assertEqual(d1.getName(), "dep")
        self.assertEqual(d1.getId(), 3)
        self.assertEqual(d1.getNoBeds(), 44)
        self.assertEqual(d1.getPatientList(),[p4,p5])

    def testDeleteByIndex(self):
        self.assertEqual(len(self.department_controller),1)
        self.department_controller.deleteDepartmentByIndex(0)
        self.assertEqual(len(self.department_controller),0)

        self.assertEqual(len(self.d3dep_controller),3)
        self.d3dep_controller.deleteDepartmentByIndex(0)
        self.assertEqual(len(self.d3dep_controller),2)
        self.d3dep_controller.deleteDepartmentByIndex(1)
        self.assertEqual(len(self.d3dep_controller),1)
        self.d3dep_controller.deleteDepartmentByIndex(0)
        self.assertEqual(len(self.d3dep_controller),0)



