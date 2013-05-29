import django.views.generic as generic
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy, ugettext as _