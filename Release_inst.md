# Release Instruction

## Update copyright

If necessary, update `copyright` in `docs/conf.py`.

## Update Authors

If necessary, update `authors` in `pyproject.toml`.

## Bump up version

```
$ poetry run bump2version <part>
```

The `part` of the version to increase: `major`, `minor`, `patch`

Example bumping up minor par of version:

```
$ poetry run bump2version minor
```
