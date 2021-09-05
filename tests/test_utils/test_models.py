from django.test import TestCase
from utils.models import PhoneField
from unittest import mock
import pytest


# Tips:
# refresh_from_db() if you delete or update a field from a model instance
# validators are caled with clean methods


class PhoneFieldTestCase(TestCase):

    def test_validate_phone_1(self):
        p = PhoneField.objects.create(phone="999999999")
        p.full_clean()
        p.save()
        p.refresh_from_db()
        p = PhoneField.objects.all()
        assert p[0].phone == '999999999'

    def test_validate_phone_2(self):
        p = PhoneField.objects.create(phone="000000000")
        p.full_clean()
        p.save()
        p.refresh_from_db()
        p = PhoneField.objects.all()
        assert p[0].phone == '000000000'
    
    def test_validate_phone_3(self):
        p = PhoneField.objects.create(phone="9999999999999")
        p.full_clean()
        p.save()
        p.refresh_from_db()
        p = PhoneField.objects.all()
        assert p[0].phone == '9999999999999'

    def test_validate_phone_4(self):
        p = PhoneField.objects.create(phone="0000000000000")
        p.full_clean()
        p.save()
        p.refresh_from_db()
        p = PhoneField.objects.all()
        assert p[0].phone == '0000000000000'

    def test_validate_phone_5(self):
        p = PhoneField.objects.create(phone=999999999)
        p.full_clean()
        p.save()
        p.refresh_from_db()
        p = PhoneField.objects.all()
        assert p[0].phone == '999999999'

    @pytest.mark.xfail
    def test_validate_phone_6(self):
        p = PhoneField.objects.create(phone=000000000) # int(000000000) = str(0)
        p.full_clean()
        p.save()
        p.refresh_from_db()
        p = PhoneField.objects.all()
        assert p[0].phone == '000000000'
    
    def test_validate_phone_7(self):
        p = PhoneField.objects.create(phone=9999999999999)
        p.full_clean()
        p.save()
        p.refresh_from_db()
        p = PhoneField.objects.all()
        assert p[0].phone == '9999999999999'

    @pytest.mark.xfail
    def test_validate_phone_8(self):
        p = PhoneField.objects.create(phone=0000000000000) # int(0000000000000) = str(0)
        p.full_clean()
        p.save()
        p.refresh_from_db()
        p = PhoneField.objects.all()
        assert p[0].phone == '0000000000000'
    
    @pytest.mark.xfail
    def test_validate_phone_9(self):
        p = PhoneField.objects.create(phone="9")
        p.full_clean()
        p.save()
        p.refresh_from_db()
        p = PhoneField.objects.all()
        assert p[0].phone == '999999999'

    @pytest.mark.xfail
    def test_validate_phone_10(self):
        p = PhoneField.objects.create(phone="0")
        p.full_clean()
        p.save()
        p.refresh_from_db()
        p = PhoneField.objects.all()
        assert p[0].phone == '999999999'
    
    @pytest.mark.xfail
    def test_validate_phone_11(self):
        p = PhoneField.objects.create(phone=99999999999999)
        p.full_clean()
        p.save()
        p.refresh_from_db()
        p = PhoneField.objects.all()
        assert p[0].phone == '99999999999999'

    @pytest.mark.xfail
    def test_validate_phone_12(self):
        p = PhoneField.objects.create(phone=00000000000000)
        p.full_clean()
        p.save()
        p.refresh_from_db()
        p = PhoneField.objects.all()
        assert p[0].phone == '00000000000000'