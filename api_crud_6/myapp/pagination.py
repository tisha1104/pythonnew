# from rest_framework.pagination import PageNumberPagination

# class IncreasingPagination(PageNumberPagination):

#     def get_page_size(self, request):
#         page = int(request.query_params.get('page', 1))
#         return page

#     def paginate_queryset(self, queryset, request, view=None):
#         page_size = self.get_page_size(request)

#         # if page size exceeds queryset length → prevent crash
#         if page_size > queryset.count():
#             return queryset[:]

#         return super().paginate_queryset(queryset, request, view)