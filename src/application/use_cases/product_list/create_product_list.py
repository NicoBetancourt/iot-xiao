from src.domain.repositories.product_list_repo import ProductListRepository


class CreateProductList:
    def __init__(self, product_list_repo: ProductListRepository):
        self.product_list_repo = product_list_repo

    def execute(self, product_data) -> str:
        res = self.product_list_repo.create(product_data.dict())
        return res
