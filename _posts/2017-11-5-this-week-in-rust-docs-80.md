---
layout: post
title: This Week in Rust Docs 80
date: 2017-11-5
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

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) included [external files in documentation in rustdoc (RFC 1990)](https://github.com/rust-lang/rust/pull/44781), showed [in docs whether the return type of a function impls Iterator/Read/Write](https://github.com/rust-lang/rust/pull/45039), added [#[allow(unused)] to every doctest in rustdoc](https://github.com/rust-lang/rust/pull/45764) and added [talk about #![doc(test(no_crate_inject))] and #![doc(test(attr(...)))] in rustdoc](https://github.com/rust-lang/rust/pull/45767).
* [@Aaronepower](https://github.com/Aaronepower) updated [Release notes for 1.22.0](https://github.com/rust-lang/rust/pull/45454).
* [@estebank](https://github.com/estebank) highlighted [code on diagnostics when underlined](https://github.com/rust-lang/rust/pull/45776) and highlighted [code on diagnostics when underlined](https://github.com/rust-lang/rust/pull/45752).
* [@Havvy](https://github.com/Havvy) updated [reference link in doc's 404](https://github.com/rust-lang/rust/pull/45778).
* [@topecongiro](https://github.com/topecongiro) fixed [typos in README.md](https://github.com/rust-lang/rust/pull/45756).
* [@steveklabnik](https://github.com/steveklabnik) started [shipping the Cargo book](https://github.com/rust-lang/rust/pull/45692).
* [@sdroege](https://github.com/sdroege) updated [the std::thread docs and clarified that panics can nowadays be caught](https://github.com/rust-lang/rust/pull/45714).
* [@fhartwig](https://github.com/fhartwig) made [rustdoc not include self-by-value methods from Deref target](https://github.com/rust-lang/rust/pull/45645).
* [@ollie27](https://github.com/ollie27) fixed [duplicated impls with generics in rustdoc](https://github.com/rust-lang/rust/pull/45620).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing links and examples](https://github.com/rust-lang/rust/pull/45582), added [missing docs for MetadataExt](https://github.com/rust-lang/rust/pull/45470), added [more elements in the sidebar](https://github.com/rust-lang/rust/pull/45766), added [search over generic types in docs](https://github.com/rust-lang/rust/pull/45673) and added [missing links and examples for FileExt](https://github.com/rust-lang/rust/pull/45631).

# Recent doc contributions

* [@joshleeb](https://github.com/joshleeb) fixed [duplicated display of error E0502](https://github.com/rust-lang/rust/pull/45603) and improved [display of error E0308](https://github.com/rust-lang/rust/pull/45630).
* [@leodasvacas](https://github.com/leodasvacas) documented [that call expressions also represent ADT constructors](https://github.com/rust-lang/rust/pull/45579).
* [@tirr-c](https://github.com/tirr-c) displayed [spans correctly when there are zero-width or wide characters](https://github.com/rust-lang/rust/pull/45711).
* [@Ljzn](https://github.com/Ljzn) fixed [typo](https://github.com/rust-lang/rust/pull/45718) and fixed [typo](https://github.com/rust-lang/rust/pull/45681).
* [@LaurentMazare](https://github.com/LaurentMazare) added [a nicer error message for missing in for loop, fixes #40782](https://github.com/rust-lang/rust/pull/45639).
* [@Cldfire](https://github.com/Cldfire) suggested [renaming import if names clash](https://github.com/rust-lang/rust/pull/45660).
* [@mbrubeck](https://github.com/mbrubeck) fixed [incorrect error type in Read::byte docs](https://github.com/rust-lang/rust/pull/45664).
* [@carols10cents](https://github.com/carols10cents) updated [the book for a fix to the print button](https://github.com/rust-lang/rust/pull/45554).
* [@Technius](https://github.com/Technius) improved [std::process module docs](https://github.com/rust-lang/rust/pull/45295).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) improved [sidebar rendering and added methods list](https://github.com/rust-lang/rust/pull/45187), fixed [title heading overlap in rust doc](https://github.com/rust-lang/rust/pull/45450), search [fixes](https://github.com/rust-lang/rust/pull/45617) and added [tests for methods listing in rust docs](https://github.com/rust-lang/rust/pull/45746).

# Meetings

Next meeting will be on Tuesday 7th of November 2017 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
