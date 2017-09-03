---
layout: post
title: This Week in Rust Docs 71
date: 2017-9-3
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

* [@qnighy](https://github.com/qnighy) added [hints when intercrate ambiguity causes overlap](https://github.com/rust-lang/rust/pull/43426).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [new "Implementations on Foreign Types" section to traits in rustdoc](https://github.com/rust-lang/rust/pull/43849), hid [internal types/traits from std docs via new #[doc(masked)] attribute](https://github.com/rust-lang/rust/pull/44026) and expanded [on using rustup custom toolchains in CONTRIBUTING.md](https://github.com/rust-lang/rust/pull/44194).
* [@gaurikholkar](https://github.com/gaurikholkar) extended [E0623 for LateBound and EarlyBound Regions](https://github.com/rust-lang/rust/pull/44079) and added [E0623 for return types - both parameters are anonymous](https://github.com/rust-lang/rust/pull/44124).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) added [tests rustdoc](https://github.com/rust-lang/rust/pull/44274).
* [@MarkMcCaskey](https://github.com/MarkMcCaskey) updated [unimplemented! docs](https://github.com/rust-lang/rust/pull/44206).
* [@steveklabnik](https://github.com/steveklabnik) deprecated [several flags in rustdoc](https://github.com/rust-lang/rust/pull/44138).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) stabilised [compile_fail](https://github.com/rust-lang/rust/pull/43949), added [deref suggestion](https://github.com/rust-lang/rust/pull/43870), fixed [rendering of const keyword for functions](https://github.com/rust-lang/rust/pull/44254) and added [display of cfg in rustdoc](https://github.com/rust-lang/rust/pull/44165).

# Recent doc contributions

* [@ishitatsuyuki](https://github.com/ishitatsuyuki) made [unused-extern-crate warn-by-default](https://github.com/rust-lang/rust/pull/42588).
* [@llogiq](https://github.com/llogiq) added [a lowercase suggestion to unknown_lints](https://github.com/rust-lang/rust/pull/44104).
* [@oli-obk](https://github.com/oli-obk) added [clippy as a submodule](https://github.com/rust-lang/rust/pull/43886), `](https://github.com/rust-lang/rust/pull/44059).
* [@mystor](https://github.com/mystor) removed [highlight of # which does not start an attribute in rustdoc](https://github.com/rust-lang/rust/pull/43918).
* [@nrc](https://github.com/nrc) improved [the Pulldown/hoedown warnings](https://github.com/rust-lang/rust/pull/44238).
* [@mattico](https://github.com/mattico) fixed [link in unstable book entry for Generators](https://github.com/rust-lang/rust/pull/44172).
* [@frewsxcv](https://github.com/frewsxcv) expandws [docs of multi-address behavior of some UDP/TCP APIs](https://github.com/rust-lang/rust/pull/44209), fixed [typo in doc `ToSocketAddrs` example](https://github.com/rust-lang/rust/pull/44205) and rewrote [`std::net::ToSocketAddrs` doc examples](https://github.com/rust-lang/rust/pull/44117).
* [@lukaramu](https://github.com/lukaramu) fixed [release notes on associated constants](https://github.com/rust-lang/rust/pull/44231).
* [@Phlosioneer](https://github.com/Phlosioneer) fixed [typo in 1.20.0 release notes](https://github.com/rust-lang/rust/pull/44230).
* [@daboross](https://github.com/daboross) clarified [that VecDeque::swap can panic](https://github.com/rust-lang/rust/pull/44114).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings when rustdoc html rendering differs](https://github.com/rust-lang/rust/pull/41991), updated [html-diff-rs version](https://github.com/rust-lang/rust/pull/44256), fixed [invalid display of enum sub-fields docs](https://github.com/rust-lang/rust/pull/44192) and fixed [invalid linker position](https://github.com/rust-lang/rust/pull/44135).

# Meetings

Next meeting will be on Wednesday 6th of September 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
