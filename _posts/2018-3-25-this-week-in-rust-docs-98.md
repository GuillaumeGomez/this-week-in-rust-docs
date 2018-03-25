---
layout: post
title: This Week in Rust Docs 98
date: 2018-3-25
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

Nothing interesting enough.

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@FraGag](https://github.com/FraGag) improved [documentation of Clone and Copy implementors](https://github.com/rust-lang/rust/pull/48171).
* [@tinaun](https://github.com/tinaun) removed [erroneous error message when checking impl trait params](https://github.com/rust-lang/rust/pull/48709).
* [@gaurikholkar](https://github.com/gaurikholkar) modified [E0389 error message](https://github.com/rust-lang/rust/pull/48914).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) suppressed [the default allow(unused) under --display-warnings in rustdoctest](https://github.com/rust-lang/rust/pull/49064) and moved [the "important traits" button to beside the type in rustdoc](https://github.com/rust-lang/rust/pull/49286).
* [@Phlosioneer](https://github.com/Phlosioneer) documented [when types have OS-dependent sizes](https://github.com/rust-lang/rust/pull/48932).
* [@klnusbaum](https://github.com/klnusbaum) provided [better borrow checker error message](https://github.com/rust-lang/rust/pull/48708).
* [@pthariensflame](https://github.com/pthariensflame) made [a minor message/label formatting consistency fix](https://github.com/rust-lang/rust/pull/49351).
* [@krk](https://github.com/krk) added [submodule fetch instructions](https://github.com/rust-lang/rust/pull/49338).
* [@chisophugis](https://github.com/chisophugis) fixed [confusing doc for `scan`](https://github.com/rust-lang/rust/pull/49353).
* [@sinkuu](https://github.com/sinkuu) added [support for universal_impl_trait in rustdoc](https://github.com/rust-lang/rust/pull/49304).
* [@PramodBisht](https://github.com/PramodBisht) fixed [doc comments present after a particular syntax error cause an unhelpful error message to be output](https://github.com/rust-lang/rust/pull/48946).
* [@zackmdavis](https://github.com/zackmdavis) added [suggestion of `!` for erroneous identifier `not`](https://github.com/rust-lang/rust/pull/49258) and pointed [to value in "value assigned is never read" lint](https://github.com/rust-lang/rust/pull/49197).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [error codes for libsyntax_ext](https://github.com/rust-lang/rust/pull/48173), fixed [impl assoc constant link not working](https://github.com/rust-lang/rust/pull/49333), removed [unneeded trait implementations titles](https://github.com/rust-lang/rust/pull/49335), added [repeat method on slice](https://github.com/rust-lang/rust/pull/48999) and proposed [a variant if it is an enum for E0599](https://github.com/rust-lang/rust/pull/49223).

# Recent doc contributions

* [@partim](https://github.com/partim) improved [documentation for Borrow, AsRef, and friends](https://github.com/rust-lang/rust/pull/46518).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) exposed [#[target_feature] attributes as doc(cfg) flags in rustdoc](https://github.com/rust-lang/rust/pull/48759), added [an "unstable features" chapter to the rustdoc book](https://github.com/rust-lang/rust/pull/49028) and whitelisted [every target feature for rustdoc](https://github.com/rust-lang/rust/pull/49225).
* [@csmoe](https://github.com/csmoe) improved [error message of inner attribute syntax](https://github.com/rust-lang/rust/pull/49104).
* [@SimonSapin](https://github.com/SimonSapin) added [an example of lossy decoding to str::Utf8Error docs](https://github.com/rust-lang/rust/pull/49105) and fixed [incorrect copy-paste for new `X?` in formatting strings](https://github.com/rust-lang/rust/pull/49161).
* [@ysiraichi](https://github.com/ysiraichi) suggested [removing `&`s](https://github.com/rust-lang/rust/pull/48834).
* [@RalfJung](https://github.com/RalfJung) improved [lint for type alias bounds](https://github.com/rust-lang/rust/pull/48909).
* [@klnusbaum](https://github.com/klnusbaum) renamed [epoch to edition](https://github.com/rust-lang/rust/pull/49035).
* [@steveklabnik](https://github.com/steveklabnik) updated [books for next release](https://github.com/rust-lang/rust/pull/49318).
* [@ordovicia](https://github.com/ordovicia) improved [diagnostics for '..' pattern fragment not in the last position](https://github.com/rust-lang/rust/pull/49268).
* [@Centril](https://github.com/Centril) documented [format_args! / Arguments<'a> behavior wrt. Display and Debug](https://github.com/rust-lang/rust/pull/49229).
* [@davidtwco](https://github.com/davidtwco) hosted [compiler documentation](https://github.com/rust-lang/rust/pull/49193).
* [@sanxiyn](https://github.com/sanxiyn) documented [only-X test header](https://github.com/rust-lang/rust/pull/49169).
* [@estebank](https://github.com/estebank) reduced [the diagnostic spam when multiple fields are missing in pattern](https://github.com/rust-lang/rust/pull/49160).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.25.0](https://github.com/rust-lang/rust/pull/48374).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warning for invalid start of code blocks in rustdoc](https://github.com/rust-lang/rust/pull/48596), and made [Atomic doc examples specific to each type](https://github.com/rust-lang/rust/pull/49029), fixed [IE11 search](https://github.com/rust-lang/rust/pull/49312), fixed [automatic urls with backticks](https://github.com/rust-lang/rust/pull/49189) and fixed [events handling in rustdoc](https://github.com/rust-lang/rust/pull/49152).

# Meetings

Next meeting will be on Tuesday 27th of March 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
