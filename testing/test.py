try:
    from src.serverSide import machineStatus
    import unittest
except Exception as exe:
    print("Exception Occured {}".format(exe))

class FlaskAppTesting(unittest.TestCase):
      # test case to check if response is 200 or not
      def test_response(self):
          tester_one=machineStatus.test_client(self)
          responseTester_one=tester_one.get("/status/")
          statuscode = responseTester_one.status_code
          self.assertEqual(statuscode,200)

      # test to check if the content written return is in application/json format or not
      def test_contentType(self):
          tester_one = machineStatus.test_client(self)
          responseTester_one = tester_one.get("/status/")
          self.assertEqual(responseTester_one.content_type, "text/html; charset=utf-8") #application/json

      # test to check some data content in response
      def test_dataContent(self):
          tester_one = machineStatus.test_client(self)
          responseTester_one = tester_one.get("/status/")
          self.assertTrue(b'Machine_Name' in responseTester_one.data)


if __name__ == "__main__":
    unittest.main()






