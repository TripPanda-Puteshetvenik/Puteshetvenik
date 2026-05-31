from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post

class PostModelTest(TestCase):
    
    def setUp(self):
        # 1. Създаваме тестов потребител, тъй като author е задължително поле
        self.user = User.objects.create_user(
            username='testuser', 
            password='password123'
        )
        
        # 2. Създаваме тестовия пост с вашите реални полета
        self.post = Post.objects.create(
            author=self.user,
            title='Екскурзия до Рим',
            body='Прекрасно пътуване за 3 дни.',
            location_name='Колизеума'
        )

    def test_post_creation(self):
        # Проверяваме дали обектът е създаден успешно и е от клас Post
        self.assertTrue(isinstance(self.post, Post))
        
        # Проверяваме дали заглавието и локацията са записани правилно
        self.assertEqual(self.post.title, 'Екскурзия до Рим')
        self.assertEqual(self.post.location_name, 'Колизеума')

    def test_post_default_values(self):
        # Проверяваме дали стойностите по подразбиране работят
        # Полето published трябва автоматично да е True, а views_count да е 0
        self.assertTrue(self.post.published)
        self.assertEqual(self.post.views_count, 0)
