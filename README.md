# Pandera test
Pandera Minimal Reproducible Example to test issues with pandera typing on dataframes.

## Reproduce
* `poetry install`
* `poetry run pyright pandera_test/main.py`

## Issues
```
  pandera_test/main.py:10:27 - error: Type of "Field" is partially unknown
    Type of "Field" is "(*, eq: Any | None = None, ne: Any | None = None, gt: Any | None = None, ge: Any | None = None, lt: Any | None = None, le: Any | None = None, in_range: Dict[str, Any] | None = None, isin: Iterable[Unknown] | None = None, notin: Iterable[Unknown] | None = None, str_contains: str | None = None, str_endswith: str | None = None, str_length: Dict[str, Any] | None = None, str_matches: str | None = None, str_startswith: str | None = None, nullable: bool = False, unique: bool = False, coerce: bool = False, regex: bool = False, ignore_na: bool = True, raise_warning: bool = False, n_failure_cases: int | None = None, alias: Any | None = None, check_name: bool | None = None, dtype_kwargs: Dict[str, Any] | None = None, title: str | None = None, description: str | None = None, default: Any | None = None, metadata: dict[Unknown, Unknown] | None = None, **kwargs: Unknown) -> Any" (reportUnknownMemberType)
```

```
  pandera_test/main.py:11:66 - error: Type of "Field" is partially unknown
    Type of "Field" is "(*, eq: Any | None = None, ne: Any | None = None, gt: Any | None = None, ge: Any | None = None, lt: Any | None = None, le: Any | None = None, in_range: Dict[str, Any] | None = None, isin: Iterable[Unknown] | None = None, notin: Iterable[Unknown] | None = None, str_contains: str | None = None, str_endswith: str | None = None, str_length: Dict[str, Any] | None = None, str_matches: str | None = None, str_startswith: str | None = None, nullable: bool = False, unique: bool = False, coerce: bool = False, regex: bool = False, ignore_na: bool = True, raise_warning: bool = False, n_failure_cases: int | None = None, alias: Any | None = None, check_name: bool | None = None, dtype_kwargs: Dict[str, Any] | None = None, title: str | None = None, description: str | None = None, default: Any | None = None, metadata: dict[Unknown, Unknown] | None = None, **kwargs: Unknown) -> Any" (reportUnknownMemberType)
```

```
  pandera_test/main.py:15:11 - error: Type of "field1" is partially unknown
    Type of "field1" is "Series[Unknown]" (reportUnknownMemberType)
```

```
  pandera_test/main.py:15:11 - error: Argument type is partially unknown
    Argument corresponds to parameter "values" in function "print"
    Argument type is "Series[Unknown]" (reportUnknownArgumentType)
```

```
  pandera_test/main.py:16:11 - error: Type of "field2" is partially unknown
    Type of "field2" is "Series[Unknown]" (reportUnknownMemberType)
```

```
  pandera_test/main.py:16:11 - error: Argument type is partially unknown
    Argument corresponds to parameter "values" in function "print"
    Argument type is "Series[Unknown]" (reportUnknownArgumentType)
```

