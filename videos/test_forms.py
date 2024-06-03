from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):
    """ Adapted from Code Institute Walkthough Project"""

    def test_review_form_is_valid(self):
        """ Tests all required fields """
        review_form = ReviewForm({
            "title": "What did I just watch!?",
            "content": "I hated this movie.",
            })
        self.assertTrue(review_form.is_valid())

    def test_empty_review_form_is_invalid(self):
        """ Tests all required fields """
        review_form = ReviewForm({
            "title": "",
            "content": "",
            })
        self.assertFalse(review_form.is_valid())