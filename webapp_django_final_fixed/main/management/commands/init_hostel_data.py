from django.core.management.base import BaseCommand
from main.models import Hostel
from django.utils import timezone

class Command(BaseCommand):
    help = 'Initialize the database with sample hostel data'

    def handle(self, *args, **kwargs):
        # Clear existing hostels
        Hostel.objects.all().delete()
        
        # Create sample hostels based on the cards in the index.html
        hostels = [
            {
                'name': 'NEW FRIENDS HOSTEL & BAR',
                'location': 'Valladolid, Mexico',
                'description': 'Located in the heart of Valladolid, this vibrant hostel offers a social atmosphere with a lively bar area. Perfect for solo travelers looking to make new connections. The hostel features comfortable dorm rooms, a communal kitchen, and organized social events.',
                'image_url': 'https://th.bing.com/th/id/OIP.tIE6BZyHg2CvfGU6iY_6aAHaE7?rs=1&pid=ImgDetMain',
                'rating': 8.9,
                'reviews_count': 739,
                'price_per_night': 25.00,
                'discount_percentage': 60,
                'amenities': 'Free WiFi, Breakfast Included, Bar, Communal Kitchen, Lockers, 24-Hour Reception, Air Conditioning, Tours & Activities'
            },
            {
                'name': 'Rivoli Cinema Hostel',
                'location': 'Porto, Portugal',
                'description': 'Housed in a historic cinema building, this unique hostel combines vintage charm with modern comfort. Each room is themed after a classic movie, creating a one-of-a-kind stay experience. Located near Porto\'s main attractions, it\'s the perfect base for exploring the city.',
                'image_url': 'https://media.timeout.com/images/103849378/image.jpg',
                'rating': 9.4,
                'reviews_count': 3656,
                'price_per_night': 30.00,
                'discount_percentage': 15,
                'amenities': 'Free WiFi, Movie Room, Breakfast Available, Communal Kitchen, Laundry Facilities, Terrace, Bicycle Rental, City Tours'
            },
            {
                'name': 'ELTARI Pine House',
                'location': 'Malang, Indonesia',
                'description': 'Nestled in the lush greenery of Malang, this eco-friendly hostel offers a peaceful retreat from the hustle and bustle of city life. The wooden architecture and natural surroundings create a serene atmosphere perfect for relaxation and connecting with nature.',
                'image_url': 'https://th.bing.com/th/id/OIP.SMYxFFkDBhaHq_e13RRqXwAAAA?rs=1&pid=ImgDetMain',
                'rating': 9.4,
                'reviews_count': 51,
                'price_per_night': 18.00,
                'discount_percentage': 25,
                'amenities': 'Free WiFi, Garden, Outdoor Terrace, Breakfast Included, Yoga Classes, Mountain Views, Eco-Friendly Facilities, Local Tours'
            },
            {
                'name': 'Sir Toby\'s Midtown',
                'location': 'Prague, Czech Republic',
                'description': 'A charming hostel with a cozy pub atmosphere in the heart of Prague. Sir Toby\'s offers a blend of historic charm and modern amenities, making it a favorite among travelers. The cellar pub is a great place to meet fellow travelers and enjoy local Czech beers.',
                'image_url': 'https://th.bing.com/th/id/OIP.xV4GhSsmmzny_2v9I15ZNAHaE8?rs=1&pid=ImgDetMain',
                'rating': 9.2,
                'reviews_count': 46,
                'price_per_night': 22.00,
                'discount_percentage': 20,
                'amenities': 'Free WiFi, Pub, Breakfast Available, Communal Kitchen, Book Exchange, Bicycle Rental, Laundry Facilities, Walking Tours'
            },
            {
                'name': 'Sloth Backpackers Hostel',
                'location': 'Monteverde, Costa Rica',
                'description': 'Surrounded by the lush cloud forests of Monteverde, this eco-hostel is perfect for nature lovers and adventure seekers. The hostel organizes daily tours to explore the rich biodiversity of the region and offers a relaxed atmosphere to unwind after a day of exploration.',
                'image_url': 'https://cf.bstatic.com/xdata/images/hotel/max1024x768/25505278.jpg?k=5e523714b5648de97798b81973b52d693ade61fff6314c33f8ac88ae28ae8fda&o=&hp=1',
                'rating': 8.5,
                'reviews_count': 744,
                'price_per_night': 20.00,
                'discount_percentage': 50,
                'amenities': 'Free WiFi, Hammocks, Jungle Views, Communal Kitchen, Tour Desk, Book Exchange, Outdoor Terrace, Sustainable Practices'
            }
        ]
        
        # Create the hostel objects
        for i, hostel_data in enumerate(hostels, 1):
            hostel = Hostel(
                name=hostel_data['name'],
                location=hostel_data['location'],
                description=hostel_data['description'],
                image_url=hostel_data['image_url'],
                rating=hostel_data['rating'],
                reviews_count=hostel_data['reviews_count'],
                price_per_night=hostel_data['price_per_night'],
                discount_percentage=hostel_data['discount_percentage'],
                amenities=hostel_data['amenities'],
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
            hostel.save()
            self.stdout.write(self.style.SUCCESS(f'Created hostel: {hostel.name}'))
        
        self.stdout.write(self.style.SUCCESS('Successfully initialized hostel data'))
