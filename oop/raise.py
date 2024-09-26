class TestError(Exception):
    def __init__(self,msg):
        self.msg=msg
def testcase():
    if False:
        print("GM")
    else:
        try:
            raise TestError("Text Error")
        except TestError as err:
            print("Handling Error")
testcase()