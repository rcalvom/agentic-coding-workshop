# Contributing

Contributions to the Campus Study Room Availability API are welcome.

## Development setup

Follow the instructions in [README.md](README.md) to create a virtual environment, install dependencies, and start the API.

Before submitting a change, run the test suite:

```bash
python -m pytest -q
```

For a focused change, you can run an individual test module:

```bash
python -m pytest -q tests/test_availability.py
```

## Reporting issues

Open a [GitHub issue](https://github.com/rcalvom/agentic-coding-workshop/issues) with:

- A concise description of the behavior.
- Steps to reproduce, including request parameters when applicable.
- Expected versus observed results.
- Environment information if relevant.

## Proposing changes

1. Review the relevant specification in `docs/api-spec.md`.
2. Keep changes focused and add or update tests for intended behavior.
3. Run the targeted and full test suites.
4. Review your diff before opening a pull request.
5. In the PR description, summarize the change, test results, and any known limitations.

Please do not commit virtual environments, credentials, or generated cache files.
