---
layout: post
title: This Week in Rust Docs 89
date: 2018-1-21
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

* [@estebank](https://github.com/estebank) highlighted [code on diagnostics when underlined](https://github.com/rust-lang/rust/pull/45752), suggested [casting on numeric type error](https://github.com/rust-lang/rust/pull/47247), added [a custom error when moving arg outside of its closure](https://github.com/rust-lang/rust/pull/47144), added [filtering options to `rustc_on_unimplemented`](https://github.com/rust-lang/rust/pull/47613), added [env flags `RUSTC_COLOR` and `RUSTC_ERROR_FORMAT`](https://github.com/rust-lang/rust/pull/46961), removed [private traits suggestions on missing method](https://github.com/rust-lang/rust/pull/47534) and included [space in suggestion `mut` in bindings](https://github.com/rust-lang/rust/pull/47465).
* [@SimonSapin](https://github.com/SimonSapin) documented [the size of bool](https://github.com/rust-lang/rust/pull/46156).
* [@partim](https://github.com/partim) improved [documentation for Borrow, AsRef, and friends](https://github.com/rust-lang/rust/pull/46518).
* [@clarcharr](https://github.com/clarcharr) documented [std::os::raw](https://github.com/rust-lang/rust/pull/46962).
* [@dbrgn](https://github.com/dbrgn) whitelisted [based suggestions](https://github.com/rust-lang/rust/pull/46815).
* [@vramana](https://github.com/vramana) improved [error messages in the case of partial and collateral moves for NLL](https://github.com/rust-lang/rust/pull/47020) and improved [move related error messages](https://github.com/rust-lang/rust/pull/47093).
* [@est31](https://github.com/est31) checked [for deadlinks from the summary during book generation](https://github.com/rust-lang/rust/pull/47423).
* [@Manishearth](https://github.com/Manishearth) implemented [RFC 1946 - intra-rustdoc links](https://github.com/rust-lang/rust/pull/47046).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.24.0](https://github.com/rust-lang/rust/pull/47286).
* [@sdroege](https://github.com/sdroege) fixed [broken links to other slice functions in chunks/chunks_mut/exact_…](https://github.com/rust-lang/rust/pull/47632).
* [@PieterPenninckx](https://github.com/PieterPenninckx) made [small improvements to the documentation of VecDeque](https://github.com/rust-lang/rust/pull/47595).
* [@astraw](https://github.com/astraw) fixed [doctests for BTreeSet to use BTreeSet (not BTreeMap)](https://github.com/rust-lang/rust/pull/47625).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [documentation from doc(include) to analysis data](https://github.com/rust-lang/rust/pull/47496).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [multiple themes support in rustdoc](https://github.com/rust-lang/rust/pull/47620) and added [E0659 for ambiguous names](https://github.com/rust-lang/rust/pull/47512).

# Recent doc contributions

* [@hellow554](https://github.com/hellow554) added [kbd style tag to main.css in rustdoc](https://github.com/rust-lang/rust/pull/46938).
* [@davidtwco](https://github.com/davidtwco) fixed [bad error message when converting anonymous lifetime to `'static` for NLL](https://github.com/rust-lang/rust/pull/47329).
* [@tspiteri](https://github.com/tspiteri) showed [that `f32::log` and `f64::log` are not correctly rounded in docs](https://github.com/rust-lang/rust/pull/47277).
* [@Manishearth](https://github.com/Manishearth) fixed [line offsets for doctests](https://github.com/rust-lang/rust/pull/47274).
* [@carols10cents](https://github.com/carols10cents) standardized [on "re-export" rather than "reexport"](https://github.com/rust-lang/rust/pull/47404).
* [@arthurprs](https://github.com/arthurprs) updated [BTreeMap recommendation](https://github.com/rust-lang/rust/pull/47578).
* [@estebank](https://github.com/estebank) removed [suggestion to make `mut` binding external to `Fn` closure](https://github.com/rust-lang/rust/pull/47468), pointed [at method with the requirements on E0283](https://github.com/rust-lang/rust/pull/47471) and pointed [at unused arguments for format string](https://github.com/rust-lang/rust/pull/47481).
* [@tbu-](https://github.com/tbu-) added [some edge cases to the documentation of `Path`](https://github.com/rust-lang/rust/pull/47532).
* [@goffrie](https://github.com/goffrie) removed [incorrect `Default::default` links, add a new one](https://github.com/rust-lang/rust/pull/47497).
* [@gaurikholkar](https://github.com/gaurikholkar) fixed [mispositioned span in suggestions with wide characters](https://github.com/rust-lang/rust/pull/47407).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [error code for unstable feature errors](https://github.com/rust-lang/rust/pull/47413), added [tests for rustdoc search](https://github.com/rust-lang/rust/pull/47250), switched [to pulldown as default markdown renderer](https://github.com/rust-lang/rust/pull/47398) and updated [html-diff crate (fix unicode parsing and invalid paths)](https://github.com/rust-lang/rust/pull/47436).

# Meetings

Next meeting will be on Tuesday 23rd of January 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
