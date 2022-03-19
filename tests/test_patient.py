
from domain.patient import Patient


def test_create():
    p = Patient("Maria","Popescu",6606363636363,"dis")
    assert p.getFirst() == "Maria"
    assert p.getLast() == "Popescu"
    assert p.getCnp() == 6606363636363
    assert p.getDisease() == "dis"
    p.setFirst("Marius")
    assert p.getFirst() == "Marius"
    p.setLast("Popa")
    assert p.getLast() == "Popa"
    p.setCnp(1805454545454)
    assert p.getCnp() == 1805454545454
    p.setDisease("disease")
    assert p.getDisease() == "disease"

    p1 = Patient("Tudor","Gal",6038888888888,"fever")
    assert p1.getFirst() == "Tudor"
    assert p1.getLast() == "Gal"
    assert p1.getCnp() == 6038888888888
    assert p1.getDisease() == "fever"
    p1.setFirst("Marius")
    assert p1.getFirst() == "Marius"
    p1.setLast("Popa")
    assert p1.getLast() == "Popa"
    p1.setCnp(6010955555555)
    assert p1.getCnp() == 6010955555555
    p1.setDisease("disease")
    assert p1.getDisease() == "disease"

    p2 = Patient("Oana","Popa" , 6020304050607, "gastr")
    assert p2.getFirst() == "Oana"
    assert p2.getLast() == "Popa"
    assert p2.getCnp() == 6020304050607
    assert p2.getDisease() == "gastr"
    p2.setFirst("Paul")
    assert p2.getFirst() == "Paul"
    p2.setLast("Maier")
    assert p2.getLast() == "Maier"
    p2.setCnp(6010955555555)
    assert p2.getCnp() == 6010955555555
    p2.setDisease("fever")
    assert p2.getDisease() == "fever"

    p3 = Patient("Oana", "Popa", 6020304050607, "gastr")
    assert p3.getFirst() == "Oana"
    assert p3.getLast() == "Popa"
    assert p3.getCnp() == 6020304050607
    assert p3.getDisease() == "gastr"
    p3.setFirst("Paul")
    assert p3.getFirst() == "Paul"
    p3.setLast("Maier")
    assert p3.getLast() == "Maier"
    p3.setCnp(6010955555555)
    assert p3.getCnp() == 6010955555555
    p3 .setDisease("fever")
    assert p3.getDisease() == "fever"

    p3 = Patient("Raul", "M", 6020304050607, "dis")
    assert p3.getFirst() == "Raul"
    assert p3.getLast() == "M"
    assert p3.getCnp() == 6020304050607
    assert p3.getDisease() == "dis"
    p3.setFirst("Maria")
    assert p3.getFirst() == "Maria"
    p3.setLast("Nan")
    assert p3.getLast() == "Nan"
    p3.setCnp(1790955555555)
    assert p3.getCnp() == 1790955555555
    p3.setDisease("dis")
    assert p3.getDisease() == "dis"
test_create()



