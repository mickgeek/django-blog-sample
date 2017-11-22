# -*- coding: utf-8 -*-

from django import template

register = template.Library()


@register.filter
def create_pagination_range(page, max_num_buttons):
    max_num_buttons = int(max_num_buttons)
    begin_page = max(1, page.number - int(max_num_buttons / 2))
    end_page = begin_page + max_num_buttons
    if end_page > page.paginator.num_pages:
        end_page = page.paginator.num_pages + 1
        begin_page = max(1, end_page - max_num_buttons)
    return range(begin_page, end_page)
