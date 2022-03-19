import unittest

from domain.patient import Patient


class TestPatient(unittest.TestCase):
    def test_create(self):
        p = Patient("Maria", "Popescu", 6606363636363, "dis")
        self.assertEqual(p.getFirst() , "Maria")
        self.assertEqual(p.getLast() , "Popescu")
        self.assertEqual(p.getCnp() , 6606363636363)
        self.assertEqual(p.getDisease() , "dis")
        p.setFirst("Marius")
        self.assertEqual(p.getFirst() , "Marius")
        p.setLast("Popa")
        self.assertEqual(p.getLast() , "Popa")
        p.setCnp(1805454545454)
        self.assertEqual(p.getCnp() , 1805454545454)
        p.setDisease("disease")
        self.assertEqual(p.getDisease() , "disease")

        p1 = Patient("Tudor", "Gal", 6038888888888, "fever")
        self.assertEqual(p1.getFirst() , "Tudor")
        self.assertEqual(p1.getLast() , "Gal")
        self.assertEqual(p1.getCnp() , 6038888888888)
        self.assertEqual(p1.getDisease() , "fever")
        p1.setFirst("Marius")
        self.assertEqual(p1.getFirst() , "Marius")
        p1.setLast("Popa")
        self.assertEqual(p1.getLast() , "Popa")
        p1.setCnp(6010955555555)
        self.assertEqual(p1.getCnp() , 6010955555555)
        p1.setDisease("disease")
        self.assertEqual(p1.getDisease() , "disease")

        p2 = Patient("Oana", "Popa", 6020304050607, "gastr")
        self.assertEqual(p2.getFirst() , "Oana")
        self.assertEqual(p2.getLast() , "Popa")
        self.assertEqual(p2.getCnp() , 6020304050607)
        self.assertEqual(p2.getDisease() , "gastr")
        p2.setFirst("Paul")
        self.assertEqual(p2.getFirst() , "Paul")
        p2.setLast("Maier")
        self.assertEqual(p2.getLast() , "Maier")
        p2.setCnp(6010955555555)
        self.assertEqual(p2.getCnp() , 6010955555555)
        p2.setDisease("fever")
        self.assertEqual(p2.getDisease() , "fever")

        p3 = Patient("Oana", "Popa", 6020304050607, "gastr")
        self.assertEqual(p3.getFirst() , "Oana")
        self.assertEqual(p3.getLast() , "Popa")
        self.assertEqual(p3.getCnp() , 6020304050607)
        self.assertEqual(p3.getDisease() , "gastr")
        p3.setFirst("Paul")
        self.assertEqual(p3.getFirst() , "Paul")
        p3.setLast("Maier")
        self.assertEqual(p3.getLast() , "Maier")
        p3.setCnp(6010955555555)
        self.assertEqual(p3.getCnp() , 6010955555555)
        p3.setDisease("fever")
        self.assertEqual(p3.getDisease(), "fever")

        p3 = Patient("Raul", "M", 6020304050607, "dis")
        self.assertEqual(p3.getFirst() , "Raul")
        self.assertEqual(p3.getLast() , "M")
        self.assertEqual(p3.getCnp() , 6020304050607)
        self.assertEqual(p3.getDisease() , "dis")
        p3.setFirst("Maria")
        self.assertEqual(p3.getFirst() , "Maria")
        p3.setLast("Nan")
        self.assertEqual(p3.getLast() , "Nan")
        p3.setCnp(1790955555555)
        self.assertEqual(p3.getCnp() , 1790955555555)
        p3.setDisease("dis")
        self.assertEqual(p3.getDisease() , "dis")

if __name__ == "__main__":
    import sys;

    sys.argv = ['', 'Test.testName']
    unittest.main()