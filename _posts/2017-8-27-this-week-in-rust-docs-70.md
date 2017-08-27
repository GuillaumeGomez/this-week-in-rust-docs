---
layout: post
title: This Week in Rust Docs 70
date: 2017-8-27
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

The [rewrite of rustdoc](https://github.com/steveklabnik/rustdoc) is still under heavy development. Don't hesitate to give it a try!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@qnighy](https://github.com/qnighy) added [hints when intercrate ambiguity causes overlap](https://github.com/rust-lang/rust/pull/43426).
* [@huntiep](https://github.com/huntiep) improved [Try error messages](https://github.com/rust-lang/rust/pull/43984).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [new "Implementations on Foreign Types" section to traits in rustdoc](https://github.com/rust-lang/rust/pull/43849) and hid [internal types/traits from std docs via new #[doc(masked)] attribute](https://github.com/rust-lang/rust/pull/44026).
* [@zackmdavis](https://github.com/zackmdavis) added [comparison operators to must-use lint (under `fn_must_use` feature)](https://github.com/rust-lang/rust/pull/44103).
* [@ishitatsuyuki](https://github.com/ishitatsuyuki) made [unused-extern-crate warn-by-default](https://github.com/rust-lang/rust/pull/42588).
* [@llogiq](https://github.com/llogiq) added [a lowercase suggestion to unknown_lints](https://github.com/rust-lang/rust/pull/44104).
* [@gaurikholkar](https://github.com/gaurikholkar) extended [E0623 for LateBound and EarlyBound Regions](https://github.com/rust-lang/rust/pull/44079).
* [@oli-obk](https://github.com/oli-obk) added [clippy as a submodule](https://github.com/rust-lang/rust/pull/43886) and suggested [`Ok(())` when encountering `Result::<(), E>::Ok()`](https://github.com/rust-lang/rust/pull/44059).
* [@mystor](https://github.com/mystor) removed [highlight of # which does not start an attribute in rustdoc](https://github.com/rust-lang/rust/pull/43918).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings when rustdoc html rendering differs](https://github.com/rust-lang/rust/pull/41991), compile [fail stable](https://github.com/rust-lang/rust/pull/43949) and added [deref suggestion](https://github.com/rust-lang/rust/pull/43870).

# Recent doc contributions

* [@oli-obk](https://github.com/oli-obk) improved [placement of `use` suggestions](https://github.com/rust-lang/rust/pull/43929).
* [@ruuda](https://github.com/ruuda) pointed ["deref coercions" links to new book](https://github.com/rust-lang/rust/pull/43631).
* [@gaurikholkar](https://github.com/gaurikholkar) added [E0623 for structs](https://github.com/rust-lang/rust/pull/43700).
* [@shanavas786](https://github.com/shanavas786) fixed [typo in doc](https://github.com/rust-lang/rust/pull/43996).
* [@estebank](https://github.com/estebank) pointed [out missing if conditional](https://github.com/rust-lang/rust/pull/43854).
* [@lukaramu](https://github.com/lukaramu) fixed [inconsistent doc headings](https://github.com/rust-lang/rust/pull/44072).
* [@Jouan](https://github.com/Jouan) added [links for impls](https://github.com/rust-lang/rust/pull/43979).
* [@mattico](https://github.com/mattico) clarified [windows build instructions in README](https://github.com/rust-lang/rust/pull/44043).
* [@remexre](https://github.com/remexre) mentionned [null_mut on the pointer primitive docs](https://github.com/rust-lang/rust/pull/44039).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing links in docs](https://github.com/rust-lang/rust/pull/43978), removed [outline when details have focus](https://github.com/rust-lang/rust/pull/43977), removed [duplicates in rustdoc](https://github.com/rust-lang/rust/pull/43966), add [missing link in string doc](https://github.com/rust-lang/rust/pull/44090), add [missing links for Read trait](https://github.com/rust-lang/rust/pull/44010) and rollup [of 5 pull requests](https://github.com/rust-lang/rust/pull/44033).

# Meetings

Next meeting will be on Wednesday 30th of August 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
