---
layout: post
title: This Week in Rust Docs 86
date: 2017-12-17
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

* [@estebank](https://github.com/estebank) highlighted [code on diagnostics when underlined](https://github.com/rust-lang/rust/pull/45752), showed [closure signature on type errors](https://github.com/rust-lang/rust/pull/46350) and fixed [incorrect type mismatch label pointing at return type](https://github.com/rust-lang/rust/pull/46720).
* [@zackmdavis](https://github.com/zackmdavis) added [type error method suggestions use whitelisted identity-like conversions](https://github.com/rust-lang/rust/pull/46461).
* [@SimonSapin](https://github.com/SimonSapin) documented [the size of bool](https://github.com/rust-lang/rust/pull/46156).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.23.0](https://github.com/rust-lang/rust/pull/46327).
* [@partim](https://github.com/partim) improved [documentation for Borrow, AsRef, and friends](https://github.com/rust-lang/rust/pull/46518).
* [@MaloJaffre](https://github.com/MaloJaffre) added [compiler docs testing to CI](https://github.com/rust-lang/rust/pull/46278).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) removed [display of hidden types in rustdoc](https://github.com/rust-lang/rust/pull/46359), stabilized [allow_fail flag test feature](https://github.com/rust-lang/rust/pull/46501) and made [doc search more relevant](https://github.com/rust-lang/rust/pull/46700).

# Recent doc contributions

* [@estebank](https://github.com/estebank) resolved [type on return type suggestion](https://github.com/rust-lang/rust/pull/46608), pointed [at var in short lived borrows instead of drop location](https://github.com/rust-lang/rust/pull/46719) and pointed [at whole method call instead of args](https://github.com/rust-lang/rust/pull/46633).
* [@canndrew](https://github.com/canndrew) added [docs for never primitive](https://github.com/rust-lang/rust/pull/46232).
* [@zackmdavis](https://github.com/zackmdavis) added [one-time diagnostics for private enum variants glob reexport](https://github.com/rust-lang/rust/pull/46248).
* [@matthewjasper](https://github.com/matthewjasper) used [a better link for method resolution in Deref docs](https://github.com/rust-lang/rust/pull/46601).
* [@tshepang](https://github.com/tshepang) made [a better example in docs](https://github.com/rust-lang/rust/pull/46737).
* [@rillian](https://github.com/rillian) marked [ascii methods on primitive types stable in 1.23.0 not 1.21.0](https://github.com/rust-lang/rust/pull/46411).
* [@emilio](https://github.com/emilio) fixed [typo in infer README](https://github.com/rust-lang/rust/pull/46625).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [mobile doc style and improve search bar](https://github.com/rust-lang/rust/pull/46668), fixed [type filter in rustdoc js](https://github.com/rust-lang/rust/pull/46672) and fixed [switched types in type mismatch](https://github.com/rust-lang/rust/pull/46611).

# Meetings

Next meeting will be on Tuesday 19th of December 2017 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
