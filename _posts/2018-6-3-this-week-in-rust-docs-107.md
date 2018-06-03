---
layout: post
title: This Week in Rust Docs 107
date: 2018-6-3
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

Nothing important enough.

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/projects/1)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@fkjogu](https://github.com/fkjogu) documented [round-off error in `.mod_euc()`-method](https://github.com/rust-lang/rust/pull/50342).
* [@petrochenkov](https://github.com/petrochenkov) added [deprecation lint for duplicated `macro_export`s](https://github.com/rust-lang/rust/pull/50143) and stabilize [`use_extern_macros`](https://github.com/rust-lang/rust/pull/50911).
* [@mandeep](https://github.com/mandeep) added [doc comment to hiding portions of code example](https://github.com/rust-lang/rust/pull/50852).
* [@ogham](https://github.com/ogham) documented [Vec's particular IntoIter behaviour](https://github.com/rust-lang/rust/pull/51156), mentionned [spec and indented blocks in doctest docs](https://github.com/rust-lang/rust/pull/51158) and l
* [@kennytm](https://github.com/kennytm) pointed [to the rustdoc attribute where intralink resolution failed](https://github.com/rust-lang/rust/pull/51111).
* [@teiesti](https://github.com/teiesti) updated [rustdoc book to suggest using Termination trait instead of hidden ‘foo’ function](https://github.com/rust-lang/rust/pull/51183).
* [@kornelski](https://github.com/kornelski) used [String, not &str in some collection examples](https://github.com/rust-lang/rust/pull/51081).
* [@avdv](https://github.com/avdv) fixed [confusing error message for sub_instant](https://github.com/rust-lang/rust/pull/51255).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.27.0](https://github.com/rust-lang/rust/pull/51261).
* [@cmdd](https://github.com/cmdd) added [error message for using >= 65535 hashes for raw string literal escapes](https://github.com/rust-lang/rust/pull/50296).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [extern prelude failure in rustdoc](https://github.com/rust-lang/rust/pull/50617), introduce [the #[doc(keyword="")] attribute for documenting keywords](https://github.com/rust-lang/rust/pull/51140) and fixed [crate-name option in rustdoc](https://github.com/rust-lang/rust/pull/51256).

# Recent doc contributions

* [@F001](https://github.com/F001) added [lint for multiple associated types](https://github.com/rust-lang/rust/pull/50682).
* [@frewsxcv](https://github.com/frewsxcv) provided [more context for what the {f32,f64}::EPSILON values represent](https://github.com/rust-lang/rust/pull/50919), clarified [the difference between get_mut and into_mut for OccupiedEntry](https://github.com/rust-lang/rust/pull/51312), reworded [{ptr,mem}::replace docs](https://github.com/rust-lang/rust/pull/51124) and added [doc link from discriminant struct to function](https://github.com/rust-lang/rust/pull/51127).
* [@davidtwco](https://github.com/davidtwco) added [rustdoc documentation to compiler docs](https://github.com/rust-lang/rust/pull/50892).
* [@simartin](https://github.com/simartin) improved [error diagnostic with missing commas after struct fields](https://github.com/rust-lang/rust/pull/50914).
* [@d-e-s-o](https://github.com/d-e-s-o) fixed [typo in cell.rs](https://github.com/rust-lang/rust/pull/50913).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) used ["short form" doc(cfg) printing even when combined with other conditionals in rustdoc](https://github.com/rust-lang/rust/pull/50875) and hid [macro export statements from docs](https://github.com/rust-lang/rust/pull/51011).
* [@euclio](https://github.com/euclio) used [type name in E0599 enum variant suggestion](https://github.com/rust-lang/rust/pull/51313).
* [@evincarofautumn](https://github.com/evincarofautumn) fixed [typos of ‘ambiguous’](https://github.com/rust-lang/rust/pull/51291).
* [@steveklabnik](https://github.com/steveklabnik) removed [feature flag from fs::read_to_string example](https://github.com/rust-lang/rust/pull/51272).
* [@petrochenkov](https://github.com/petrochenkov) fixed [naming conventions for new lints](https://github.com/rust-lang/rust/pull/50879).
* [@crlf0710](https://github.com/crlf0710) replaced [`if` with `if and only if` in the definition dox of `Sync`](https://github.com/rust-lang/rust/pull/51152).
* [@estebank](https://github.com/estebank) tweaked [output on E0599 for assoc fn used as method](https://github.com/rust-lang/rust/pull/51135) and suggested [using `as_ref` on some borrow errors [hack]](https://github.com/rust-lang/rust/pull/51100).
* [@akoserwal](https://github.com/akoserwal) updated [build instructions](https://github.com/rust-lang/rust/pull/51123).
* [@RalfJung](https://github.com/RalfJung) extended [from_raw_parts docs for slices and strs to mention alignment requirement](https://github.com/rust-lang/rust/pull/51134).
* [@nickbabcock](https://github.com/nickbabcock) documented [additional use case for iter::inspect](https://github.com/rust-lang/rust/pull/51142).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) stabilized [short error format](https://github.com/rust-lang/rust/pull/49546), added [E0665](https://github.com/rust-lang/rust/pull/50846), fixed [run button style](https://github.com/rust-lang/rust/pull/51297), added [attributes for trait and methods as well](https://github.com/rust-lang/rust/pull/50953), stabilize [Formatter alignment](https://github.com/rust-lang/rust/pull/51078), added [missing whitespace in num example](https://github.com/rust-lang/rust/pull/51262) and fixed [some style issues in rustdoc "implementations on Foreign types"](https://github.com/rust-lang/rust/pull/51193).

# Meetings

Next meeting will be on Tuesday 5th of June 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
