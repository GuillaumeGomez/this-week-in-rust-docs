---
layout: post
title: This Week in Rust Docs 85
date: 2017-12-10
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

* [@estebank](https://github.com/estebank) highlighted [code on diagnostics when underlined](https://github.com/rust-lang/rust/pull/45752), showed [closure signature on type errors](https://github.com/rust-lang/rust/pull/46350) and resolved [type on return type suggestion](https://github.com/rust-lang/rust/pull/46608).
* [@canndrew](https://github.com/canndrew) added [docs for never primitive](https://github.com/rust-lang/rust/pull/46232).
* [@zackmdavis](https://github.com/zackmdavis) added [type error method suggestions use whitelisted identity-like conversions](https://github.com/rust-lang/rust/pull/46461) and added [one-time diagnostics for private enum variants glob reexport](https://github.com/rust-lang/rust/pull/46248).
* [@SimonSapin](https://github.com/SimonSapin) documented [the size of bool](https://github.com/rust-lang/rust/pull/46156).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.23.0](https://github.com/rust-lang/rust/pull/46327).
* [@partim](https://github.com/partim) improved [documentation for Borrow, AsRef, and friends](https://github.com/rust-lang/rust/pull/46518).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) turned [errors from loading external docs into a proper lint](https://github.com/rust-lang/rust/pull/46567).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) removed [display of hidden types in rustdoc](https://github.com/rust-lang/rust/pull/46359) and stabilized [allow_fail flag test feature](https://github.com/rust-lang/rust/pull/46501).

# Recent doc contributions

* [@estebank](https://github.com/estebank) displayed [`\t` in diagnostics code as four spaces](https://github.com/rust-lang/rust/pull/45953).
* [@JRegimbal](https://github.com/JRegimbal) changed ["Types/modules" title of search tab to be more accurate](https://github.com/rust-lang/rust/pull/45898).
* [@tbu-](https://github.com/tbu-) clarified [what `-D warnings` or `-F warnings` does](https://github.com/rust-lang/rust/pull/46136).
* [@nak3](https://github.com/nak3) fixed [invalid docs path for compiler plugins](https://github.com/rust-lang/rust/pull/46463) and fixed [invalid link to lint_plugin_test.rs](https://github.com/rust-lang/rust/pull/46465).
* [@tromey](https://github.com/tromey) fixed [documentation for DecodeUtf16Error](https://github.com/rust-lang/rust/pull/46432).
* [@steveklabnik](https://github.com/steveklabnik) mentionned [the name of ? in Result's docs](https://github.com/rust-lang/rust/pull/46431).
* [@vramana](https://github.com/vramana) fixed [bad error message for cannot_reborrow_already_uniquely_borrowed](https://github.com/rust-lang/rust/pull/46572).
* [@ollie27](https://github.com/ollie27) included [`impl [u8]` in the docs](https://github.com/rust-lang/rust/pull/46603).
* [@liigo](https://github.com/liigo) specified [that macro `cfg!` evaluating at compile-time](https://github.com/rust-lang/rust/pull/46416).
* [@AgustinCB](https://github.com/AgustinCB) modified [message for keyword as identifier name](https://github.com/rust-lang/rust/pull/46497).
* [@notriddle](https://github.com/notriddle) renamed [C-like enum to Field-less enum](https://github.com/rust-lang/rust/pull/46187).
* [@frewsxcv](https://github.com/frewsxcv) documented [behavior of `ptr::swap` with overlapping regions of memory](https://github.com/rust-lang/rust/pull/46483).
* [@Havvy](https://github.com/Havvy) added [compile_error macro examples](https://github.com/rust-lang/rust/pull/46512).
* [@timotree3](https://github.com/timotree3) updated [old link](https://github.com/rust-lang/rust/pull/46495).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings for markdown doc generation](https://github.com/rust-lang/rust/pull/46247), speedup [search loading when search url is received in rust docs](https://github.com/rust-lang/rust/pull/46221), fixed [deduplication of items in rust docs search](https://github.com/rust-lang/rust/pull/46433), fixed [search results overlap](https://github.com/rust-lang/rust/pull/46454), moved [colors to main.css](https://github.com/rust-lang/rust/pull/46444), fixed [switched types in type mismatch error](https://github.com/rust-lang/rust/pull/46611), fixed [doc important trait display on mobile](https://github.com/rust-lang/rust/pull/46586), greatly improved [sidebar when width < 700px](https://github.com/rust-lang/rust/pull/46526) and improved [search style](https://github.com/rust-lang/rust/pull/46502).

# Meetings

Next meeting will be on Tuesday 12th of December 2017 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
