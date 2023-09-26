from PPatel_NotePositions import get_fret, get_frets

def test_get_fret_same_target_and_string():
    result = get_fret("A", "A")
    assert result == 0

def test_get_fret_target_larger_than_string():
    result = get_fret("C", "A")
    assert result == 3

def test_get_fret_target_smaller_than_string():
    result = get_fret("A", "C")
    assert result == 9

def test_get_fret_sharp_and_flat():
    result_sharp = get_fret("G#", "G")
    result_flat = get_fret("Ab", "G")
    assert result_sharp == result_flat

def test_get_frets_single_string():
    result = get_frets("C", ["G"])
    assert len(result) == 1
    assert result["G"] == 7

def test_get_frets_multiple_strings():
    result = get_frets("E", ["G", "D", "A"])
    assert len(result) == 3
    assert result["G"] == 5
    assert result["D"] == 2
    assert result["A"] == 9

# Run the tests
test_get_fret_same_target_and_string()
test_get_fret_target_larger_than_string()
test_get_fret_target_smaller_than_string()
test_get_fret_sharp_and_flat()
test_get_frets_single_string()
test_get_frets_multiple_strings()

# Print success message if all tests passed
print("All tests passed!")
