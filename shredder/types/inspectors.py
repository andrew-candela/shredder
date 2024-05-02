from shredder.types.database import Table, TableFKRelationship
from abc import ABC, abstractmethod


class Inspector(ABC):

    @abstractmethod
    def get_dependent_tables(table: Table) -> list[TableFKRelationship]:
