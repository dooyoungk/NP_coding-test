def ipv4_address(address):
    ip_count = address.split('.')
    for i in ip_count:
        if int(i) > 255:
            address = False
        elif int(i) < 0:
            address = False
        elif len(i) != 4:
            address = False
        elif i[0] == 0:
            address = False
        else:
            pass    

    if '\n' in address:
        address = False          

def test_q():
    assert ipv4_address("") == False
    assert ipv4_address("127.0.0.1") == True
    assert ipv4_address("0.0.0.0") == True
    assert ipv4_address("255.255.255.255") == True
    assert ipv4_address("10.20.30.40") == True
    assert ipv4_address("10.256.30.40") == False
    assert ipv4_address("10.20.030.40") == False
    assert ipv4_address("127.0.1") == False
    assert ipv4_address("127.0.0.0.1") == False
    assert ipv4_address("..255.255") == False
    assert ipv4_address("127.0.0.1\n") == False
    assert ipv4_address("\n127.0.0.1") == False
    assert ipv4_address(" 127.0.0.1") == False
    assert ipv4_address("127.0.0.1 ") == False
    assert ipv4_address(" 127.0.0.1 ") == False    