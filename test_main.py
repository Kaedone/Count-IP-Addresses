@Test.describe("Fixed tests")
def fixed_tests():
    test.assert_equals(ips_between("150.0.0.0", "150.0.0.1"), 1)
    test.assert_equals(ips_between("10.0.0.0", "10.0.0.50"), 50)
    test.assert_equals(ips_between("20.0.0.10", "20.0.1.0"), 246)
    test.assert_equals(ips_between("10.11.12.13", "10.11.13.0"), 243)
    test.assert_equals(ips_between("160.0.0.0", "160.0.1.0"), 256)
    test.assert_equals(ips_between("170.0.0.0", "170.1.0.0"), 65536)
    test.assert_equals(ips_between("50.0.0.0", "50.1.1.1"), 65793)
    test.assert_equals(ips_between("180.0.0.0", "181.0.0.0"), 16777216)
    test.assert_equals(ips_between("1.2.3.4", "5.6.7.8"), 67372036)


@Test.describe("Random tests")
def random_tests():
    from random import randint
    
    def to_ip(n):
        return ".".join([str((n//256**i)&255) for i in range(4)][::-1])
    
    for _ in range(50):
        a = randint(0, 256**4-1)
        b = a + randint(1, 10**randint(1, 10))
        b = min([b, 256**4-1])
        
        @test.it("Testing %s and %s, Expecting: %s" % (to_ip(a), to_ip(b), b-a))
        def single_test():
            test.assert_equals(ips_between(to_ip(a), to_ip(b)), b-a)
