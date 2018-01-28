---
layout: post
title: This Week in Rust Docs 90
date: 2018-1-28
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

This week was a big one: the whole new [url system](https://github.com/rust-lang/rust/pull/47046) and the [multiple themes support](https://github.com/rust-lang/rust/pull/47620) have been added in rustdoc!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@estebank](https://github.com/estebank) highlighted [code on diagnostics when underlined](https://github.com/rust-lang/rust/pull/45752), added [filtering options to `rustc_on_unimplemented`](https://github.com/rust-lang/rust/pull/47613), added [env flags `RUSTC_COLOR` and `RUSTC_ERROR_FORMAT`](https://github.com/rust-lang/rust/pull/46961), included [space in suggestion `mut` in bindings](https://github.com/rust-lang/rust/pull/47465), tweaked [error message when reborrowing `&mut self` as `mut`](https://github.com/rust-lang/rust/pull/47818) and tweaked [presentation on lifetime trait mismatch](https://github.com/rust-lang/rust/pull/47791).
* [@SimonSapin](https://github.com/SimonSapin) documented [the size of bool](https://github.com/rust-lang/rust/pull/46156).
* [@partim](https://github.com/partim) improved [documentation for Borrow, AsRef, and friends](https://github.com/rust-lang/rust/pull/46518).
* [@clarcharr](https://github.com/clarcharr) documented [std::os::raw](https://github.com/rust-lang/rust/pull/46962) and move [Duration to libcore](https://github.com/rust-lang/rust/pull/46666).
* [@dbrgn](https://github.com/dbrgn) whitelisted [based suggestions](https://github.com/rust-lang/rust/pull/46815).
* [@vramana](https://github.com/vramana) improved [error messages in the case of partial and collateral moves for NLL](https://github.com/rust-lang/rust/pull/47020) and improved [move related error messages](https://github.com/rust-lang/rust/pull/47093).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.24.0](https://github.com/rust-lang/rust/pull/47286).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [documentation from doc(include) to analysis data](https://github.com/rust-lang/rust/pull/47496).
* [@steveklabnik](https://github.com/steveklabnik) updated [rust book](https://github.com/rust-lang/rust/pull/47753).
* [@varkor](https://github.com/varkor) added [line numbers and columns to error messages spanning multiple files](https://github.com/rust-lang/rust/pull/47780) and documented [the behaviour of infinite iterators on potentially-computable methods](https://github.com/rust-lang/rust/pull/47547).
* [@jimmantooth](https://github.com/jimmantooth) improved [punctuation and clarity](https://github.com/rust-lang/rust/pull/47515).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [tests for themes](https://github.com/rust-lang/rust/pull/47761) and fixed [themes rendering issues on mobile](https://github.com/rust-lang/rust/pull/47810).

# Recent doc contributions

* [@estebank](https://github.com/estebank) suggested [casting on numeric type error](https://github.com/rust-lang/rust/pull/47247), added [a custom error when moving arg outside of its closure](https://github.com/rust-lang/rust/pull/47144), removed [private traits suggestions on missing method](https://github.com/rust-lang/rust/pull/47534), correctly [formatted `extern crate` conflict resolution help](https://github.com/rust-lang/rust/pull/47767), pointed [at the "head" expression for E0277 on `for` loops, point](https://github.com/rust-lang/rust/pull/47690) and pointed [at unknown lang item attribute](https://github.com/rust-lang/rust/pull/47691).
* [@est31](https://github.com/est31) checked [for deadlinks from the summary during book generation](https://github.com/rust-lang/rust/pull/47423).
* [@Manishearth](https://github.com/Manishearth) implemented [RFC 1946 - intra-rustdoc links](https://github.com/rust-lang/rust/pull/47046) and fixed [intra-doc-links](https://github.com/rust-lang/rust/pull/47701).
* [@sdroege](https://github.com/sdroege) fixed [broken links to other slice functions in chunks/chunks_mut/exact_…](https://github.com/rust-lang/rust/pull/47632).
* [@PieterPenninckx](https://github.com/PieterPenninckx) made [small improvements to the documentation of VecDeque](https://github.com/rust-lang/rust/pull/47595).
* [@astraw](https://github.com/astraw) fixed [doctests for BTreeSet to use BTreeSet (not BTreeMap)](https://github.com/rust-lang/rust/pull/47625).
* [@ollie27](https://github.com/ollie27) removed [ methods from #[doc(masked)] crates from the search index in rustdoc](https://github.com/rust-lang/rust/pull/47675) and showed [when traits are auto traits in rustdoc](https://github.com/rust-lang/rust/pull/47672).
* [@evelynmitchell](https://github.com/evelynmitchell) fixed [invalid URL](https://github.com/rust-lang/rust/pull/47717).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [multiple themes support in rustdoc](https://github.com/rust-lang/rust/pull/47620), added [E0659 for ambiguous names](https://github.com/rust-lang/rust/pull/47512), fixed [experimental text display on default theme](https://github.com/rust-lang/rust/pull/47721), made [a few fixes for multiple themes support feature](https://github.com/rust-lang/rust/pull/47686) and fixed [quoted search](https://github.com/rust-lang/rust/pull/47667).

# Meetings

Next meeting will be on Tuesday 30th of January 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
