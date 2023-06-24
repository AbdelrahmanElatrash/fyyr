from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from accounts.models import CustomUser
from .models import Venue ,Artist ,Show 



class TestFyyur(TestCase):

    def test_list_show_page(self):
        url=reverse('show_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # filed with this error staticfiles manifest entry for 'images/favicon.ico'  in django , solved by comment line 136 in setting.py

    def test_list_show_page_template(self):
        url=reverse('show_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'fyyur/show_list.html')
        self.assertTemplateUsed(response, '_base.html')
    


    @classmethod
    def setUpTestData(cls) -> None:
        cls.user=CustomUser.objects.create_user(
            username='test',
            email='teas@email.com',
            password='1234'
        ) # Manager isn't accessible via CustomUser instances

        cls.venue=Venue.objects.create(
            name='venu name',
            city='venu city',
            address=' venue addres',
            phone='452-485-412',
            img_link='https://images.unsplash.com/photo-1549213783-8284d0336c',
            facebook_link="https://www.facebook.com/GunsNPetals",
            genres=["Rock n Roll"],
            website_link="https://www.gunsnpetalsband.com",
            seeking_talent=True ,
            seeking_description="Looking for shows to perform at in the San "
            

        )

        cls.artist=Artist.objects.create(
            name="The Wild Sax Band",
            city="San Francisco",
            phone="432-325-5432",
            genres=["Jazz", "Classical"],
            img_link="https://images.unsplash.com/photo-1558369981-f9ca7846",
            facebook_link="https://www.facebook.com/GunsNPetals",
            seeking_venue=False,
            
        )

        cls.show=Show.objects.create(
            start_time="2019-05-21T21:30:00.000Z",
            venue=cls.venue,
            artist=cls.artist,
            admin=cls.user
        )



    def test_fields(self):
        self.assertIsInstance(self.show.start_time , str)
        self.assertIsInstance(self.show.admin , object)
        self.assertIsInstance(self.show.venue, object )
    

    def test_venue_detail_page_status_code(self):
        url = reverse('venue_detail',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_artist_detail_page_template(self):
        url = reverse('artist_detail',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'fyyur/artist_detail.html')
        self.assertTemplateUsed(response, '_base.html')



    def test_create_show_view(self):
        obj={
            'start_time':"2019-05-21T21:30:00.000Z",
            'venue': self.venue,
            'artist':self.artist,
            'admin':self.user,
        }

        url = reverse('create_show')
        response = self.client.post(path=url,data=obj,follow=True)
        self.assertEqual(response.status_code, 200)



    def test_update_venue(self):
        obj={
           'name':'venu name',
            'city':'venu city',
            'address':' venue addres',
            'phone':'452-485-412',
            'img_link':'https://images.unsplash.com/photo-1549213783-8284d0336c',
            'facebook_link':"https://www.facebook.com/GunsNPetals",
            'genres':["Rock n Roll"],
            'website_link':"https://www.gunsnpetalsband.com",
            'seeking_talent':True ,
            'seeking_description':"Looking for shows to perform at in the San "
        }

        url = reverse('update_venue',args=[self.venue.id])
        response = self.client.post(path=url,data=obj,follow=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_artist(self):
        url = reverse('delete_artist',args=[self.artist.id])
        response = self.client.delete(path=url,follow=True)
        self.assertRedirects(response, reverse('artist_list'))
        self.assertEqual(response.status_code, 200)