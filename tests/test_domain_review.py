import unittest

from src.harbor_tool_diff_mark.domain_review import DomainReview, review_lane, review_score


class DomainReviewTests(unittest.TestCase):
    def test_review_lane(self) -> None:
        item = DomainReview(55, 51, 27, 78)
        self.assertEqual(review_score(item), 158)
        self.assertEqual(review_lane(item), "ship")


if __name__ == "__main__":
    unittest.main()
