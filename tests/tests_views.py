"""Tests for the models of the threebot_stats app."""
from django.test import TestCase

from threebot_stats.views import index, detail


class DummyModelTestCase(TestCase):
    def test_index(self):
        index(None)
