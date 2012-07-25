#models
from django.db import models

#imagekit
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import resize, crop
from imagekit.imagecache import NonValidatingImageCacheBackend

#utils
from django.template.defaultfilters import slugify