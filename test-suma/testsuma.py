from sumardosnumeros import sumar

def test_sumar_correcto():
    assert sumar(2, 3) == 5

# Esto fallará
def test_sumar_falla():
    assert sumar(2, 2) == 5