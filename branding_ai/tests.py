from django.test import TestCase
from branding_ai.models import BrandingCategories
from django.utils import timezone
import datetime
# Create your tests here.


class BrandingCategoriesModelTests(TestCase):

    def test_was_published_recently_with_old_branding_categories(self):
        """
        was_published_recently() returns False for branding_categories whose created_at
        is older than 1 day.
        """
        old_branding_categories = BrandingCategories()
        old_branding_categories.category = "Test Cat"
        old_branding_categories.created_at = timezone.now(
        ) - datetime.timedelta(days=1, seconds=1)
        self.assertIs(old_branding_categories.was_published_recently(), False)

    def test_was_published_recently_with_recent_branding_categories(self):
        """
        was_published_recently() returns True for branding_categories whose created_at
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_branding_categories = BrandingCategories(created_at=time)
        self.assertIs(
            recent_branding_categories.was_published_recently(), True)

    def test_was_published_recently_with_future_branding_categories(self):
        """
        was_published_recently() returns False for branding_categories whose created_at
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_branding_categories = BrandingCategories(created_at=time)
        self.assertIs(
            future_branding_categories.was_published_recently(), False)

    def test_create_branding_categories(self):
        """
        create_branding_categories() returns True for branding_categories whose created_at
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        cat = BrandingCategories(created_at=time)
        cat.category = "Test Cat Recent"
        self.assertEqual(cat.category, "Test Cat Recent")

    def test_delete_branding_categories(self):
        """
        delete_branding_categories() returns True for deleted branding_categories successfully.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        cat = BrandingCategories(created_at=time)
        cat.category = "Test Cat Recent"

        BrandingCategories.objects.filter(id=cat.id).delete()

        deleted_cat = BrandingCategories.objects.filter(
            category=cat.category).first()

        self.assertIsNone(deleted_cat, msg="Category has been deleted")

    def test_update_branding_categories(self):
        """
        update_branding_categories() returns True for updated branding_categories successfully.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        cat = BrandingCategories(created_at=time)
        cat.category = "Test Cat Recent"

        cat.save()

        cat2 = BrandingCategories.objects.filter(
            category=cat.category).first()
        cat2.category = "Updated"
        cat2.save()

        updated_cat = BrandingCategories.objects.filter(    
            category=cat2.category).first()
        self.assertEqual(updated_cat.category,"Updated")
        
    def test_get_recent_branding_categories(self):
        """
        get recent branding_categories() returns list of branding_categories whose created_at is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        cat = BrandingCategories(created_at=time)
        cat.category = "Test Cat Recent"
        cat.save()

        recent_cats = BrandingCategories.get_recent_branding_categories()
        self.assertEqual(recent_cats[0].category, "Test Cat Recent")
        self.assertEqual(len(recent_cats), 1)
         
        