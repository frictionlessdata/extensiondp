# ruff: noqa -- DO NOT UPDATE this @generated file

from __future__ import annotations

from typing import Any, Literal, Mapping, Sequence, TypedDict, Union

from typing_extensions import NotRequired


class Table1Resource(TypedDict):
    name: Literal['table1']
    data: NotRequired[Sequence[Mapping[str, Any]]]
    """
    Data items have to conform to the Table1 schema
    """
    schema: Literal[
        'https://raw.githubusercontent.com/datisthq/extensiondp/v0.1.0/extension/schemas/table1.json'
    ]


class Table2Resource(TypedDict):
    name: Literal['table2']
    data: NotRequired[Sequence[Mapping[str, Any]]]
    """
    Data items have to conform to the Table2 schema
    """
    schema: Literal[
        'https://raw.githubusercontent.com/datisthq/extensiondp/v0.1.0/extension/schemas/table2.json'
    ]


Resource = Union[Table1Resource, Table2Resource]


Package = TypedDict(
    'Package',
    {
        '$schema': Literal[
            'https://raw.githubusercontent.com/datisthq/extensiondp/v0.1.0/extension/profile.json'
        ],
        'resources': Sequence[Resource],
    },
)


class ExtensionDataPackageProfile(Package):
    pass
