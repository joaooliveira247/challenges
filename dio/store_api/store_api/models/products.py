from store_api.models.base import CreateBaseModel
from store_api.schemas.products import ProductIn


class ProductModel(ProductIn, CreateBaseModel):
    ...
