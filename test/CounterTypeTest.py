import unittest

from countertype import CounterType


class CounterTypeTest(unittest.TestCase):
    @unittest.expectedFailure
    def test_tags_must_contain_id(self) -> None:
        ct = CounterType()

        ct.put(
            item="ev1",
            tags={
                "_state": "RUNNING",
            },
        )

    def test_simple_find(self):
        ct = CounterType()

        ct.put(
            item="ev1",
            tags={
                "id": "ev1",
                "state": "RUNNING",
                "parent_id": "123",
                "deduplication_id": "a",
            },
        )
        ct.put(
            item="ev2",
            tags={
                "id": "ev2",
                "state": "STOPPED",
                "parent_id": None,
                "deduplication_id": "a",
            },
        )

        # Finding by a specific tag should work
        self.assertEqual(
            {"ev1"},
            ct.find(state="RUNNING"),
        )
        self.assertEqual(
            {"ev2"},
            ct.find(state="STOPPED"),
        )

        # Finding with None values should work as well
        self.assertEqual(
            {"ev1"},
            ct.find(parent_id="123"),
        )
        self.assertEqual(
            {"ev2"},
            ct.find(parent_id=None),
        )

        # Finding multiple matches should also get us results
        self.assertEqual(
            {"ev1", "ev2"},
            ct.find(deduplication_id="a"),
        )
