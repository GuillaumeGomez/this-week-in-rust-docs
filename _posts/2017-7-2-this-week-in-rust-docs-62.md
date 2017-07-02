---
layout: post
title: This Week in Rust Docs 62
date: 2017-7-2
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

After a long debate, it has been decided to keep hoedown testing/rendering by default in rustdoc. However, you can test pulldown by running rustdoc with `-Z unstable-options enable-commonmark`.

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@oli-obk](https://github.com/oli-obk) changed [some notes into suggestions](https://github.com/rust-lang/rust/pull/42033).
* [@Aaronepower](https://github.com/Aaronepower) updated [releases notes for 1.19](https://github.com/rust-lang/rust/pull/42503).
* [@frewsxcv](https://github.com/frewsxcv) fixed [a couple broken links to the reference from error messages](https://github.com/rust-lang/rust/pull/42624).
* [@rthomas](https://github.com/rthomas) updated [docs on Error struct](https://github.com/rust-lang/rust/pull/42837) and updated [docs for Debug* structs](https://github.com/rust-lang/rust/pull/42836).
* [@cengizIO](https://github.com/cengizIO) added [pager support for `rustc --explain EXXXX`](https://github.com/rust-lang/rust/pull/42732).
* [@Fourchaux](https://github.com/Fourchaux) fixed [basic typos in Doc Comments](https://github.com/rust-lang/rust/pull/42812).
* [@dns2utf8](https://github.com/dns2utf8) added [hint about the return code of panic!](https://github.com/rust-lang/rust/pull/42670).
* [@Emilgardis](https://github.com/Emilgardis) fixed [wrong report on closure args mismatch when a ref is expected but not found](https://github.com/rust-lang/rust/pull/42270).
* [@Boreeas](https://github.com/Boreeas) folded [E0612, E0613 into E0609](https://github.com/rust-lang/rust/pull/42996).
* [@estebank](https://github.com/estebank) added [`rustc_on_unimplemented` message to `std::ops::Try`](https://github.com/rust-lang/rust/pull/43001) and made [suggestion include the line number](https://github.com/rust-lang/rust/pull/42904).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) refactored [pretty printing slightly](https://github.com/rust-lang/rust/pull/42897) and allowed [setting the limit on std::io::Take](https://github.com/rust-lang/rust/pull/42697).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings when rustdoc html rendering differs](https://github.com/rust-lang/rust/pull/41991), added [errors when doc comments are added where they're unused](https://github.com/rust-lang/rust/pull/43009), cleaned [up some code](https://github.com/rust-lang/rust/pull/43006) and fixed [toggle wrappers not generated correctly in rustdoc](https://github.com/rust-lang/rust/pull/42972).

# Recent doc contributions

* [@pwoolcoc](https://github.com/pwoolcoc) added [`allow_fail` test attribute](https://github.com/rust-lang/rust/pull/42219).
* [@ollie27](https://github.com/ollie27) fixed [a few issues with associated consts in rustdoc](https://github.com/rust-lang/rust/pull/42865) and fixed [ICE on `use *;` in rustdoc](https://github.com/rust-lang/rust/pull/42885).
* [@rthomas](https://github.com/rthomas) updated [docs for fmt::write](https://github.com/rust-lang/rust/pull/42831) and updated [docs for std::fmt::format](https://github.com/rust-lang/rust/pull/42832).
* [@gaurikholkar](https://github.com/gaurikholkar) added [diagnostic code for lifetime errors with one named, one anonymous lifetime parameter](https://github.com/rust-lang/rust/pull/42669).
* [@tbu-](https://github.com/tbu-) documented [possible `io::ErrorKind`s of `fs::open`](https://github.com/rust-lang/rust/pull/42925).
* [@matklad](https://github.com/matklad) documented [that `/` works as separator on Windows](https://github.com/rust-lang/rust/pull/42955).
* [@estebank](https://github.com/estebank) added [missing `;` detection on methods with return type `()`](https://github.com/rust-lang/rust/pull/42850).
* [@AndiDog](https://github.com/AndiDog) fixed [compile-error.md link reference](https://github.com/rust-lang/rust/pull/42946).
* [@casey](https://github.com/casey) reworded [OsStr docs to clarify that utf8 may contain nulls](https://github.com/rust-lang/rust/pull/42905).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) created [more error codes](https://github.com/rust-lang/rust/pull/42519), removed [err methods](https://github.com/rust-lang/rust/pull/42887) and added [E0619 error explanation](https://github.com/rust-lang/rust/pull/42957).

# Meetings

Next meeting will be on Wednesday 5th of July 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
