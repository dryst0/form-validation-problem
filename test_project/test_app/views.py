from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext

from test_app import models as test_models, forms as test_forms

def index(request, template_name='test_app/index.html'):
    context = RequestContext(request)

    form = test_forms.TestForm(data={
        'email': '',
        'password': '',
        'colour': '',
        'animal': '',
        'type_of_tiger': ''
    })

    if request.method == 'POST':
        form = test_forms.TestForm(data=request.POST)
        
        if form.is_valid():
            messages.success(request, "Form is valid")

    http_response = render_to_response(
        template_name,
        {
            'form': form
        },
        context_instance=context
    )

    return http_response
