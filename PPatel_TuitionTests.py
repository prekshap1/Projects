from PPatel_tuition import calculate_tuition

def test_calculate_tuition():
    # Test cases for resident, no differential tuition
    assert calculate_tuition(0, True, False) == 0.0
    assert calculate_tuition(1, True, False) == 822.0
    assert calculate_tuition(8, True, False) == 3391.0
    

    # Test cases for resident, differential tuition
    assert calculate_tuition(0, True, True) == 0.0
    assert calculate_tuition(1, True, True) == 940.0
    assert calculate_tuition(8, True, True) == 4335.0
    

    # Test cases for nonresident, no differential tuition
    assert calculate_tuition(0, False, False) == 0.0
    assert calculate_tuition(1, False, False) == 1911.0
    assert calculate_tuition(8, False, False) == 12103.0


    # Test cases for nonresident, differential tuition
    assert calculate_tuition(0, False, True) == 0.0
    assert calculate_tuition(1, False, True) == 2029.0
    assert calculate_tuition(8, False, True) == 13047.0
   

    print("All tests passed!")

test_calculate_tuition()
