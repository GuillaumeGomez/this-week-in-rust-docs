---
layout: post
title: This Week in Rust Docs 24
date: 2016-10-02
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

* [@frewsxcv](https://github.com/frewsxcv) made a ["minor" librustdoc cleanup and refactoring](https://github.com/rust-lang/rust/pull/36903).
* [@BlueSpaceCanary](https://github.com/BlueSpaceCanary) removed [the double introduction for `cargo run`](https://github.com/rust-lang/rust/pull/36878).
* [@gavinb](https://github.com/gavinb) improved [error message and snippet for "did you mean `x`"](https://github.com/rust-lang/rust/pull/36798).
* [@green-coder](https://github.com/green-coder) updated [example code in the documentation](https://github.com/rust-lang/rust/pull/36746).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) updated rustdoc [to print non-self arguments of bare functions and struct methods on their own line](https://github.com/rust-lang/rust/pull/36679).
* [@kmcallister](https://github.com/kmcallister) updated [Arc docs to match new Rc docs](https://github.com/rust-lang/rust/pull/36665).
* [@liigo](https://github.com/liigo) updated rustdoc to [inline sidebar items, to display more in a page](https://github.com/rust-lang/rust/pull/36644).
* [@sinkuu](https://github.com/sinkuu) made [E0243/E0244 message consistent with E0107](https://github.com/rust-lang/rust/pull/36615).
* [@christopherdumas](https://github.com/christopherdumas) updated [`includes!` documentation](https://github.com/rust-lang/rust/pull/36404).
* [@matthew-piziak](https://github.com/matthew-piziak) added [links to interesting items in `std::ptr` documentation](https://github.com/rust-lang/rust/pull/35880), [refactored range examples](https://github.com/rust-lang/rust/pull/35759) and added [`default` docstrings for `String`, `AtomicBool`, and `Generics`](https://github.com/rust-lang/rust/pull/36364).
* [@steveklabnik](https://github.com/steveklabnik) made it clear that [reference isn't normative](https://github.com/rust-lang/rust/pull/35102).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [run button appearing when it shouldn't](https://github.com/rust-lang/rust/pull/36637), added [information in case of markdown block code test failure](https://github.com/rust-lang/rust/pull/36320) and fixed [formatting generation for rustdoc code examples](https://github.com/rust-lang/rust/pull/35012).

# Recent doc contributions

* [@alygin](https://github.com/alygin) updated [E0512 to new error format](https://github.com/rust-lang/rust/pull/36756).
* [@KiChjang](https://github.com/KiChjang) updated [E0025 to new error format](https://github.com/rust-lang/rust/pull/36757).
* [@nathanmusoke](https://github.com/nathanmusoke) fixed [minor typo in variable bindings in The Book](https://github.com/rust-lang/rust/pull/36769).
* [@palango](https://github.com/palango) added [link to format! docs](https://github.com/rust-lang/rust/pull/36813).
* [@wesleywiser](https://github.com/wesleywiser) made [`Send` and `Sync` traits to the reference](https://github.com/rust-lang/rust/pull/36860).
* [@tmiasko](https://github.com/tmiasko) fixed [BufRead::read_until documentation](https://github.com/rust-lang/rust/pull/36851) and reworded [description of SystemTimeError](https://github.com/rust-lang/rust/pull/36833).
* [@frewsxcv](https://github.com/frewsxcv) made [a couple refactorings in librustdoc](https://github.com/rust-lang/rust/pull/36872) and added [basic doc example for `core::ptr::write_bytes`](https://github.com/rust-lang/rust/pull/36765).
* [@bluss](https://github.com/bluss) updated rustdoc's CSS [to put `where` in trait listings on a new line](https://github.com/rust-lang/rust/pull/36676).
* [@japaric](https://github.com/japaric) implemented [--sysroot on rustdoc](https://github.com/rust-lang/rust/pull/36586).
* [@giannicic](https://github.com/giannicic) fixed [E0520 error message](https://github.com/rust-lang/rust/pull/36652).
* [@pmatos](https://github.com/pmatos) improved [documention troubleshooting missing linker](https://github.com/rust-lang/rust/pull/36672).
* [@vanjacosic](https://github.com/vanjacosic) updated [the "Ownership" section of The Book](https://github.com/rust-lang/rust/pull/36564) and updated [the "Getting started" section of The Book](https://github.com/rust-lang/rust/pull/36563).
* [@jonathandturner](https://github.com/jonathandturner) updated [E0425, E0446 and E0449](https://github.com/rust-lang/rust/pull/36761).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) updated [doc comments to new macro url syntax](https://github.com/rust-lang/rust/pull/36535), added [E0513 stuff](https://github.com/rust-lang/rust/pull/36723), updated [E0035, E0036 and E0370 to new error format](https://github.com/rust-lang/rust/pull/36873), improved [process module doc a bit](https://github.com/rust-lang/rust/pull/36841), added [missing urls for ops module](https://github.com/rust-lang/rust/pull/36810), added [missing links on cmp module](https://github.com/rust-lang/rust/pull/36750), fixed [some typos and improve doc comments style](https://github.com/rust-lang/rust/pull/36623) and added [missing urls for Box doc](https://github.com/rust-lang/rust/pull/36576).

# Meetings

Next meeting will be on Wednesday 5th of October 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
