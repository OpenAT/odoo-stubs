from typing import Any, Optional

_logger: Any
PG_CONCURRENCY_ERRORS_TO_RETRY: Any
MAX_TRIES_ON_CONCURRENCY_FAILURE: int

def dispatch(method: Any, params: Any): ...
def check(f: Any): ...
def execute_cr(cr: Any, uid: Any, obj: Any, method: Any, *args: Any, **kw: Any): ...
def execute_kw(db: Any, uid: Any, obj: Any, method: Any, args: Any, kw: Optional[Any] = ...): ...
def execute(db: Any, uid: Any, obj: Any, method: Any, *args: Any, **kw: Any): ...
