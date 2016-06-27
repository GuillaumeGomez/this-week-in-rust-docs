---
layout: post
title: This Week in Rust Docs 10
date: 2016-06-27
---

Hello and welcome to *This Week in Rust Docs*!

*This Week in Rust Docs* is openly developed [on GitHub](https://github.com/GuillaumeGomez/this-week-in-rust-docs).
If you find any errors in this week's issue, [please submit a PR](https://github.com/GuillaumeGomez/this-week-in-rust-docs/pulls).

And of course, don't forget to look at the docs:

* [Stable](https://doc.rust-lang.org/)
* [Beta](http://doc.rust-lang.org/beta/)
* [Nightly](http://doc.rust-lang.org/nightly/)

This week's edition was edited by: [GuillaumeGomez](https://github.com/GuillaumeGomez).

# Latest news

The "doc days" event is now over. Thanks to everyone who contributed! Here is a list of the contributions:

* [tempdir](https://github.com/rust-lang-nursery/tempdir/pull/11)
* [unix-socket](https://github.com/rust-lang-nursery/unix-socket/pull/26)
* [uuid (1)](https://github.com/rust-lang-nursery/uuid/pull/65) and [uuid (2)](https://github.com/rust-lang-nursery/uuid/pull/64)
* [glob](https://github.com/rust-lang-nursery/glob/pull/53)
* [rand](https://github.com/rust-lang-nursery/rand/pull/106)
* [rustc-serialize](https://github.com/rust-lang-nursery/rustc-serialize/pull/153)

# Current opened issues

For now, here are the two big issues opened for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They both need help to move forward so any contribution is very welcome!

There are currently around 50 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on github!

# Call for participation

There's now a call for participation to [display all methods of a type, even those from implicit traits](https://github.com/rust-lang/rust/issues/33772). This is a great way to help users find everything that a type can do. Any help on it would be very appreciated!

# Waiting for merge

* [@tatsuya6502](https://github.com/tatsuya6502) fixed [links in Ownership section of the book](https://github.com/rust-lang/rust/pull/34442).
* [@ubsan](https://github.com/ubsan) fixed [ABI string docs in reference.md](https://github.com/rust-lang/rust/pull/34461).
* [@dns2utf8](https://github.com/dns2utf8) added [example with leading zeros](https://github.com/rust-lang/rust/pull/34462).
* [@frewsxcv](https://github.com/frewsxcv) expanded [`std::path::Component` documentation](https://github.com/rust-lang/rust/pull/34475) and added [example for `std::thread::sleep`](https://github.com/rust-lang/rust/pull/34406).
* [@estebank](https://github.com/estebank) added [specific error message for missplaced doc comments](https://github.com/rust-lang/rust/pull/33922).
* [@ollie27](https://github.com/ollie27) fixed [inlined renamed reexports in import lists](https://github.com/rust-lang/rust/pull/34479), fixed [float examples](https://github.com/rust-lang/rust/pull/34415), fixed [search result layout for enum variants and struct fields](https://github.com/rust-lang/rust/pull/34477) and removed [Remove Derived Implementations title](https://github.com/rust-lang/rust/pull/34105).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [E0269 explanation](https://github.com/rust-lang/rust/pull/34471) and added [new error codes and improve some explanations](https://github.com/rust-lang/rust/pull/34467).

# Recent doc contributions

* [@frewsxcv](https://github.com/frewsxcv) indicated [how the `std::path::Components` struct is created](https://github.com/rust-lang/rust/pull/34469), indicated [how the `JoinHandle` struct is created](https://github.com/rust-lang/rust/pull/34438), fixed [doc parameters formatting](https://github.com/rust-lang/rust/pull/34410), added [doc example for `std::thread::Builder::name`](https://github.com/rust-lang/rust/pull/34465) and added [hyperlinks to `std::fs` functions from `std::path`](https://github.com/rust-lang/rust/pull/34468).
* [@liigo](https://github.com/liigo) updated [rustc-ux-guidelines](https://github.com/rust-lang/rust/pull/34378) and improved [E0425 explanation](https://github.com/rust-lang/rust/pull/34379).
* [@cynicaldevil](https://github.com/cynicaldevil) modified E0220 [to show error messages for more general cases](https://github.com/rust-lang/rust/pull/34364).
* [@ollie27](https://github.com/ollie27) added [more types to the rustdoc sidebar](https://github.com/rust-lang/rust/pull/34372), fixed [panic caused by doc(hidden) trait methods](https://github.com/rust-lang/rust/pull/34439) and fixed [a couple of issues with src links to external crates](https://github.com/rust-lang/rust/pull/34387).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [error code flags](https://github.com/rust-lang/rust/pull/34401).

# Meetings

Next meeting will be on Wednesday 29th of June 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
