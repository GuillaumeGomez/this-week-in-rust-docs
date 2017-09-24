---
layout: post
title: This Week in Rust Docs 74
date: 2017-9-24
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

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) made [rustdoc optimizations](https://github.com/rust-lang/rust/pull/44613) and included [external files in documentation in rustdoc (RFC 1990)](https://github.com/rust-lang/rust/pull/44781).
* [@gaurikholkar](https://github.com/gaurikholkar) added [E0623 for return types - both parameters are anonymous](https://github.com/rust-lang/rust/pull/44124).
* [@steveklabnik](https://github.com/steveklabnik) deprecated [several flags in rustdoc](https://github.com/rust-lang/rust/pull/44138).
* [@laumann](https://github.com/laumann) added [suggestions for misspelled method names](https://github.com/rust-lang/rust/pull/44297).
* [@zackmdavis](https://github.com/zackmdavis) added [comparison operators to must-use lint (under `fn_must_use` feature)](https://github.com/rust-lang/rust/pull/44103) and prevented [rustdoc to get confused by text "fn main" in a line comment](https://github.com/rust-lang/rust/pull/44713).
* [@frewsxcv](https://github.com/frewsxcv) indicated [how ChildStd{in,out,err} FDs are closed](https://github.com/rust-lang/rust/pull/44625).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.21.0](https://github.com/rust-lang/rust/pull/44481).
* [@thombles](https://github.com/thombles) improved [diagnostics when attempting to match tuple enum variant with struct pattern](https://github.com/rust-lang/rust/pull/44786).
* [@napen123](https://github.com/napen123) added [doc example to HashMap::hasher](https://github.com/rust-lang/rust/pull/44794).
* [@lucasem](https://github.com/lucasem) made [docs improvement in std::sync::{PoisonError, TryLockError}](https://github.com/rust-lang/rust/pull/44797).
* [@tirr-c](https://github.com/tirr-c) made [a friendlier error message for closure argument type mismatch](https://github.com/rust-lang/rust/pull/44735).
* [@estebank](https://github.com/estebank) pointed [at parameter type on E0301](https://github.com/rust-lang/rust/pull/44782
* [@budziq](https://github.com/budziq) corrected [the CONTRIBUTING.md "External Dependencies" section](https://github.com/rust-lang/rust/pull/44664).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [short error message-format](https://github.com/rust-lang/rust/pull/44636) and fixed [warning position in rustdoc code blocks](https://github.com/rust-lang/rust/pull/44789).

# Recent doc contributions

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) hid [internal types/traits from std docs via new #[doc(masked)] attribute](https://github.com/rust-lang/rust/pull/44026).
* [@gaurikholkar](https://github.com/gaurikholkar) extended [E0623 for earlybound and latebound for structs](https://github.com/rust-lang/rust/pull/44549).
* [@bluss](https://github.com/bluss) documented [thread builder panics for nul bytes in thread names](https://github.com/rust-lang/rust/pull/44651).
* [@oli-obk](https://github.com/oli-obk) removed [suggestion of placing `use` statements into expanded code](https://github.com/rust-lang/rust/pull/44215).
* [@Havvy](https://github.com/Havvy) expanded [size_of docs](https://github.com/rust-lang/rust/pull/44648).
* [@frewsxcv](https://github.com/frewsxcv) fixed [incorrect `into_inner` link in docs](https://github.com/rust-lang/rust/pull/44622).
* [@nikomatsakis](https://github.com/nikomatsakis) reworked [the README.md for rustc and add other readmes](https://github.com/rust-lang/rust/pull/44505).
* [@lucasem](https://github.com/lucasem) improved [std::sync::RwLock docs](https://github.com/rust-lang/rust/pull/44778).
* [@spastorino](https://github.com/spastorino) linked [to Rust forge from CONTRIBUTING.md](https://github.com/rust-lang/rust/pull/44776).
* [@durka](https://github.com/durka) improved [english in create_dir_all docs](https://github.com/rust-lang/rust/pull/44759).
* [@mattico](https://github.com/mattico) fixed [librustc/README.md diagram](https://github.com/rust-lang/rust/pull/44726).
* [@oconnor663](https://github.com/oconnor663) fixed [an incorrect assertion in the doc example for `std::io::copy`](https://github.com/rust-lang/rust/pull/44712).
* [@mssun](https://github.com/mssun) fixed [a typo in rustc help menu](https://github.com/rust-lang/rust/pull/44693).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [deref suggestion](https://github.com/rust-lang/rust/pull/43870), updated [codeblock color](https://github.com/rust-lang/rust/pull/44397), removed [small id false positive in rustdoc html diff](https://github.com/rust-lang/rust/pull/44350), added [pub visibility for methods as well](https://github.com/rust-lang/rust/pull/44554), added [missing links for Arc](https://github.com/rust-lang/rust/pull/44773), added [some missing links in io docs](https://github.com/rust-lang/rust/pull/44703), fixed [run button](https://github.com/rust-lang/rust/pull/44671) and added [more links and put the link character to the left](https://github.com/rust-lang/rust/pull/44661).

# Meetings

Next meeting will be on Wednesday 27th of September 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
