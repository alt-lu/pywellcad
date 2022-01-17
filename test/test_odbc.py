import unittest
import wellcad.com
from ._sample_path import SamplePath


class TestOdbc(unittest.TestCase, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Classic Sample.wcl"))

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_interpret_sql_statement(self):
        result = self.borehole.odbc.interpret_sql_statement("ENABLETRACE(TRUE)")
        self.assertTrue(result)
        self.fail("This doesn't seem to work at all, but still returns True.")


if __name__ == '__main__':
    unittest.main()
