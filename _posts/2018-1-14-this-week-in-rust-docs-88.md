---
layout: post
title: This Week in Rust Docs 88
date: 2018-1-14
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

The hoedown -> pulldown migration moved forward by a step this last week: now the default renderer is pulldown.

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@estebank](https://github.com/estebank) highlighted [code on diagnostics when underlined](https://github.com/rust-lang/rust/pull/45752), suggested [casting on numeric type error](https://github.com/rust-lang/rust/pull/47247) and added [a custom error when moving arg outside of its closure](https://github.com/rust-lang/rust/pull/47144).
* [@SimonSapin](https://github.com/SimonSapin) documented [the size of bool](https://github.com/rust-lang/rust/pull/46156).
* [@partim](https://github.com/partim) improved [documentation for Borrow, AsRef, and friends](https://github.com/rust-lang/rust/pull/46518).
* [@clarcharr](https://github.com/clarcharr) documented [std::os::raw](https://github.com/rust-lang/rust/pull/46962), better [Debug impl for io::Error](https://github.com/rust-lang/rust/pull/47120).
* [@hellow554](https://github.com/hellow554) added [kbd style tag to main.css in rustdoc](https://github.com/rust-lang/rust/pull/46938).
* [@dbrgn](https://github.com/dbrgn) whitelisted [based suggestions](https://github.com/rust-lang/rust/pull/46815).
* [@vramana](https://github.com/vramana) improved [error messages in the case of partial and collateral moves for NLL](https://github.com/rust-lang/rust/pull/47020) and improved [move related error messages](https://github.com/rust-lang/rust/pull/47093).
* [@etaoins](https://github.com/etaoins) extended [macro name suggestion span](https://github.com/rust-lang/rust/pull/47424).
* [@davidtwco](https://github.com/davidtwco) fixed [bad error message when converting anonymous lifetime to `'static` for NLL](https://github.com/rust-lang/rust/pull/47329).
* [@est31](https://github.com/est31) checked [for deadlinks from the summary during book generation](https://github.com/rust-lang/rust/pull/47423).
* [@tspiteri](https://github.com/tspiteri) showed [that `f32::log` and `f64::log` are not correctly rounded in docs](https://github.com/rust-lang/rust/pull/47277).
* [@Manishearth](https://github.com/Manishearth) fixed [line offsets for doctests](https://github.com/rust-lang/rust/pull/47274) and implemented [RFC 1946 - intra-rustdoc links](https://github.com/rust-lang/rust/pull/47046).
* [@carols10cents](https://github.com/carols10cents) standardized [on "re-export" rather than "reexport"](https://github.com/rust-lang/rust/pull/47404).
* [@ollie27](https://github.com/ollie27) populated [external_traits with traits only seen in impls in rustdoc](https://github.com/rust-lang/rust/pull/47313).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.24.0](https://github.com/rust-lang/rust/pull/47286).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) stabilized [allow_fail flag test feature](https://github.com/rust-lang/rust/pull/46501), added [error code for unstable feature errors](https://github.com/rust-lang/rust/pull/47413), test [rustdoc js](https://github.com/rust-lang/rust/pull/47250) and switched [to pulldown as default markdown renderer](https://github.com/rust-lang/rust/pull/47398).

# Recent doc contributions

* [@estebank](https://github.com/estebank) provided [suggestion when trying to use method on numeric literal](https://github.com/rust-lang/rust/pull/47171).
* [@zackmdavis](https://github.com/zackmdavis) added [type error method suggestions use whitelisted identity-like conversions](https://github.com/rust-lang/rust/pull/46461) and fixed [the doc-comment-decoration-trimming edge-case rustdoc ICE](https://github.com/rust-lang/rust/pull/47210).
* [@keatinge](https://github.com/keatinge) added [help message for incorrect pattern syntax](https://github.com/rust-lang/rust/pull/47232).
* [@ollie27](https://github.com/ollie27) added [missing src links for generic impls on trait pages in rustdoc](https://github.com/rust-lang/rust/pull/47039).
* [@whentze](https://github.com/whentze) fixed [docs for OsStr](https://github.com/rust-lang/rust/pull/47357).
* [@overvenus](https://github.com/overvenus) fixed [examples of Duration::subsec_millis and Duration::subsec_micros](https://github.com/rust-lang/rust/pull/47375).
* [@alercah](https://github.com/alercah) fixed [typo](https://github.com/rust-lang/rust/pull/47340).

# Meetings

Next meeting will be on Tuesday 16th of January 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
