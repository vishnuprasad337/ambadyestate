from .models import Blog, Testimonial, Category, GalleryImage
from django import forms


# --------- Blog Form ---------
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["image", "title", "description"]


# --------- Testimonial Form ---------
class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ["name", "image", "review", "rating"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class GalleryImageForm(forms.ModelForm):  # no need
    class Meta:
        model = GalleryImage
        fields = ["category", "title", "image"]


 
from .models import Room, RoomImage
 
 
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            "status",
            "room_category",
            "bedroom_beds",
            "living_room_beds",
            "description",
            "price_per_night",
            "main_image",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }
# --------- Multiple Gallery Images for a Room ---------

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

    def value_from_datadict(self, data, files, name):
        if hasattr(files, "getlist"):
            return files.getlist(name)
        return files.get(name)


class MultipleFileField(forms.FileField):
    """
    Django's FileField only cleans a single file by default.
    This subclass makes it accept and validate a list of files
    from a <input type="file" multiple> field.
    """
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput(attrs={"multiple": True}))
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class RoomImageForm(forms.Form):
    gallery_images = MultipleFileField(required=False)

    def clean_gallery_images(self):
        files = self.cleaned_data.get("gallery_images")
        if files:
            for f in files:
                if not f.content_type.startswith("image/"):
                    raise forms.ValidationError(f"'{f.name}' is not a valid image file.")
                if f.size > 5 * 1024 * 1024:  # 5MB limit
                    raise forms.ValidationError(f"'{f.name}' exceeds the 5MB size limit.")
        return files



from django.forms import inlineformset_factory
from .models import Activity, ActivityImage


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = [
            "name",
            "description",
            "image",
            "status",
            "duration",
            "price",
            "location",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "duration": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


# Inline formset so you can add/edit multiple gallery images
# on the same page as the Activity form.
ActivityImageFormSet = inlineformset_factory(
    Activity,
    ActivityImage,
    fields=["image", "caption", "order"],
    extra=3,          # empty extra rows for adding new images
    can_delete=True,  # allows deleting existing gallery images
    widgets={
        "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        "caption": forms.TextInput(attrs={"class": "form-control"}),
        "order": forms.NumberInput(attrs={"class": "form-control", "style": "width:80px"}),
    },
)

from .models import NearbyDestination, NearbyDestinationImage


class NearbyDestinationForm(forms.ModelForm):
    class Meta:
        model = NearbyDestination
        fields = [
            "name",
            "description",
            "image",
            "status",
            "distance",
            "location",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "distance": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


# Inline formset so you can add/edit multiple gallery images
# on the same page as the NearbyDestination form.
NearbyDestinationImageFormSet = inlineformset_factory(
    NearbyDestination,
    NearbyDestinationImage,
    fields=["image", "caption", "order"],
    extra=3,          # empty extra rows for adding new images
    can_delete=True,  # allows deleting existing gallery images
    widgets={
        "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        "caption": forms.TextInput(attrs={"class": "form-control"}),
        "order": forms.NumberInput(attrs={"class": "form-control", "style": "width:80px"}),
    },
)
import re

from django import forms
from .models import Package


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = [
            "name",
            "description",
            "image",
            "status",
            "duration",
            "price",
            "rooms",
            "activities",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "duration": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. 3 Days / 2 Nights"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "rooms": forms.SelectMultiple(attrs={"class": "form-select", "size": 6}),
            "activities": forms.SelectMultiple(attrs={"class": "form-select", "size": 6}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Strip "#<id>" from Room/Activity dropdown labels, e.g.
        # "Clonical Cottage #2 (Active)" -> "Clonical Cottage (Active)"
        self.fields["rooms"].label_from_instance = self._strip_id_label
        self.fields["activities"].label_from_instance = self._strip_id_label

    @staticmethod
    def _strip_id_label(obj):
        return re.sub(r"\s*#\d+\s*", " ", str(obj)).strip()
    

from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "guest_name", "guest_email", "guest_phone",
            "package", "check_in", "check_out",
            "num_guests", "special_requests",
        ]
        widgets = {
            "guest_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter full name"}),
            "guest_email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "you@example.com"}),
            "guest_phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "+91 9876543210"}),
            "package": forms.Select(attrs={"class": "form-select"}),
            "check_in": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "check_out": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "num_guests": forms.NumberInput(attrs={"class": "form-control", "min": 1, "placeholder": "Number of guests"}),
            "special_requests": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Any special requests (optional)"}),
        }
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Public-facing form matching the fields in the enquiry widget:
    First Name, Last Name, Phone Number, Email Address, Send Message."""

    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "phone_number", "email", "message"]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "Phone Number", "class": "form-control"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email Address", "class": "form-control"}),
            "message": forms.Textarea(attrs={"placeholder": "Send Message", "class": "form-control", "rows": 5}),
        }


class ReplyForm(forms.Form):
    """Admin/staff-facing form used to reply to an enquiry.
    Submitting this sends an email directly to the enquirer's email address."""

    reply_message = forms.CharField(
        label="Reply",
        widget=forms.Textarea(attrs={"rows": 6, "class": "form-control", "placeholder": "Type your reply..."}),
    )