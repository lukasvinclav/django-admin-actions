# django-admin-actions

## Getting started

1. Installation

```bash
pip install git+https://git@github.com/lukasvinclav/django-admin-actions.git
```

2. Add **admin_admin_actions** into **INSTALLED_APPS** in your settings file before **django.contrib.admin**.

## Sample admin configuration

```python
from django.contrib import admin, messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import ExampleModel
from admin_actions.admin import ActionsAdmin


@admin.register(ExampleModel)
class CustomAdmin(ActionsAdmin):
    actions_list = ('custom_list_action', )
    actions_row = ('custom_row_action', )
    actions_detail = ('custom_detail_action', )

    def custom_list_action(self, request):
        # custom logic here
        return redirect(reverse_lazy('admin:APP_MODEL_changelist'))
    custom_list_action.short_description = _('Custom name')
    custom_list_action.url_path = 'clean-url-path-1'

    def custom_row_action(self, request, pk):
        # custom logic here
        return redirect(reverse_lazy('admin:APP_MODEL_changelist'))
    custom_row_action.short_description = _('Row custom name')
    custom_row_action.url_path = 'clean-url-path-2'

    def custom_detail_action(self, request, pk):
        # custom logic here
        return redirect(reverse_lazy('admin:APP_MODEL_changelist'))
    custom_detail_action.short_description = _('Detail custom name')
    custom_detail_action.url_path = 'clean-url-path-3'
```