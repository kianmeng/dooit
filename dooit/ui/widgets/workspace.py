from typing import Iterator, List
from textual.widget import Widget
from dooit.api.workspace import Workspace
from dooit.ui.widgets.inputs import Description
from dooit.ui.widgets.simple_input import SimpleInput
from dooit.ui.widgets.utils import Padding
from .node import Node


class WorkspaceWidget(Node):
    """
    Subclass of `Node` class to visualize workspace
    """

    DEFAULT_CSS = """
    WorkspaceWidget {
        layout: grid;
        grid-size: 3;
        grid-columns: auto auto 1fr;
    }
    """

    ModelType = Workspace

    def setup_children(self) -> None:
        self.description = Description(self.model)

    def get_child_inputs(self) -> List[SimpleInput]:
        return [self.description]

    def _get_model_children(self) -> List[Workspace]:
        return self.model.workspaces

    def draw(self) -> Iterator[Widget]:
        yield self.pointer
        yield Padding(self.model.nest_level)
        yield self.description
