---
layout: post
title: This Week in Rust Docs 75
date: 2017-10-1
---

Hello and welcome to *This Week in Rust Docs*!

*This Week in Rust Docs* is openly developed [on GitHub](https://github.com/GuillaumeGomez/this-week-in-rust-docs).
If you find any errors in this week's issue, [please submit a PR](https://github.com/GuillaumeGomez/this-week-in-rust-docs/pulls).

And of course, don't forget to look at the docs:

* [Stable](https://doc.rust-lang.org/)
* [Beta](https://doc.rust-lang.org/beta/)
* [Nightly](https://doc.rust-lang.org/nightly/)

This week's edition was edited by [Guillaume Gomez](https://github.com/GuillaumeGomez).

# Latest news

The switch to [Pulldown](https://github.com/google/pulldown-cmark) for the rust doc rendering has finally [started](https://github.com/rust-lang/rust/pull/41991)!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) made [rustdoc optimizations](https://github.com/rust-lang/rust/pull/44613) abd included [external files in documentation in rustdoc (RFC 1990)](https://github.com/rust-lang/rust/pull/44781).
* [@steveklabnik](https://github.com/steveklabnik) deprecated [several flags in rustdoc](https://github.com/rust-lang/rust/pull/44138).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.21.0](https://github.com/rust-lang/rust/pull/44481).
* [@budziq](https://github.com/budziq) corrected [the CONTRIBUTING.md "External Dependencies" section](https://github.com/rust-lang/rust/pull/44664).
* [@vi](https://github.com/vi) rendered [`[src]` links for trait implementors in rustdoc](https://github.com/rust-lang/rust/pull/44920).
* [@Havvy](https://github.com/Havvy) improved [docs for size_of::<#[repr(C)]> items](https://github.com/rust-lang/rust/pull/44897).
* [@leavehouse](https://github.com/leavehouse) fixed [TcpStream::local_addr docs example code](https://github.com/rust-lang/rust/pull/44913).
* [@Pirh](https://github.com/Pirh) updated [docs for process::abort](https://github.com/rust-lang/rust/pull/44905).
* [@kennytm](https://github.com/kennytm) improved [doc-test: in Markdown tests, Use all of `<h1>` to `<h6>` as the test name](https://github.com/rust-lang/rust/pull/44867).
* [@federicomenaquintero](https://github.com/federicomenaquintero) improved [docs for CStr, CString, OsStr, OsString](https://github.com/rust-lang/rust/pull/44855).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [short error message-format](https://github.com/rust-lang/rust/pull/44636) and added [missing fnty args rustdoc](https://github.com/rust-lang/rust/pull/44892).

# Recent doc contributions

* [@laumann](https://github.com/laumann) added [suggestions for misspelled method names](https://github.com/rust-lang/rust/pull/44297).
* [@zackmdavis](https://github.com/zackmdavis) added [comparison operators to must-use lint (under `fn_must_use` feature)](https://github.com/rust-lang/rust/pull/44103) and prevented [rustdoc to get confused by text "fn main" in a line comment](https://github.com/rust-lang/rust/pull/44713).
* [@frewsxcv](https://github.com/frewsxcv) indicated [how ChildStd{in,out,err} FDs are closed](https://github.com/rust-lang/rust/pull/44625).
* [@thombles](https://github.com/thombles) improved [diagnostics when attempting to match tuple enum variant with struct pattern](https://github.com/rust-lang/rust/pull/44786).
* [@tirr-c](https://github.com/tirr-c) made [a friendlier error message for closure argument type mismatch](https://github.com/rust-lang/rust/pull/44735).
* [@estebank](https://github.com/estebank) pointed [at parameter type on E0301](https://github.com/rust-lang/rust/pull/44782].), pointed [at signature on unused lint](https://github.com/rust-lang/rust/pull/44847) anded point [at parameter type on E0301](https://github.com/rust-lang/rust/pull/44782).
* [@dbrgn](https://github.com/dbrgn) added [trace_macros! to unstable book](https://github.com/rust-lang/rust/pull/44944).
* [@pnkfelix](https://github.com/pnkfelix) some [fixes to mir-borrowck](https://github.com/rust-lang/rust/pull/44736).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [warning position in rustdoc code blocks](https://github.com/rust-lang/rust/pull/44789).

# Meetings

Next meeting will be on Wednesday 4th of October 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
