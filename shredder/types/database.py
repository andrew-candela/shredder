"""
Generic database objects.
Start with tables - may be more later.
"""
from dataclasses import dataclass
from typing import Callable


def _is_cycle(
        edge: "TableFKRelationship",
        visited_tables: set["str"],
        cyclic_edges: set["str"]) -> bool:
    
    if (edge_str := edge.hashprep()) in visited_tables:
        cyclic_edges.add(edge_str)
        return True
    visited_tables.add(edge_str)
    return False


@dataclass
class TableFKRelationship:
    parent_table: str
    parent_column: str
    child_table: str
    child_column: str

    def hashprep(self) -> str:
        return (
            f"{self.parent_table}:{self.parent_column}:"
            f"{self.child_table}:{self.child_column}"
        )
    
    def sql_to_null_fk_relationships(self, ids: list[str]) -> str:
        return (
            f"UPDATE TABLE {self.parent_table} SET {self.parent_column} = Null "
            f"WHERE "
        )
    
    @classmethod
    def deserialize(cls, str_rep: str) -> "TableFKRelationship":
        return cls(*str_rep.split(":")[:4])


class TableGraph:
    def __init__(self, root_table: "Table"):
        self.root_table = root_table


class Table:
    def __init__(self, name: str):
        self.name = name
        self.dependencies: list[Table] = []
    
    
    def find_dependencies(self, inspector: Callable[[str], list["Table"]]):
        """
        Traverses the graph of all children of this table.
        populates self.dependencies and self.dependency_cycles.
        """
        visited_tables: set[str] = set()
        cyclic_tables: set[str] = set()
        table_deps = inspector(self.name)
        for table_edge in table_deps:
            if not _is_cycle(table_edge, visited_tables, cyclic_tables):
                table_deps.extend(inspector(table_edge.child_table))
        self.dependencies = [TableFKRelationship.deserialize(t) for t in visited_tables]
        self.dependency_cycles = [TableFKRelationship.deserialize(t) for t in cyclic_tables]

    def handle_cycles(self) -> list[str]:
        """
        Produces a list of SQL statements that null out the 
        """
        for cycle in self.dependency_cycles:

    
