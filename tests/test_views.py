from django.test import TestCase, Client
from django.urls import reverse

class TravelPlatformViewsTest(TestCase):
    def setUp(self):
        # Създава виртуален клиент (браузър) за заявките
        self.client = Client()

    def test_home_page_status_code(self):
        # reverse('home') автоматично ще намери пътя '' (началната страница)
        url = reverse('home')
        response = self.client.get(url)
        
        # Проверява дали страницата връща статус 200 (Успех)
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        url = reverse('home')
        response = self.client.get(url)
        
        # Проверява дали се използва правилният HTML шаблон
        # Заменете 'home.html' с истинското име на вашия HTML файл за тази страница
        self.assertTemplateUsed(response, 'posts/home.html')
