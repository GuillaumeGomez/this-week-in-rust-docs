---
layout: post
title: This Week in Rust Docs 79
date: 2017-10-29
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

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) included [external files in documentation in rustdoc (RFC 1990)](https://github.com/rust-lang/rust/pull/44781) and showed [in docs whether the return type of a function impls Iterator/Read/Write](https://github.com/rust-lang/rust/pull/45039).
* [@joshleeb](https://github.com/joshleeb) fixed [duplicated display of error E0502](https://github.com/rust-lang/rust/pull/45603).
* [@Aaronepower](https://github.com/Aaronepower) updated [Release notes for 1.22.0](https://github.com/rust-lang/rust/pull/45454).
* [@leodasvacas](https://github.com/leodasvacas) documented [that call expressions also represent ADT constructors](https://github.com/rust-lang/rust/pull/45579).
* [@estebank](https://github.com/estebank) detected [`=` -> `:` typo in let bindings](https://github.com/rust-lang/rust/pull/45452).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) improved [sidebar rendering and added methods list](https://github.com/rust-lang/rust/pull/45187), added [missing links and examples](https://github.com/rust-lang/rust/pull/45582), add [missing docs for MetadataExt](https://github.com/rust-lang/rust/pull/45470) and fixed [title heading overlap in rust doc](https://github.com/rust-lang/rust/pull/45450).

# Recent doc contributions

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) updated [pulldown and fixed spurious rendering difference around footnotes](https://github.com/rust-lang/rust/pull/45421).
* [@frewsxcv](https://github.com/frewsxcv) improved [docs around `Once::call_once_force` and `OnceState`](https://github.com/rust-lang/rust/pull/45429), removed ['future Rust version' code block in diagnostic text](https://github.com/rust-lang/rust/pull/45585) and improved [docs for UdpSocket::set_nonblocking](https://github.com/rust-lang/rust/pull/45449).
* [@carols10cents](https://github.com/carols10cents) corrected [misspelling in error text: re-assignment => reassignment](https://github.com/rust-lang/rust/pull/45398), updated [the book for a fix to the print button](https://github.com/rust-lang/rust/pull/45554) and updated [the book on beta to fix the print button](https://github.com/rust-lang/rust/pull/45555).
* [@Technius](https://github.com/Technius) improved [std::process module docs](https://github.com/rust-lang/rust/pull/45295).
* [@nzig](https://github.com/nzig) fixed [rustc_on_unimplemented example in Unstable Book](https://github.com/rust-lang/rust/pull/45574).
* [@steveklabnik](https://github.com/steveklabnik) removed ['just' in diagnostics](https://github.com/rust-lang/rust/pull/45549) and fixed [formatting in unstable book's attr-literals section](https://github.com/rust-lang/rust/pull/45531).
* [@thombles](https://github.com/thombles) improved [diagnostics when list of tokens has incorrect separators](https://github.com/rust-lang/rust/pull/45503).
* [@michaelwoerister](https://github.com/michaelwoerister) removed [duplicated compiler diagnostic emissions](https://github.com/rust-lang/rust/pull/45519).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [short error message-format](https://github.com/rust-lang/rust/pull/44636), limited [the sidebar height](https://github.com/rust-lang/rust/pull/45212), added [missing code examples](https://github.com/rust-lang/rust/pull/45361) and showed [src button and function version on mobile version](https://github.com/rust-lang/rust/pull/45502).

# Meetings

Next meeting will be on Tuesday 31st of October 2017 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
