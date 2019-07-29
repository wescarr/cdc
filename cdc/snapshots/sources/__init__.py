from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import AnyStr, IO, Sequence

from cdc.utils.registry import Registry
from cdc.snapshots.destinations import SnapshotDestination
from cdc.snapshots.snapshot_types import SnapshotDescriptor

class SnapshotSource(ABC):
    """
    Takes a snapshot from the source database and store the content into
    the output object. 
    """

    @abstractmethod
    def dump(self,
        output: SnapshotDestination,
        tables: Sequence[str],
    ) -> SnapshotDescriptor:
        raise NotImplementedError


from cdc.snapshots.sources.postgres_snapshot import postgres_snapshot_factory

registry: Registry[SnapshotSource] = Registry(
    {"postgres_logical": postgres_snapshot_factory}
)
