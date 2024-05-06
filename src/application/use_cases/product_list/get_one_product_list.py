from src.domain.entities.product_list import ProductList
from src.domain.repositories.product_list_repo import ProductListRepository


class GetOneProductList:
    def __init__(self, product_list_repo: ProductListRepository):
        self.product_list_repo = product_list_repo

    def execute(self, id: str) -> ProductList:
        res = self.product_list_repo.get_one(id)
        return res
