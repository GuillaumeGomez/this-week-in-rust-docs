---
layout: post
title: This Week in Rust Docs 23
date: 2016-09-25
---

Hello and welcome to *This Week in Rust Docs*!

*This Week in Rust Docs* is openly developed [on GitHub](https://github.com/GuillaumeGomez/this-week-in-rust-docs).
If you find any errors in this week's issue, [please submit a PR](https://github.com/GuillaumeGomez/this-week-in-rust-docs/pulls).

And of course, don't forget to look at the docs:

* [Stable](https://doc.rust-lang.org/)
* [Beta](http://doc.rust-lang.org/beta/)
* [Nightly](http://doc.rust-lang.org/nightly/)

This week's edition was edited by [Guillaume Gomez](https://github.com/GuillaumeGomez).

# Latest news

The ["new" run button](https://github.com/rust-lang/rust/pull/36334) has been merged and is now used in [nightly docs](https://doc.rust-lang.org/nightly/std/). Give it a try!

Please take a look [to the next rust doc days planning reminder](https://users.rust-lang.org/t/reminder-planning-the-next-rust-doc-days/6901).

The topic to propose crates for the Rust Doc Days is still open and waiting for contributions [here](https://users.rust-lang.org/t/call-for-proposals-for-next-rust-doc-days-crates/6685). Please take a look!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [Error code list which need to be updated to new format](https://github.com/rust-lang/rust/issues/35233)
* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on GitHub!

# Call for participation

There's now a call for participation to [display all methods of a type, even those from implicit traits in rustdoc](https://github.com/rust-lang/rust/issues/33772). This is a great way to help users find everything that a type can do. Any help on it would be very appreciated!

# Waiting for merge

* [@bluss](https://github.com/bluss) updated rustdoc's CSS [to put `where` in trait listings on a new line](https://github.com/rust-lang/rust/pull/36676).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) updated rustdoc [to print non-self arguments of bare functions and struct methods on their own line](https://github.com/rust-lang/rust/pull/36679).
* [@pmatos](https://github.com/pmatos) improved [documention troubleshooting missing linker](https://github.com/rust-lang/rust/pull/36672).
* [@kmcallister](https://github.com/kmcallister) updated [Arc docs to match new Rc docs](https://github.com/rust-lang/rust/pull/36665).
* [@japaric](https://github.com/japaric) implemented [--sysroot on rustdoc](https://github.com/rust-lang/rust/pull/36586).
* [@liigo](https://github.com/liigo) updated rustdoc to [inline sidebar items, to display more in a page](https://github.com/rust-lang/rust/pull/36644).
* [@giannicic](https://github.com/giannicic) fixed [E0520 error message](https://github.com/rust-lang/rust/pull/36652).
* [@sinkuu](https://github.com/sinkuu) made [E0243/E0244 message consistent with E0107](https://github.com/rust-lang/rust/pull/36615).
* [@vanjacosic](https://github.com/vanjacosic) updated [the "Ownership" section of The Book](https://github.com/rust-lang/rust/pull/36564) and updated [the "Getting started" section of The Book](https://github.com/rust-lang/rust/pull/36563).
* [@christopherdumas](https://github.com/christopherdumas) updated [`includes!` documentation](https://github.com/rust-lang/rust/pull/36404).
* [@EdorianDark](https://github.com/EdorianDark) inserted [examples with universal function call syntax](https://github.com/rust-lang/rust/pull/36248).
* [@matthew-piziak](https://github.com/matthew-piziak) added [links to interesting items in `std::ptr` documentation](https://github.com/rust-lang/rust/pull/35880), [refactored range examples](https://github.com/rust-lang/rust/pull/35759) and added [`default` docstrings for `String`, `AtomicBool`, and `Generics`](https://github.com/rust-lang/rust/pull/36364).
* [@steveklabnik](https://github.com/steveklabnik) made it clear that [reference isn't normative](https://github.com/rust-lang/rust/pull/35102).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) updated [doc comments to new macro url syntax](https://github.com/rust-lang/rust/pull/36535), fixed [run button appearing when it shouldn't](https://github.com/rust-lang/rust/pull/36637), fixed [some typos and improve doc comments style](https://github.com/rust-lang/rust/pull/36623), added [missing urls for Box doc](https://github.com/rust-lang/rust/pull/36576), added [information in case of markdown block code test failure](https://github.com/rust-lang/rust/pull/36320) and fixed [formatting generation for rustdoc code examples](https://github.com/rust-lang/rust/pull/35012).

# Recent doc contributions

* [@kmcallister](https://github.com/kmcallister) tweaked [std::rc docs](https://github.com/rust-lang/rust/pull/36571).
* [@caipre](https://github.com/caipre) made [a minor correction in `sort_by_key` doc comment](https://github.com/rust-lang/rust/pull/36600).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) fixed [language in documentation comment](https://github.com/rust-lang/rust/pull/36521), added [example in AsMut trait documentation](https://github.com/rust-lang/rust/pull/36519) and added links between format_args! macro and std::fmt::Arguments struct](https://github.com/rust-lang/rust/pull/36523).
* [@frewsxcv](https://github.com/frewsxcv) added [basic doc examples for `std::panic::{set_hook, take_hook}`](https://github.com/rust-lang/rust/pull/36390) and made [a minor `VecDeque` doc examples cleanup](https://github.com/rust-lang/rust/pull/36664).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) proposed [a global rust-lang.org architecture change](https://github.com/rust-lang/rust-www/pull/533), replaced ['e.g.' by 'i.e.'](https://github.com/rust-lang/rust/pull/36578) and added [metadata diagnostics](https://github.com/rust-lang/rust/pull/36102).

# Meetings

Next meeting will be on Wednesday 28th of September 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
