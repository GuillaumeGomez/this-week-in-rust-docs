---
layout: post
title: This Week in Rust Docs 95
date: 2018-3-4
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
* [@zilbuz](https://github.com/zilbuz) showed [the used type variable when issuing a "can't use type parameters from outer function" error message](https://github.com/rust-lang/rust/pull/47574).
* [@christianpoveda](https://github.com/christianpoveda) made [new Cell docs](https://github.com/rust-lang/rust/pull/48474).
* [@Phlosioneer](https://github.com/Phlosioneer) made [slight modification to the as_ref example of std::option::Option](https://github.com/rust-lang/rust/pull/48509).
* [@flip1995](https://github.com/flip1995) suggested [type for overflowing bin/hex-literals](https://github.com/rust-lang/rust/pull/48432).
* [@jethrogb](https://github.com/jethrogb) clarified [interfaction between File::set_len and file cursor](https://github.com/rust-lang/rust/pull/48480).
* [@lukaslueg](https://github.com/lukaslueg) fixed [spelling s/casted/cast/](https://github.com/rust-lang/rust/pull/48403).
* [@RalfJung](https://github.com/RalfJung) warned [about ignored generic bounds in `for`](https://github.com/rust-lang/rust/pull/48326).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.25.0](https://github.com/rust-lang/rust/pull/48374).
* [@scottmcm](https://github.com/scottmcm) improved [docs and associated SUCCESS/FAILURE for process::ExitCode](https://github.com/rust-lang/rust/pull/48618) and produced [better size_hints from Flatten & FlatMap](https://github.com/rust-lang/rust/pull/48544).
* [@tinaun](https://github.com/tinaun) removed [erroneous error message when checking impl trait params](https://github.com/rust-lang/rust/pull/48709).
* [@ehuss](https://github.com/ehuss) added [crate name to "main function not found" error message](https://github.com/rust-lang/rust/pull/48706).
* [@focusaurus](https://github.com/focusaurus) remember [state of top-level collapse toggle widget in rust docs](https://github.com/rust-lang/rust/pull/48631).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [resource-suffix option for rustdoc](https://github.com/rust-lang/rust/pull/48511), added [error codes for libsyntax_ext](https://github.com/rust-lang/rust/pull/48173), added [new warning for CStr::from_ptr](https://github.com/rust-lang/rust/pull/48507), updated [rustc --explain sentence](https://github.com/rust-lang/rust/pull/48559), put [back ui json check](https://github.com/rust-lang/rust/pull/48684) and added [warning for invalid start of code blocks in rustdoc](https://github.com/rust-lang/rust/pull/48596).

# Recent doc contributions

* [@estebank](https://github.com/estebank) provided [context for missing comma in match arm and if statement without block](https://github.com/rust-lang/rust/pull/48338).
* [@vi](https://github.com/vi) added [foldable impl blocks in rustdoc](https://github.com/rust-lang/rust/pull/47894).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [readme for librustdoc](https://github.com/rust-lang/rust/pull/48283).
* [@remexre](https://github.com/remexre) fixed [docs for ASCII functions to no longer claim U+0021 is '@'](https://github.com/rust-lang/rust/pull/48529).
* [@mark-i-m](https://github.com/mark-i-m) splitted [E0404 to E0909; get rid of E0245](https://github.com/rust-lang/rust/pull/48446) and started [moving to the rustc guide!](https://github.com/rust-lang/rust/pull/48479).
* [@frewsxcv](https://github.com/frewsxcv) clarified ["It is an error to..." wording for zero-duration behaviors](https://github.com/rust-lang/rust/pull/48328).
* [@Centril](https://github.com/Centril) documented [panics in Clone, PartialEq, PartialOrd, Ord for RefCell](https://github.com/rust-lang/rust/pull/48365).
* [@steveklabnik](https://github.com/steveklabnik) removed [production TOCs for doc markdown files](https://github.com/rust-lang/rust/pull/48680).
* [@teiesti](https://github.com/teiesti) fixed [link to rustc guide in README.md](https://github.com/rust-lang/rust/pull/48626).
* [@pthariensflame](https://github.com/pthariensflame) made a [minor grammatical/style fix in docs](https://github.com/rust-lang/rust/pull/48603).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added back [rustc explain](https://github.com/rust-lang/rust/pull/48337), added [rustdoc theme securities](https://github.com/rust-lang/rust/pull/48381) and fixed [auto trait impl rustdoc ice](https://github.com/rust-lang/rust/pull/48473).

# Meetings

Next meeting will be on Tuesday 6th of March 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
