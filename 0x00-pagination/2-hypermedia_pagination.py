#!/usr/bin/env python3
"""
0x00. Pagination
"""


import csv
import math
from typing import List


def index_range(page, page_size):
    """return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination
    parameters."""
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return (startIndex, endIndex)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """A method that paginate the dataset and return the appropriate
        page of the dataset (i.e. the correct list of rows)."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        startIndex, endIndex = index_range(page, page_size)
        data = self.dataset()
        if startIndex >= len(data):
            return []
        return data[startIndex:endIndex]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """A method that return a dictionary of pagination parameters for
        a page."""
        data = self.dataset()
        total_pages = math.ceil(len(data) / page_size)
        getPage = self.get_page(page, page_size)

        return {
            'page_size': len(getPage),
            "page": page,
            "data": getPage,
            "next_page": page + 1 if page + 1 <= total_pages else None,
            "prev_page": page - 1 if page - 1 >= 1 else None,
            "total_pages": total_pages,
        }
