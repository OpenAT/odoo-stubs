from typing import Any, Optional

_logger: Any
_test_logger: Any

def load_data(cr: Any, idref: Any, mode: Any, kind: Any, package: Any, report: Any): ...
def load_demo(cr: Any, package: Any, idref: Any, mode: Any, report: Optional[Any] = ...): ...
def force_demo(cr: Any) -> None: ...
def load_module_graph(cr: Any, graph: Any, status: Optional[Any] = ..., perform_checks: bool = ..., skip_modules: Optional[Any] = ..., report: Optional[Any] = ..., models_to_check: Optional[Any] = ...): ...
def _check_module_names(cr: Any, module_names: Any) -> None: ...
def load_marked_modules(cr: Any, graph: Any, states: Any, force: Any, progressdict: Any, report: Any, loaded_modules: Any, perform_checks: Any, models_to_check: Optional[Any] = ...): ...
def load_modules(db: Any, force_demo: bool = ..., status: Optional[Any] = ..., update_module: bool = ...): ...
def reset_modules_state(db_name: Any) -> None: ...
