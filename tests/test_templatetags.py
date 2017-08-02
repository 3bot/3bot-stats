"""Tests for the templatetags of the threebot_stats app."""
from django.test import TestCase

from threebot_stats.templatetags.threebot_stats_tags import avg_response_time


class DummyModelTestCase(TestCase):
    def test_index(self):
        self.assertTrue(True)
