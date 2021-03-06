from django.test import TestCase
from myapp.models import *
from myapp.views import *
import unittest
from django.test import Client
import json
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
        response = self.client.get('/search_dimensions?content=119')
        self.failUnlessEqual(response.status_code, 200)


    def test_test_list(self):
        self.client = Client()
        response = self.client.get('/test_list?uId=78')
        self.failUnlessEqual(response.status_code, 200)


    def test_search_stat(self):
        self.client = Client()
        response = self.client.get('/search_stat?tId=1')
        self.failUnlessEqual(response.status_code, 200)


    def test_all_questions(self):
        self.client = Client()
        response = self.client.get('/search_all_questions?tId=1')
        self.failUnlessEqual(response.status_code, 200)


    def test_question(self):
        self.client = Client()
        response = self.client.get('/edit_question?qId=171')
        self.failUnlessEqual(response.status_code, 200)


    def test_by(self):
        self.client = Client()
        response = self.client.get('/search_atest_by?tId=1')
        self.failUnlessEqual(response.status_code, 200)


    def test_search_all_atest(self):
        self.client = Client()
        response = self.client.post("/search_all_atest/",json.dumps({"uId" : 1 
        }), content_type="application/json")
        self.failUnlessEqual(response.status_code, 200)
    

    def test_create(self):
        self.client = Client()
        response = self.client.post("/create/",json.dumps({"tName" : "1223",'tDescribe' : "ssdsed",
        "uId" : 1 }), content_type="application/json")
        self.failUnlessEqual(response.status_code, 200)


    def test_set_dimension_page(self):
        self.client = Client()
        response = self.client.post("/set_dimension_page/",json.dumps({"tId" : 1 }), content_type="application/json")
        self.failUnlessEqual(response.status_code, 200)
        response = self.client.get('/load_result?tId=1')
    
    
    def test_delete_evaluation(self):
        self.client = Client()
        response = self.client.post("/delete_evaluation/",json.dumps({"tId" : 1 }), content_type="application/json")
        self.failUnlessEqual(response.status_code, 200)
    
    
    def test_update_atest(self):
        self.client = Client()
        response = self.client.post("/update_atest/",json.dumps({"tId" : 1 ,"evaluationName" : "12qw",
        "evaluationDescribe" : "12wdede"}), content_type="application/json")
        self.failUnlessEqual(response.status_code, 200)
    

    def test_delete_question(self):
        self.client = Client()
        response = self.client.post("/delete_question/",json.dumps({"qId" : 1 }), content_type="application/json")
        self.failUnlessEqual(response.status_code, 200)

    
    def test_create_dimension(self):
        self.client = Client()
        response = self.client.post("/create_dimension/",json.dumps({"tId" : 1 , "dimensions" : [{"dName": "sdsd"}]}), 
        content_type="application/json")
        self.failUnlessEqual(response.status_code, 200)
    

    def test_update_dimension(self):
        self.client = Client()
        response = self.client.post("/update_dimension/",
        json.dumps({"tId": 1, "qName": "asd", "oName": ["sdsd"], "score": [5], "dId": [5]}),
        content_type="application/json")
        self.failUnlessEqual(response.status_code, 200)
    

    def test_add_question(self):
        self.client = Client()
        response = self.client.post("/add_question/",
        json.dumps({"tId": 1, "qName": "asd", "oName": ["sdsd"], "score": [5], "dId": [5]}),
        content_type="application/json")
        self.failUnlessEqual(response.status_code, 200)


    def test_question_chat(self):
        self.client = Client()
        response = self.client.post("/question_chat/",
            json.dumps({"tId": 1, "qName": "asd", "oName": ["sdsd"], "score": [5], "dId": [5]}), 
            content_type="application/json")
        self.failUnlessEqual(response.status_code, 200)


    def test_update_question(self):
        self.client = Client()
        response = self.client.post("/update_question/",
            json.dumps({"qId": 1 , "newQuestionName": "asd", "newOptionData": [{"oName": "asdas", "score": 4, "dId": 1}]}), 
            content_type="application/json")
        self.failUnlessEqual(response.status_code, 200)
    

    def test_update_dimension(self):
        self.client = Client()
        response = self.client.post("/update_dimension/",json.dumps({"tId" : 1 , "dimensionName" : [{"dName": "sdsd"}]}), 
        content_type="application/json")
        self.failUnlessEqual(response.status_code, 200)

    
    def test_edit_judge(self):
        self.client = Client()
        response = self.client.post("/edit_judge/",
        json.dumps({"tId" : 1 , "due": "2018-01-01", "judge" : ["sdsd"], "dimensionId": [1]}), 
        content_type="application/json")
        self.failUnlessEqual(response.status_code, 200)

    
    def test_search_judge(self):
        self.client = Client()
        response = self.client.get('/search_judge?tId=1')
        self.failUnlessEqual(response.status_code, 200)

    
    def test_show_atest(self):
        self.client = Client()
        response = self.client.get('/show_atest?tId=1')
        self.failUnlessEqual(response.status_code, 200)

    
    def test_add_record(self):
        self.client = Client()
        response = self.client.post("/add_record/",
            json.dumps({"tId" : 119 , "options" : [{"qId" : 173, "oId" : 220}]}), 
            content_type="application/json")
        self.failUnlessEqual(response.status_code, 200)
