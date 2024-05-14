from src.domain.entities.product_list import ProductList
from src.domain.repositories.product_list_repo import ProductListRepository


class GetAllProductList:
    def __init__(self, product_list_repo: ProductListRepository):
        self.product_list_repo = product_list_repo

    def execute(self,filter,options) -> ProductList:
        res = self.product_list_repo.get_all(filter, options)
        return res
