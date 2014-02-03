import autocomplete_light
from locations import models

# This will generate a PersonAutocomplete class
autocomplete_light.register(models.Suburb,
    # Just like in ModelAdmin.search_fields
    search_fields=['^suburb'],
    # This will actually html attribute data-placeholder which will set
    # javascript attribute widget.autocomplete.placeholder.
    autocomplete_js_attributes={'placeholder': 'Other model name ?',},
)