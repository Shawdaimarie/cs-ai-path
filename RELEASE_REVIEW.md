# Release review

Before publishing, inspect the diff and run the repository's documented checks on the exact intended revision. Record the runtime versions, command, exit status, and limitations alongside the result. Recheck links without removing restricted-access destinations.

Keep local tests, synthetic data, and sample interfaces labeled. Live provider integration, public deployment, independent accessibility review, and research validation require their own evidence. Do not present local verification as production certification or university endorsement.

Review the existing license before distribution. Where no license is present, the owner must choose distribution terms; this review does not silently assign a license. Keep credentials outside source control. Publish only after owner review.

## Checks for this repository

Use the runtime and setup described in the README.

```sh
python tests/test_internal_links.py
```

Tests that require services or optional development packages need the documented setup. CI files are prepared locally; hosted CI has not run on these unpublished changes.
