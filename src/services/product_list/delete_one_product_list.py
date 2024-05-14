from src.domain.repositories.product_list_repo import ProductListRepository


class DeleteProductList:
    def __init__(self, product_list_repo: ProductListRepository):
        self.product_list_repo = product_list_repo

    def execute(self, id:str) -> str:
        res = self.product_list_repo.delete(id)
        return res
