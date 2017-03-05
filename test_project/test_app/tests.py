from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class TestAppViewTests(TestCase):
    def test_index_view_with_no_inputs(self):
        self.client.get(reverse('test_app:index'))
