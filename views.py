#base views
import django.views.generic as generic

#http
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

#utils
from django.core.urlresolvers import reverse, reverse_lazy

#trans
from django.utils.translation import ugettext_lazy, ugettext as _