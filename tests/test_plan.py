def inc(x):
    return x + 1

def test_answer():
    assert inc(4) == 5

def test_clickshare_warranty():
    # ==Given== `Check your ClickShare warranty` page is displayed
    # ==When== User input `serial number` to get warranty info
    # ==Then== Warranty result for `serial number` is displayed
    # ==And== Verify `Warranty end date` exists in the warranty result
    raise Exception('failure')

if __name__ == '__main__':
    test_clickshare_warranty()