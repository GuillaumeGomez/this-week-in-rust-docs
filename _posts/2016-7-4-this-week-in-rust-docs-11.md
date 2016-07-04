---
layout: post
title: This Week in Rust Docs 11
date: 2016-07-04
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

In the last team meeting (renamed "schrodinger's doc meeting", thanks for the idea [@jonathandturner](https://github.com/jonathandturner)!), we mainly talked about The Rust Doc Days. The feedback is globally good but I'll let read the great [post](https://facility9.com/2016/07/rust-doc-days-follow-up/) that [@peschkaj](https://github.com/peschkaj) wrote about it.

# Current opened issues

For now, here are the two big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They both need help to move forward so any contribution is very welcome!

There are currently around 50 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on github!

# Call for participation

There's now a call for participation to [display all methods of a type, even those from implicit traits in rustdoc](https://github.com/rust-lang/rust/issues/33772). This is a great way to help users find everything that a type can do. Any help on it would be very appreciated!

# Waiting for merge

* [@sylvestre](https://github.com/sylvestre) fixed [typos](https://github.com/rust-lang/rust/pull/34626).
* [@jaredmanning](https://github.com/jaredmanning) fixed [spacing in for loop enumeration example](https://github.com/rust-lang/rust/pull/34625).
* [@Xmasreturns](https://github.com/Xmasreturns) updated [glossary.md](https://github.com/rust-lang/rust/pull/34602).
* [@frewsxcv](https://github.com/frewsxcv) fixed [broken markdown link in README](https://github.com/rust-lang/rust/pull/34619) and added [doc examples for `io::Error::from_raw_os_error`](https://github.com/rust-lang/rust/pull/34612).
* [@rdotdk](https://github.com/rdotdk) updated [cargo doc link](https://github.com/rust-lang/rust/pull/34615).
* [@Manishearth](https://github.com/Manishearth) clarified [UnsafeCell docs](https://github.com/rust-lang/rust/pull/34520).
* [@ubsan](https://github.com/ubsan) added [more docs to std::mem::transmute](https://github.com/rust-lang/rust/pull/34609), fixed [ABI string docs in reference.md](https://github.com/rust-lang/rust/pull/34461) and fixed [ABI string docs in reference.md](https://github.com/rust-lang/rust/pull/34461).
* [@estebank](https://github.com/estebank) added [specific error message for missplaced doc comments](https://github.com/rust-lang/rust/pull/33922).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [libsyntax error codes explanation](https://github.com/rust-lang/rust/pull/34637).

# Recent doc contributions

* [@jupp0r](https://github.com/jupp0r) improved [code example for try!](https://github.com/rust-lang/rust/pull/34540).
* [@jonmarkprice](https://github.com/jonmarkprice) made [small grammatical and stylistic edits to The Book](https://github.com/rust-lang/rust/pull/34532).
* [@tatsuya6502](https://github.com/tatsuya6502) fixed [links in Ownership section of the book](https://github.com/rust-lang/rust/pull/34442).
* [@dns2utf8](https://github.com/dns2utf8) added [example with leading zeros](https://github.com/rust-lang/rust/pull/34462).
* [@frewsxcv](https://github.com/frewsxcv) expanded [`std::path::Component` documentation](https://github.com/rust-lang/rust/pull/34475), added [doc example for `std::io::sink`](https://github.com/rust-lang/rust/pull/34524), added [doc example for `std::io::repeat`](https://github.com/rust-lang/rust/pull/34518), made [a minor rewrite of `std::io::empty` doc example](https://github.com/rust-lang/rust/pull/34517) and added [example for `std::thread::sleep`](https://github.com/rust-lang/rust/pull/34406).
* [@ollie27](https://github.com/ollie27) fixed [inlined renamed reexports in import lists](https://github.com/rust-lang/rust/pull/34479), fixed [a few stripping issues in rustdoc](https://github.com/rust-lang/rust/pull/34513), fixed [float examples](https://github.com/rust-lang/rust/pull/34415), fixed [search result layout for enum variants and struct fields](https://github.com/rust-lang/rust/pull/34477), fixed [empty Implementations section on some module pages in rustdoc](https://github.com/rust-lang/rust/pull/34536) and removed [Remove Derived Implementations title](https://github.com/rust-lang/rust/pull/34105).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [E0269 explanation](https://github.com/rust-lang/rust/pull/34471), added [error codes in libsyntax](https://github.com/rust-lang/rust/pull/34531) and added [new error codes and improve some explanations](https://github.com/rust-lang/rust/pull/34467).

# Meetings

Next meeting will be on Wednesday 6th of July 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
