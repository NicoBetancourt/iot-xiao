from src.domain.entities.product_list import ProductList
from src.domain.repositories.product_list_repo import ProductListRepository


class UpdateProductList:
    def __init__(self, product_list_repo: ProductListRepository):
        self.product_list_repo = product_list_repo

    def execute(self, id, product_data) -> ProductList:
        res = self.product_list_repo.update(id, product_data.dict())
        return res
