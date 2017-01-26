from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from diligen.forms import *
from diligen.utils import *

def index(request):
    ''' Index page
    - if given a GET parameter 'text' then displays analytics for that text
    - otherwise provides a blank textarea form and submit button to submit a GET
        request
    '''
    # define a blank dictionary for items to be passed to the template
    template_items = {}

    # see if there was a get request for ?text
    text_analytics = request.GET.get('text', None)

    # if there was, remove the textarea input and simply display the results
    # and the original paragraph
    if text_analytics:
        # fetch the counts for single words and consecutive pairs of words
        template_items['single_word_counts'], template_items['double_word_counts'] = parse_text(text_analytics)
        # pass the original text
        template_items['original_text'] = text_analytics

    # otherwise, have the textarea input present
    else:
        TAForm = TextAnalyticForm()
        template_items['TAForm'] = TAForm

    return render(request, 'index.html', template_items)
