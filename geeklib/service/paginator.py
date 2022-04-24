from django.core.paginator import Paginator


def paginate_queryset(request, queryset, paginate_by=5):
    paginator = Paginator(queryset, paginate_by)
    return paginator.get_page(request.GET.get('page'))
