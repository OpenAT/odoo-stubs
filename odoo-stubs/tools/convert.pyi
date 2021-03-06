from typing import Any, Optional

_logger: Any
safe_eval: Any

class ParseError(Exception):
    msg: Any = ...
    text: Any = ...
    filename: Any = ...
    lineno: Any = ...
    def __init__(self, msg: Any, text: Any, filename: Any, lineno: Any) -> None: ...
    def __str__(self): ...

class RecordDictWrapper(dict):
    record: Any = ...
    def __init__(self, record: Any) -> None: ...
    def __getitem__(self, key: Any): ...

def _get_idref(self, env: Any, model_str: Any, idref: Any): ...
def _fix_multiple_roots(node: Any) -> None: ...
def _eval_xml(self, node: Any, env: Any): ...
def str2bool(value: Any): ...

class xml_import:
    @staticmethod
    def nodeattr2bool(node: Any, attr: Any, default: bool = ...): ...
    def isnoupdate(self, data_node: Optional[Any] = ...): ...
    def get_context(self, data_node: Any, node: Any, eval_dict: Any): ...
    def get_uid(self, data_node: Any, node: Any): ...
    def make_xml_id(self, xml_id: Any): ...
    def _test_xml_id(self, xml_id: Any) -> None: ...
    def _tag_delete(self, rec: Any, data_node: Optional[Any] = ..., mode: Optional[Any] = ...) -> None: ...
    def _tag_report(self, rec: Any, data_node: Optional[Any] = ..., mode: Optional[Any] = ...): ...
    def _tag_function(self, rec: Any, data_node: Optional[Any] = ..., mode: Optional[Any] = ...) -> None: ...
    def _tag_act_window(self, rec: Any, data_node: Optional[Any] = ..., mode: Optional[Any] = ...) -> None: ...
    def _tag_menuitem(self, rec: Any, data_node: Optional[Any] = ..., mode: Optional[Any] = ...) -> None: ...
    def _assert_equals(self, f1: Any, f2: Any, prec: int = ...): ...
    def _tag_assert(self, rec: Any, data_node: Optional[Any] = ..., mode: Optional[Any] = ...) -> None: ...
    def _tag_record(self, rec: Any, data_node: Optional[Any] = ..., mode: Optional[Any] = ...): ...
    def _tag_template(self, el: Any, data_node: Optional[Any] = ..., mode: Optional[Any] = ...): ...
    def id_get(self, id_str: Any, raise_if_not_found: bool = ...): ...
    def model_id_get(self, id_str: Any, raise_if_not_found: bool = ...): ...
    def parse(self, de: Any, mode: Optional[Any] = ...): ...
    mode: Any = ...
    module: Any = ...
    env: Any = ...
    cr: Any = ...
    uid: Any = ...
    idref: Any = ...
    assertion_report: Any = ...
    noupdate: Any = ...
    xml_filename: Any = ...
    _tags: Any = ...
    def __init__(self, cr: Any, module: Any, idref: Any, mode: Any, report: Optional[Any] = ..., noupdate: bool = ..., xml_filename: Optional[Any] = ...) -> None: ...

def convert_file(cr: Any, module: Any, filename: Any, idref: Any, mode: str = ..., noupdate: bool = ..., kind: Optional[Any] = ..., report: Optional[Any] = ..., pathname: Optional[Any] = ...) -> None: ...
def convert_sql_import(cr: Any, fp: Any) -> None: ...
def convert_csv_import(cr: Any, module: Any, fname: Any, csvcontent: Any, idref: Optional[Any] = ..., mode: str = ..., noupdate: bool = ...) -> None: ...
def convert_xml_import(cr: Any, module: Any, xmlfile: Any, idref: Optional[Any] = ..., mode: str = ..., noupdate: bool = ..., report: Optional[Any] = ...): ...
