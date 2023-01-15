from island import way, swim, door

def test_way():
    assert way("r") == False
    
def test_swimg():
    assert swim("s") == False
    
def test_door():
    assert door("y") == "You Win!"