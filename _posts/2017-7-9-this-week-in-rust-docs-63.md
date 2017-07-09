---
layout: post
title: This Week in Rust Docs 63
date: 2017-7-9
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

None.

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
* [@rthomas](https://github.com/rthomas) updated [docs on Error struct](https://github.com/rust-lang/rust/pull/42837).
* [@Fourchaux](https://github.com/Fourchaux) fixed [basic typos in Doc Comments](https://github.com/rust-lang/rust/pull/42812).
* [@dns2utf8](https://github.com/dns2utf8) added [hint about the return code of panic!](https://github.com/rust-lang/rust/pull/42670).
* [@Emilgardis](https://github.com/Emilgardis) fixed [wrong report on closure args mismatch when a ref is expected but not found](https://github.com/rust-lang/rust/pull/42270).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) refactored [pretty printing slightly](https://github.com/rust-lang/rust/pull/42897) and allowed [setting the limit on std::io::Take](https://github.com/rust-lang/rust/pull/42697).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings when rustdoc html rendering differs](https://github.com/rust-lang/rust/pull/41991), added [errors when doc comments are added where they're unused](https://github.com/rust-lang/rust/pull/43009), cleaned up [some code](https://github.com/rust-lang/rust/pull/43006) and add [spacing between trait functions](https://github.com/rust-lang/rust/pull/43130).

# Recent doc contributions

* [@rthomas](https://github.com/rthomas) updated [docs for Debug* structs](https://github.com/rust-lang/rust/pull/42836) and added [annotations to the resize fn](https://github.com/rust-lang/rust/pull/43093).
* [@cengizIO](https://github.com/cengizIO) added [pager support for `rustc --explain EXXXX`](https://github.com/rust-lang/rust/pull/42732).
* [@Boreeas](https://github.com/Boreeas) folded [E0612, E0613 into E0609](https://github.com/rust-lang/rust/pull/42996).
* [@estebank](https://github.com/estebank) added [`rustc_on_unimplemented` message to `std::ops::Try`](https://github.com/rust-lang/rust/pull/43001) and made [suggestion include the line number](https://github.com/rust-lang/rust/pull/42904).
* [@durka](https://github.com/durka) fixed [links for typeck diagnostics without tripping tidy](https://github.com/rust-lang/rust/pull/43075).
* [@arielb1](https://github.com/arielb1) reported [the total number of errors on compilation failure](https://github.com/rust-lang/rust/pull/43015).
* [@ollie27](https://github.com/ollie27) fixed [markdown tests being run twice](https://github.com/rust-lang/rust/pull/43068).
* [@stjepang](https://github.com/stjepang) made [a minor fix in docs for Vec](https://github.com/rust-lang/rust/pull/43050).
* [@andersk](https://github.com/andersk) documented [unintuitive argument order for Vec::dedup_by relation](https://github.com/rust-lang/rust/pull/43041).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [toggle wrappers not generated correctly in rustdoc](https://github.com/rust-lang/rust/pull/42972).

# Meetings

Next meeting will be on Wednesday 12th of July 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
