from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic

TDom = TypeVar('TDom')
FDom = TypeVar('FDom')

class BaseImplementation(ABC, Generic[TDom, FDom]):

    @abstractmethod
    def create(self, item: TDom) -> TDom:
        pass

    @abstractmethod
    def update(self, id: str, item: TDom) -> Optional[TDom]:
        pass

    @abstractmethod
    def delete(self, id: str) -> bool:
        pass

    @abstractmethod
    def get_all(self, filter: FDom, options: dict) -> List[TDom]:
        pass

    @abstractmethod
    def get_one(self, id: str) -> Optional[TDom]:
        pass

    @abstractmethod
    def count_registers(self, filter: FDom) -> int:
        pass

    @abstractmethod
    def upsert_docs(self, query: dict, items: TDom) -> TDom:
        pass

    @abstractmethod
    def create_many(self, items: List[TDom]) -> List[TDom]:
        pass
