from django.test import TestCase
from home.views import get_index
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from accounts.models import User

# Create your tests here.


class HomePageTest(TestCase):
    def test_home_page_resolves(self):  # URL Test
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)

    def test_home_page_status_code_is_ok(self):  # Testing views - correct status code
        home_page = self.client.get('/')
        self.assertEquals(home_page.status_code, 200)

    def setUp(self):
        super(HomePageTest, self).setUp()
        self.user = User.objects.create(username='test_user')  # Test logged in view
        self.user.set_password('let_me_in')
        self.user.save()
        self.login = self.client.login(username='test_user', password='let_me_in')
        self.assertEqual(self.login, True)

    def test_check_content_is_correct(self):  # Testing views - correct content & template
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, 'index.html')
        home_page_template_output = render_to_response('index.html', {'user': self.user}).content
        self.assertEquals(home_page.content, home_page_template_output)
