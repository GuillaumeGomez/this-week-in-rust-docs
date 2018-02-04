---
layout: post
title: This Week in Rust Docs 91
date: 2018-2-4
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

* [@estebank](https://github.com/estebank) added [filtering options to `rustc_on_unimplemented`](https://github.com/rust-lang/rust/pull/47613) and added [`-Zteach` documentation](https://github.com/rust-lang/rust/pull/47843).
* [@partim](https://github.com/partim) improved [documentation for Borrow, AsRef, and friends](https://github.com/rust-lang/rust/pull/46518).
* [@clarcharr](https://github.com/clarcharr) documented [std::os::raw](https://github.com/rust-lang/rust/pull/46962).
* [@dbrgn](https://github.com/dbrgn) whitelisted [based suggestions](https://github.com/rust-lang/rust/pull/46815).
* [@vramana](https://github.com/vramana) improved [error messages in the case of partial and collateral moves for NLL](https://github.com/rust-lang/rust/pull/47020) and improved [move related error messages](https://github.com/rust-lang/rust/pull/47093).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [documentation from doc(include) to analysis data](https://github.com/rust-lang/rust/pull/47496).
* [@steveklabnik](https://github.com/steveklabnik) updated [rust book](https://github.com/rust-lang/rust/pull/47753).
* [@varkor](https://github.com/varkor) documented [the behaviour of infinite iterators on potentially-computable methods](https://github.com/rust-lang/rust/pull/47547).
* [@Manishearth](https://github.com/Manishearth) fixed [rustdoc ICE on macros defined within functions](https://github.com/rust-lang/rust/pull/47959).
* [@frewsxcv](https://github.com/frewsxcv) clarified [shared file handler behavior of File::try_clone](https://github.com/rust-lang/rust/pull/47958).
* [@vi](https://github.com/vi) added [foldable impl blocks in rustdoc](https://github.com/rust-lang/rust/pull/47894).
* [@wesleywiser](https://github.com/wesleywiser) fixed [how paths are printed by error messages during bootstrap](https://github.com/rust-lang/rust/pull/47731).
* [@Aaron1011](https://github.com/Aaron1011) generated [documentation for auto-trait impls](https://github.com/rust-lang/rust/pull/47833).
* [@zackmdavis](https://github.com/zackmdavis) declined [to lint technically-unnecessary parens in function or method arguments inside of nested macros](https://github.com/rust-lang/rust/pull/47896) and corrected [unused field pattern suggestions](https://github.com/rust-lang/rust/pull/47922).
* [@PramodBisht](https://github.com/PramodBisht) changed [color of struct link from #ff794d to #2dbfb8 for Rust docs](https://github.com/rust-lang/rust/pull/47806).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [tests for themes](https://github.com/rust-lang/rust/pull/47761), fixed [themes rendering issues on mobile](https://github.com/rust-lang/rust/pull/47810) and fixed [const evaluation ICE in rustdoc](https://github.com/rust-lang/rust/pull/47862).

# Recent doc contributions

* [@estebank](https://github.com/estebank) highlighted [code on diagnostics when underlined](https://github.com/rust-lang/rust/pull/45752), included [space in suggestion `mut` in bindings](https://github.com/rust-lang/rust/pull/47465), tweaked [presentation on lifetime trait mismatch](https://github.com/rust-lang/rust/pull/47791), minimized [weird spans involving macro context](https://github.com/rust-lang/rust/pull/47942) and suggested [removing value from `break` when invalid](https://github.com/rust-lang/rust/pull/47829).
* [@SimonSapin](https://github.com/SimonSapin) documented [the size of bool](https://github.com/rust-lang/rust/pull/46156).
* [@varkor](https://github.com/varkor) added [line numbers and columns to error messages spanning multiple files](https://github.com/rust-lang/rust/pull/47780).
* [@jimmantooth](https://github.com/jimmantooth) improved [punctuation and clarity](https://github.com/rust-lang/rust/pull/47515).
* [@vmx](https://github.com/vmx) fixed [lang items box example code](https://github.com/rust-lang/rust/pull/47916).
* [@etaoins](https://github.com/etaoins) improved [char escaping in lexer messages](https://github.com/rust-lang/rust/pull/47914), fixed [ICE on const eval of union field](https://github.com/rust-lang/rust/pull/47794) and avoided [underflow in render_source_line](https://github.com/rust-lang/rust/pull/47677).
* [@euclio](https://github.com/euclio) used [correct casing for rename suggestions](https://github.com/rust-lang/rust/pull/47838).
* [@frewsxcv](https://github.com/frewsxcv) documented [that `Index` ops can panic on `HashMap` & `BTreeMap`](https://github.com/rust-lang/rust/pull/47839).
* [@ollie27](https://github.com/ollie27) fixed [link title rendering with hoedown in rustdoc](https://github.com/rust-lang/rust/pull/47855).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [ugly hover in sidebar](https://github.com/rust-lang/rust/pull/47951) and updated [associated constants error message](https://github.com/rust-lang/rust/pull/47876).

# Meetings

Next meeting will be on Tuesday 6th of February 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
