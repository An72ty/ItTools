menu = [{'title': 'Downloads', 'url': 'ittool:downloads', 'page_number': 0},
        {'title': 'Plugins', 'url': 'ittool:plugins', 'page_number': 1},
        {'title': 'Eternal Arts', 'url': 'ittool:eternal-arts', 'page_number': 2},
        {'title': 'About', 'url': 'ittool:about', 'page_number': 3}
        ]


def list_to_queryset(model, data):
    from django.db.models.base import ModelBase

    if not isinstance(model, ModelBase):
        raise ValueError(
            "%s must be Model" % model
        )
    if not isinstance(data, list):
        raise ValueError(
            "%s must be List Object" % data
        )

    pk_list = [obj.pk for obj in data]
    return model.objects.filter(pk__in=pk_list)


def str_queryset_to_list(model, data) -> list:
    from django.db.models.base import ModelBase

    if not isinstance(model, ModelBase):
        raise ValueError(
            "%s must be Model" % model
        )
    if not isinstance(data, str):
        raise ValueError(
            "%s must be Str Object" % data
        )

    raw_list = data.split('[')
    raw_element = raw_list[1]
    raw_list_2 = raw_element.split(']')
    raw_element_2 = raw_list_2[0]
    raw_list_3 = raw_element_2.split(', ')

    model_list = []
    for model_str in raw_list_3:
        el = model_str.split(' ')
        try:
            e = el[1]
        except IndexError:
            return []
        el2 = e.split('>')
        model_name = el2[0]
        model_list.append(model.objects.get(name=model_name))

    return model_list