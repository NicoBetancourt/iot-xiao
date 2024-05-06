# Use cases package
from src.application.use_cases.product_list.create_product_list import CreateProductList
from src.application.use_cases.product_list.get_one_product_list import GetOneProductList
from src.application.use_cases.product_list.get_all_product_list import GetAllProductList
from src.application.use_cases.product_list.update_product_list import UpdateProductList
from src.application.use_cases.product_list.delete_one_product_list import DeleteProductList

# Repos
from src.domain.repositories.product_list_repo import ProductListRepository
from src.infrastructure.db.implementation.product_list_repository import ProductListMongoRepository

_product_repo = ProductListRepository(ProductListMongoRepository())

# Use cases
create_product = CreateProductList(_product_repo).execute
get_product_by_id = GetOneProductList(_product_repo).execute
get_all_products = GetAllProductList(_product_repo).execute
delete_product = DeleteProductList(_product_repo).execute
update_product = UpdateProductList(_product_repo).execute
