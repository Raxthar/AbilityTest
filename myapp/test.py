from django.test import TestCase
from myapp.models import Question, Option, ATest, Dimension
import unittest
from django.test import Client
# Create your tests here.


class ModelTest(TestCase):

    def setUp(self):
        ATest.objects.create(
            t_id=1, t_name="This one", t_describe="This discribe",
            u_id=1, t_status=0, t_due="2019-01-10")
        Dimension.objects.create(d_id=1, d_name="Out", t_id=1)
        Question.objects.create(q_id=1, q_name="Like eat what", t_id=1)
        Option.objects.create(o_id=1, o_name="Tomato", q_id=1, score=5, d_id=1)

    def test_atest_models(self):
        result = ATest.objects.get(t_name="This one")
        self.assertEqual(result.t_describe, "This discribe")
        self.assertEqual(result.t_status, 0)

    def test_dimension_models(self):
        result = Dimension.objects.get(d_name="Out")
        self.assertEqual(result.t_id, 1)

    def test_question_models(self):
        result = Question.objects.get(q_name="Like eat what")
        self.assertEqual(result.t_id, 1)

    def test_option_models(self):
        result = Option.objects.get(o_name="Tomato")
        self.assertEqual(result.q_id, 1)
        self.assertEqual(result.score, 5)
        self.assertEqual(result.d_id, 1)


class ViewTest(unittest.TestCase):
    def test_search_dimensions(self):
        self.client = Client()
        response = self.client.get('arch_dimensions?content=119')
        self.failUnlessEqual(response.status_code, 200)

