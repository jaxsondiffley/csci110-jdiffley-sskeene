import airtime 
# completed in class
def test_main1():
    assert airtime.airtime([0, 1, 2, 3, 9, 10, 9])==2

def test_main2():
    assert airtime.airtime([0, 1, 2, 3, 3, 4, 5, 3, 1])==2
    
def test_main3():
    assert airtime.airtime([11, 12])==0