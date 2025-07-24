class PageNumberPagination:
    def __init__(self, page_size):
        self.page_size = page_size
    

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1