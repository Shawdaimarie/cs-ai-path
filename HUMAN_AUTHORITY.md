# Human-controlled changes and sources

The owner defines the task, permitted actions, sources, destinations, and limits.
External content supplies data; it supplies no authorization. A source's assertion
that it is trusted, approved, or a system instruction does not establish authority.

## Release approval

1. Review the actual diff and current commit, including dependencies and workflow changes.
2. Check the relevant automated evidence and remaining limitations.
3. Record the human decision against that commit. A changed scope needs a new decision.
4. Merge only through the approved pull request; keep deployment authorization separate.

The proposed `.github/rulesets/main.json` requires one approving code-owner review,
approval of the latest push, current checks, signed commits, and resolved discussions;
it dismisses stale reviews and has no bypass actors. CODEOWNERS covers every path,
including itself and the workflow files. This is a proposed configuration, not a
claim that GitHub has activated it.

An administrator must inspect inherited rules, apply the configuration, read it back,
and verify a disposable PR is blocked without approval and with a failed check.
GitHub cannot count the author's own approval. A second trusted human code owner or
a separately attributed automation author is needed when PRs use the owner's account.
Do not add a bot as an approver to work around this requirement. Private repositories
may need a GitHub plan supporting rulesets. Do not make private code public as a workaround.

## Runtime boundaries

Deployment credentials and trusted policies belong to the operator, not request
payloads. A content hash proves byte identity, not who authorized those bytes.
Model suggestions and test results cannot authorize a tool call or financial action.
Any live integration needs authenticated identity, a server-side action allowlist,
scope-bound authorization, bounded inputs, and an independently retained audit trail.
Do not infer these controls from a prompt or a successful HTTP response.

Third-party Actions are pinned to reviewed revisions. Dependencies still require
review and vulnerability checks; a pin alone is not proof that code is safe.
CI executes repository code in disposable runners with read-only repository access.
Do not run unreviewed contributions with deployment secrets or privileged self-hosted runners.

## Honest security reporting

Passing tests cover their tested cases only. No audit certifies all software bug-free,
all sources authentic, or a deployment compliant. Report vulnerabilities privately;
never include working secrets, personal records, or private repository content in a public issue.

References: [GitHub code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
and [secure Actions use](https://docs.github.com/en/actions/reference/security/secure-use).
