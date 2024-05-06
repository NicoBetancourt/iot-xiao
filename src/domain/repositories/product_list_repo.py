from src.domain.entities.product_list import ProductList
from src.infrastructure.db.implementation.product_list_repository import ProductListMongoRepository


class ProductListRepository:
    def __init__(self, product_list_repo: ProductListMongoRepository):
        self.product_list_repo = product_list_repo

    def create(self, productList:ProductList) -> ProductList:
        res = self.product_list_repo.create(productList)
        return res
    
    def get_one(self, id:str) -> ProductList:
        res = self.product_list_repo.get_one(id)
        return res
    
    def get_all(self, filter, options) -> list[ProductList]:
        res = self.product_list_repo.get_all(filter, options)
        return res
    
    def update(self, id:str, productList:ProductList) -> ProductList:
        res = self.product_list_repo.update(id, productList)
        return res
    
    def delete(self, id:str) -> ProductList:
        res = self.product_list_repo.delete(id)
        return res