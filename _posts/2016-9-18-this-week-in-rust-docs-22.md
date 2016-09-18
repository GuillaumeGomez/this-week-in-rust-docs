---
layout: post
title: This Week in Rust Docs 22
date: 2016-09-18
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

* [@christopherdumas](https://github.com/christopherdumas) updated [`includes!` documentation](https://github.com/rust-lang/rust/pull/36404).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) links between format_args! macro and std::fmt::Arguments struct](https://github.com/rust-lang/rust/pull/36523).
* [@EdorianDark](https://github.com/EdorianDark) inserted [examples with universal function call syntax](https://github.com/rust-lang/rust/pull/36248).
* [@frewsxcv](https://github.com/frewsxcv) added [basic doc examples for `std::panic::{set_hook, take_hook}`](https://github.com/rust-lang/rust/pull/36390) and added [basic doc example for `std::panic::set_hook`](https://github.com/rust-lang/rust/pull/36390).
* [@matthew-piziak](https://github.com/matthew-piziak) added [links to interesting items in `std::ptr` documentation](https://github.com/rust-lang/rust/pull/35880), [refactored range examples](https://github.com/rust-lang/rust/pull/35759) and added [`default` docstrings for `String`, `AtomicBool`, and `Generics`](https://github.com/rust-lang/rust/pull/36364).
* [@steveklabnik](https://github.com/steveklabnik) made it clear that [reference isn't normative](https://github.com/rust-lang/rust/pull/35102).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [information in case of markdown block code test failure](https://github.com/rust-lang/rust/pull/36320), added [metadata diagnostics](https://github.com/rust-lang/rust/pull/36102), fixed [formatting generation for rustdoc code examples](https://github.com/rust-lang/rust/pull/35012).

# Recent doc contributions

This week (too), I'll split between the [new error code format](https://github.com/rust-lang/rust/issues/35233) contributions and the others. Let's start by the first one:

* [@jfirebaugh](https://github.com/jfirebaugh): [E0297](https://github.com/rust-lang/rust/pull/36389)
* [@GuillaumeGomez](https://github.com/GuillaumeGomez): [E0049](https://github.com/rust-lang/rust/pull/36383)
* [@mikhail-m1](https://github.com/mikhail-m1): [E0537, E0535 and E0536](https://github.com/rust-lang/rust/pull/36354)

Other contributions:

* [@kmcallister](https://github.com/kmcallister) tweaked [std::mem docs](https://github.com/rust-lang/rust/pull/36357), tweaked [array docs](https://github.com/rust-lang/rust/pull/36402) qnd tweaked [std::marker docs](https://github.com/rust-lang/rust/pull/36424).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) fixed [language in documentation comment](https://github.com/rust-lang/rust/pull/36521), added [example in AsMut trait documentation](https://github.com/rust-lang/rust/pull/36519).
* [@kylog](https://github.com/kylog) fixed [a typo in The Book](https://github.com/rust-lang/rust/pull/36380).
* [@tshepang](https://github.com/tshepang) improved [wording](https://github.com/rust-lang/rust/pull/36480).
* [@athulappadan](https://github.com/athulappadan) added [Documentation about what Default does for each type](https://github.com/rust-lang/rust/pull/36396).
* [@liigo](https://github.com/liigo) removed [the `docblock-short` collapse](https://github.com/rust-lang/rust/pull/36293).
* [@kylog](https://github.com/kylog) fixed [a typo in The Book](https://github.com/rust-lang/rust/pull/36380).
* [@dangcheng](https://github.com/dangcheng) fixed [a mistake (File::open -> File::create) in The Book](https://github.com/rust-lang/rust/pull/36374).
* [@c4rlo](https://github.com/c4rlo) fixed [a "\\" in a table heading to be "/"](https://github.com/rust-lang/rust/pull/36204).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [urls when they were needed](https://github.com/rust-lang/rust/pull/36363) and set [run button transparent instead of invisible](https://github.com/rust-lang/rust/pull/36334).

# Meetings

Next meeting will be on Wednesday 21st of September 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
