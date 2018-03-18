---
layout: post
title: This Week in Rust Docs 97
date: 2018-3-18
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

* [@partim](https://github.com/partim) improved [documentation for Borrow, AsRef, and friends](https://github.com/rust-lang/rust/pull/46518).
* [@FraGag](https://github.com/FraGag) improved [documentation of Clone and Copy implementors](https://github.com/rust-lang/rust/pull/48171).
* [@tinaun](https://github.com/tinaun) removed [erroneous error message when checking impl trait params](https://github.com/rust-lang/rust/pull/48709).
* [@gaurikholkar](https://github.com/gaurikholkar) modified [E0389 error message](https://github.com/rust-lang/rust/pull/48914).
* [@phansch](https://github.com/phansch) added [more precise suggestion for non_upper_case_globals](https://github.com/rust-lang/rust/pull/48361).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) exposed [#[target_feature] attributes as doc(cfg) flags in rustdoc](https://github.com/rust-lang/rust/pull/48759), added [an "unstable features" chapter to the rustdoc book](https://github.com/rust-lang/rust/pull/49028) and suppressed [the default allow(unused) under --display-warnings in rustdoctest](https://github.com/rust-lang/rust/pull/49064).
* [@csmoe](https://github.com/csmoe) improved [error message of inner attribute syntax](https://github.com/rust-lang/rust/pull/49104).
* [@zackmdavis](https://github.com/zackmdavis) suggested [`!` instead of erroneous `not` on if/while block parse failure](https://github.com/rust-lang/rust/pull/48858).
* [@SimonSapin](https://github.com/SimonSapin) added [an example of lossy decoding to str::Utf8Error docs](https://github.com/rust-lang/rust/pull/49105).
* [@Phlosioneer](https://github.com/Phlosioneer) documented [when types have OS-dependent sizes](https://github.com/rust-lang/rust/pull/48932).
* [@ysiraichi](https://github.com/ysiraichi) suggested [removing `&`s](https://github.com/rust-lang/rust/pull/48834).
* [@RalfJung](https://github.com/RalfJung) improved [lint for type alias bounds](https://github.com/rust-lang/rust/pull/48909).
* [@klnusbaum](https://github.com/klnusbaum) provided [better borrow checker error message](https://github.com/rust-lang/rust/pull/48708) and renamed [epoch to edition](https://github.com/rust-lang/rust/pull/49035).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [error codes for libsyntax_ext](https://github.com/rust-lang/rust/pull/48173), added [warning for invalid start of code blocks in rustdoc](https://github.com/rust-lang/rust/pull/48596), and made [Atomic doc examples specific to each type](https://github.com/rust-lang/rust/pull/49029).

# Recent doc contributions

* [@estebank](https://github.com/estebank) reworded [E0044 and message for `!Send` types](https://github.com/rust-lang/rust/pull/48138).
* [@NovemberZulu](https://github.com/NovemberZulu) rephrased [UnsafeCell doc](https://github.com/rust-lang/rust/pull/48201).
* [@jethrogb](https://github.com/jethrogb) clarified [interfaction between File::set_len and file cursor](https://github.com/rust-lang/rust/pull/48480).
* [@ehuss](https://github.com/ehuss) added [crate name to "main function not found" error message](https://github.com/rust-lang/rust/pull/48706).
* [@focusaurus](https://github.com/focusaurus) saved [state of top-level collapse toggle widget in rust docs](https://github.com/rust-lang/rust/pull/48631).
* [@kennytm](https://github.com/kennytm) removed [unnecessary backtick in error message E0307 (invalid self type)](https://github.com/rust-lang/rust/pull/49042).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) re-enabled [testing librustdoc](https://github.com/rust-lang/rust/pull/49090) and tweaked [code fences in the rustdoc book](https://github.com/rust-lang/rust/pull/48964).
* [@mark-i-m](https://github.com/mark-i-m) moved [librustdoc readme to rustc guide](https://github.com/rust-lang/rust/pull/48972) and moved [librustc_typeck READMEs to rustc guide](https://github.com/rust-lang/rust/pull/48971).
* [@Songbird0](https://github.com/Songbird0) added [example of use of assertions in rustdoc](https://github.com/rust-lang/rust/pull/48961) and improved [`AddrParseError` documentation](https://github.com/rust-lang/rust/pull/48853).
* [@jsgf](https://github.com/jsgf) clarified [usage message for --remap-path-prefix](https://github.com/rust-lang/rust/pull/48991).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) put [back ui json check](https://github.com/rust-lang/rust/pull/48684), removed [auto trait implementation section when empty](https://github.com/rust-lang/rust/pull/48898), added [missing urls](https://github.com/rust-lang/rust/pull/48877), fixed [blink when main theme is selected](https://github.com/rust-lang/rust/pull/48831), added [missing examples](https://github.com/rust-lang/rust/pull/48970) and added [missing links](https://github.com/rust-lang/rust/pull/48954).

# Meetings

Next meeting will be on Tuesday 20th of March 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
