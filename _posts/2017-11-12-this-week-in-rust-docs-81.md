---
layout: post
title: This Week in Rust Docs 81
date: 2017-11-12
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

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) included [external files in documentation in rustdoc (RFC 1990)](https://github.com/rust-lang/rust/pull/44781), showed [in docs whether the return type of a function impls Iterator/Read/Write](https://github.com/rust-lang/rust/pull/45039), added [talk about #![doc(test(no_crate_inject))] and #![doc(test(attr(...)))] in rustdoc](https://github.com/rust-lang/rust/pull/45767) and tweaked [notes on ignore/compile_fail examples in rustdoc](https://github.com/rust-lang/rust/pull/45815).
* [@Aaronepower](https://github.com/Aaronepower) updated [Release notes for 1.22.0](https://github.com/rust-lang/rust/pull/45454).
* [@estebank](https://github.com/estebank) highlighted [code on diagnostics when underlined](https://github.com/rust-lang/rust/pull/45776).
* [@steveklabnik](https://github.com/steveklabnik) started [shipping the Cargo book](https://github.com/rust-lang/rust/pull/45692).
* [@fhartwig](https://github.com/fhartwig) made [rustdoc not include self-by-value methods from Deref target](https://github.com/rust-lang/rust/pull/45645).
* [@JRegimbal](https://github.com/JRegimbal) change ["Types/modules" title of search tab to be more accurate](https://github.com/rust-lang/rust/pull/45898).
* [@pornel](https://github.com/pornel) remove [deprecated message](https://github.com/rust-lang/rust/pull/45828).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [search over generic types in docs](https://github.com/rust-lang/rust/pull/45673).

# Recent doc contributions

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [#[allow(unused)] to every doctest in rustdoc](https://github.com/rust-lang/rust/pull/45764).
* [@Havvy](https://github.com/Havvy) updated [reference link in doc's 404](https://github.com/rust-lang/rust/pull/45778).
* [@topecongiro](https://github.com/topecongiro) fixed [typos in README.md](https://github.com/rust-lang/rust/pull/45756).
* [@sdroege](https://github.com/sdroege) updated [the std::thread docs and clarified that panics can nowadays be caught](https://github.com/rust-lang/rust/pull/45714).
* [@ollie27](https://github.com/ollie27) fixed [duplicated impls with generics in rustdoc](https://github.com/rust-lang/rust/pull/45620).
* [@lukaramu](https://github.com/lukaramu) fixed [broken link markup in Hasher::finish docs](https://github.com/rust-lang/rust/pull/45919).
* [@xfix](https://github.com/xfix) allowed [a trailing comma in assert_eq/ne macro](https://github.com/rust-lang/rust/pull/45887).
* [@jhford](https://github.com/jhford) updated [get() example: it should use get() not get_mut()](https://github.com/rust-lang/rust/pull/45878).
* [@estebank](https://github.com/estebank) fixed [help for duplicated names: `extern crate (...) as (...)`](https://github.com/rust-lang/rust/pull/45856) and detected [`=` -> `:` typo in let bindings](https://github.com/rust-lang/rust/pull/45452).
* [@Badel2](https://github.com/Badel2) added [error for `...` in expressions](https://github.com/rust-lang/rust/pull/45773).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing links and examples](https://github.com/rust-lang/rust/pull/45582), added [missing docs for MetadataExt](https://github.com/rust-lang/rust/pull/45470), added [more elements in the sidebar](https://github.com/rust-lang/rust/pull/45766), added [missing links and examples for FileExt](https://github.com/rust-lang/rust/pull/45631), fixed [navbar click while in a search](https://github.com/rust-lang/rust/pull/45812), added [missing example for Debug trait](https://github.com/rust-lang/rust/pull/45869) and added ["-" shortcut in rust docs](https://github.com/rust-lang/rust/pull/45849).

# Meetings

Next meeting will be on Tuesday 14th of November 2017 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
