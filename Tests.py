import unittest

from BFS import *
from Knuth import *


class TestBFSForKnuthConjecture(unittest.TestCase):
    def setUp(self):
        self.init = 4
        self.goal = 5
        self.actions = KnuthActions
        self.search = BFS(self.init, self.goal, self.actions)

    def test_globals(self):
        default = namedtuple("default", "parent")(None)
        IterationLimit = 1000
        error_message = "Not Found or Iteration limit reached"

        self.assertEqual(default, BFS.default)
        self.assertEqual(IterationLimit, BFS.IterationLimit)
        self.assertEqual(error_message, BFS.error_message)

    def test_setting_of_iteration_limit(self):
        limit = 1200
        self.assertEqual(BFS.set_iteration_limit(limit), limit)

    def test_BFS(self):
        path = self.search.start()
        for x, y in zip(path, [4, 24, 4.898979485566356, 5]):
            self.assertAlmostEqual(x, y)

    def test_BFS_fail(self):
        self.init = 0
        self.goal = 1
        self.search = BFS(self.init, self.goal, self.actions)
        self.assertEqual(self.search.start(), BFS.error_message)

    def test_is_goal(self):
        self.search = BFS(self.init, self.goal, self.actions)
        self.assertEqual(self.search.is_goal(self.goal), True)

class TestKnuthActions(unittest.TestCase):
    def test_if_actions(self):
        assert len(KnuthActions) in [3, 4]

    def test_fact(self):
        self.assertEqual(fact(0), 0)
        self.assertEqual(fact(1), 1)
        self.assertEqual(fact(-1), 0)
        self.assertEqual(fact(4), 24.0)
        self.assertEqual(fact(2.5), None)
        self.assertEqual(fact(200), 200)

    def test_sqrt(self):
        self.assertEqual(sqrt(1), 1.0)
        self.assertEqual(sqrt(-1), 0)

    def test_floor(self):
        self.assertEqual(floor(-1.5), -2)
        self.assertEqual(floor(1.5), 1)

    def test_ceil_negative(self):
        self.assertEqual(ceil(-1.5), -1)
        self.assertEqual(ceil(1.5), 2)


def TestSuite():
    suite = unittest.TestSuite()
    suite.addTest(
        unittest.TestLoader().loadTestsFromTestCase(TestBFSForKnuthConjecture))
    suite.addTest(
        unittest.TestLoader().loadTestsFromTestCase(TestKnuthActions))
    return suite


if __name__ == '__main__':
    import coverage

    cov = coverage.Coverage()
    cov.start()

    # .. call your code ..
    unittest.TextTestRunner(verbosity=3).run(TestSuite())
    cov.stop()
    cov.save()

    cov.html_report(directory="CoverageReport")
