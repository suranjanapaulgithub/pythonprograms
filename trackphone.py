import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+917908531611")
phone_number2 = phonenumbers.parse("+918370902049")
phone_number3 = phonenumbers.parse("+2349126344823")
phone_number4 = phonenumbers.parse("+918420105621")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1, "en"))
print(geocoder.description_for_number(phone_number2, "en"))
print(geocoder.description_for_number(phone_number3, "en"))
print(geocoder.description_for_number(phone_number4, "en"))