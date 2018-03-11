---
layout: post
title: This Week in Rust Docs 96
date: 2018-3-11
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

* [@estebank](https://github.com/estebank) reworded [E0044 and message for `!Send` types](https://github.com/rust-lang/rust/pull/48138) and suggested [setting associated type when type argument is given instead](https://github.com/rust-lang/rust/pull/48288).
* [@partim](https://github.com/partim) improved [documentation for Borrow, AsRef, and friends](https://github.com/rust-lang/rust/pull/46518).
* [@NovemberZulu](https://github.com/NovemberZulu) rephrased [UnsafeCell doc](https://github.com/rust-lang/rust/pull/48201).
* [@FraGag](https://github.com/FraGag) improved [documentation of Clone and Copy implementors](https://github.com/rust-lang/rust/pull/48171).
* [@jethrogb](https://github.com/jethrogb) clarified [interfaction between File::set_len and file cursor](https://github.com/rust-lang/rust/pull/48480).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.25.0](https://github.com/rust-lang/rust/pull/48374).
* [@tinaun](https://github.com/tinaun) removed [erroneous error message when checking impl trait params](https://github.com/rust-lang/rust/pull/48709).
* [@ehuss](https://github.com/ehuss) added [crate name to "main function not found" error message](https://github.com/rust-lang/rust/pull/48706).
* [@focusaurus](https://github.com/focusaurus) saved [state of top-level collapse toggle widget in rust docs](https://github.com/rust-lang/rust/pull/48631).
* [@gaurikholkar](https://github.com/gaurikholkar) modified [E0389 error message](https://github.com/rust-lang/rust/pull/48914).
* [@phansch](https://github.com/phansch) added [more precise suggestion for non_upper_case_globals](https://github.com/rust-lang/rust/pull/48361).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) exposed [#[target_feature] attributes as doc(cfg) flags in rustdoc](https://github.com/rust-lang/rust/pull/48759).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [error codes for libsyntax_ext](https://github.com/rust-lang/rust/pull/48173), updated [rustc --explain sentence](https://github.com/rust-lang/rust/pull/48559), put [back ui json check](https://github.com/rust-lang/rust/pull/48684), added [warning for invalid start of code blocks in rustdoc](https://github.com/rust-lang/rust/pull/48596), removed [auto trait implementation section when empty](https://github.com/rust-lang/rust/pull/48898), added [missing urls](https://github.com/rust-lang/rust/pull/48877) and fixed [blink when main theme is selected](https://github.com/rust-lang/rust/pull/48831).

# Recent doc contributions

* [@zilbuz](https://github.com/zilbuz) showed [the used type variable when issuing a "can't use type parameters from outer function" error message](https://github.com/rust-lang/rust/pull/47574).
* [@christianpoveda](https://github.com/christianpoveda) made [new Cell docs](https://github.com/rust-lang/rust/pull/48474).
* [@Phlosioneer](https://github.com/Phlosioneer) made [slight modification to the as_ref example of std::option::Option](https://github.com/rust-lang/rust/pull/48509).
* [@flip1995](https://github.com/flip1995) suggested [type for overflowing bin/hex-literals](https://github.com/rust-lang/rust/pull/48432).
* [@lukaslueg](https://github.com/lukaslueg) fixed [spelling s/casted/cast/](https://github.com/rust-lang/rust/pull/48403).
* [@RalfJung](https://github.com/RalfJung) warned [about ignored generic bounds in `for`](https://github.com/rust-lang/rust/pull/48326).
* [@scottmcm](https://github.com/scottmcm) improved [docs and associated SUCCESS/FAILURE for process::ExitCode](https://github.com/rust-lang/rust/pull/48618).
* [@Songbird0](https://github.com/Songbird0) modified [part of `line!` documentation](https://github.com/rust-lang/rust/pull/48856), modified [part of `column!` documentation](https://github.com/rust-lang/rust/pull/48857) and added [a potential cause raising `ParseIntError`](https://github.com/rust-lang/rust/pull/48738).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [resource-suffix option for rustdoc](https://github.com/rust-lang/rust/pull/48511), added [new warning for CStr::from_ptr](https://github.com/rust-lang/rust/pull/48507), multiple [rustdoc fixes](https://github.com/rust-lang/rust/pull/48755), fix [sidebar horizontal scroll](https://github.com/rust-lang/rust/pull/48789) and raw [string error note](https://github.com/rust-lang/rust/pull/48546).

# Meetings

Next meeting will be on Tuesday 13th of March 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
