---
layout: post
title: This Week in Rust Docs 45
date: 2017-2-26
---

Hello and welcome to *This Week in Rust Docs*!

*This Week in Rust Docs* is openly developed [on GitHub](https://github.com/GuillaumeGomez/this-week-in-rust-docs).
If you find any errors in this week's issue, [please submit a PR](https://github.com/GuillaumeGomez/this-week-in-rust-docs/pulls).

And of course, don't forget to look at the docs:

* [Stable](https://doc.rust-lang.org/)
* [Beta](http://doc.rust-lang.org/beta/)
* [Nightly](http://doc.rust-lang.org/nightly/)

This week's edition was edited by [Guillaume Gomez](https://github.com/GuillaumeGomez).

# Latest news

Nothing.

# Current opened issues

For now, here are the two big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on GitHub!

# Waiting for merge

* [@brson](https://github.com/brson) added [release notes for 1.16](https://github.com/rust-lang/rust/pull/39835).
* [@pmer](https://github.com/pmer) used ["macOS" terminology consistently](https://github.com/rust-lang/rust/pull/40102).
* [@SimonSapin](https://github.com/SimonSapin) published [docs for the proc_macro crate](https://github.com/rust-lang/rust/pull/39986).
* [@keeperofdakeys](https://github.com/keeperofdakeys) replaced [./configure with config.toml in README.md and CONTRIBUTING.md](https://github.com/rust-lang/rust/pull/40056) and added [notes about capacity effects to Vec::truncate()](https://github.com/rust-lang/rust/pull/39738).
* [@oli-obk](https://github.com/oli-obk) distinguished [guesses from suggestions](https://github.com/rust-lang/rust/pull/39458).
* [@zackmdavis](https://github.com/zackmdavis) used [help rather than span note for no method error; a slight rephrasing](https://github.com/rust-lang/rust/pull/39441).
* [@estebank](https://github.com/estebank) highlighted [code in `rustc --explain`](https://github.com/rust-lang/rust/pull/39300).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [nightly-only experimental API display](https://github.com/rust-lang/rust/pull/40057), added [missing url in sync structs](https://github.com/rust-lang/rust/pull/40081), added [missing urls and small nits](https://github.com/rust-lang/rust/pull/39513), improved [invalid call on non-function error message](https://github.com/rust-lang/rust/pull/39814), fixed [invalid module suggestion](https://github.com/rust-lang/rust/pull/38255), added [missing urls and examples for Condvar docs](https://github.com/rust-lang/rust/pull/40033), added [ref suggestion](https://github.com/rust-lang/rust/pull/37658) and improved [associated constant rendering in rustdoc](https://github.com/rust-lang/rust/pull/39944).

# Recent doc contributions

* [@mp4096](https://github.com/mp4096) wrote [better explanation for return values for min, max functions for the Iterator trait](https://github.com/rust-lang/rust/pull/39955).
* [@keeperofdakeys](https://github.com/keeperofdakeys) provided [suggestions for unknown macros imported with `use`](https://github.com/rust-lang/rust/pull/39953).
* [@steveklabnik](https://github.com/steveklabnik) ported [the reference to mdbook](https://github.com/rust-lang/rust/pull/39855), created [the Unstable Book](https://github.com/rust-lang/rust/pull/39866), reenabled [the linkchecker for books](https://github.com/rust-lang/rust/pull/39976) and updated [mdbook version](https://github.com/rust-lang/rust/pull/39966).
* [@arthurprs](https://github.com/arthurprs) fixed [spelling in hashmap comments](https://github.com/rust-lang/rust/pull/39937).
* [@JDemler](https://github.com/JDemler) added [Documentation for Custom Attributes and Error Reporting in Procedural Macros](https://github.com/rust-lang/rust/pull/39845).
* [@jrmuizel](https://github.com/jrmuizel) removed [obsolete documentation about drop-flags](https://github.com/rust-lang/rust/pull/39304).
* [@mina86](https://github.com/mina86) updated The Book: [binary prefixed are defined by IEC and not in SI](https://github.com/rust-lang/rust/pull/39777).
* [@tclfs](https://github.com/tclfs) fixed [a typo](https://github.com/rust-lang/rust/pull/40078).
* [@cynicaldevil](https://github.com/cynicaldevil) added [test for inclusive_range_syntax in compile-fail test suite](https://github.com/rust-lang/rust/pull/40031).
* [@Rufflewind](https://github.com/Rufflewind) added [Gankro's table to nomicon/src/phantom-data.md](https://github.com/rust-lang/rust/pull/40069) and resolved [ambiguities of Generics in The Book](https://github.com/rust-lang/rust/pull/39748).
* [@danobi](https://github.com/danobi) moved [COMPILER_TESTS.md out of the root directory](https://github.com/rust-lang/rust/pull/40086).
* [@estebank](https://github.com/estebank) displayed [properly note/expected details](https://github.com/rust-lang/rust/pull/39905).
* [@sgrif](https://github.com/sgrif) fixed [indentation of error message](https://github.com/rust-lang/rust/pull/39940).
* [@tomwhoiscontrary](https://github.com/tomwhoiscontrary) corrected [another typo in procedural macros chapter of the Book](https://github.com/rust-lang/rust/pull/40071).
* [@mbrubeck](https://github.com/mbrubeck) added [additional docs for Vec, String, and slice trait impls](https://github.com/rust-lang/rust/pull/39886).
* [@ArtBears](https://github.com/ArtBears) fixed [a typo in CONTRIBUTING.md](https://github.com/rust-lang/rust/pull/39965).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) set [rustdoc --test files' path relative to the current directory](https://github.com/rust-lang/rust/pull/39859), improved [file not found for module error](https://github.com/rust-lang/rust/pull/39765), added [missing urls and examples into Barrier structs](https://github.com/rust-lang/rust/pull/40010) and added [missing urls in MutexGuard docs](https://github.com/rust-lang/rust/pull/40052).

# Meetings

Next meeting will be on Wednesday 1st of March 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
