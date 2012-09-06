#models
from django.db import models

#imagekit
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import resize, crop

#utils
from django.template.defaultfilters import slugify

#trans
from django.utils.translation import ugettext as _, ugettext_lazy as Z