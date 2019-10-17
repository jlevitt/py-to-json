# py-to-json
Script to convert a string representation of standard python data types to json. While debugging, it is sometimes useful to print a python dict. Simply printing a dict doesn't produce output that is formatted or easily queryable. Converting to json gives us data that can be piped into a tool like `jq` to format and query.

Example:
```
> echo "[1, 'foo', {'bar': 'baz'}]" | py-to-json | jq .
```
