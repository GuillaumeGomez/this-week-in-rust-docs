---
layout: post
title: This Week in Rust Docs 12
date: 2016-07-11
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

In the last team meeting, we decided that the [RFC "More api documentation conventions"](https://github.com/rust-lang/rfcs/pull/1574) was ready to get merged. We now wait for the core team confirmation.

# Current opened issues

For now, here are the two big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They both need help to move forward so any contribution is very welcome!

There are currently around 50 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on github!

# Call for participation

There's now a call for participation to [display all methods of a type, even those from implicit traits in rustdoc](https://github.com/rust-lang/rust/issues/33772). This is a great way to help users find everything that a type can do. Any help on it would be very appreciated!

# Waiting for merge

* [@Manishearth](https://github.com/Manishearth) clarified [UnsafeCell docs](https://github.com/rust-lang/rust/pull/34520).
* [@estebank](https://github.com/estebank) added [specific error message for missplaced doc comments](https://github.com/rust-lang/rust/pull/33922).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [libsyntax error codes explanation](https://github.com/rust-lang/rust/pull/34637).

# Recent doc contributions

* [@alexandermerritt](https://github.com/alexandermerritt) made [docs for clone_from_slice consistent with copy_from_slice](https://github.com/rust-lang/rust/pull/34745).
* [@ubsan](https://github.com/ubsan) added [more docs to std::mem::transmute](https://github.com/rust-lang/rust/pull/34609), fixed [ABI string docs in reference.md](https://github.com/rust-lang/rust/pull/34461) and fixed [ABI string docs in reference.md](https://github.com/rust-lang/rust/pull/34461).
* [@rdotdk](https://github.com/rdotdk) updated [cargo doc link](https://github.com/rust-lang/rust/pull/34615).
* [@frewsxcv](https://github.com/frewsxcv) fixed [broken markdown link in README](https://github.com/rust-lang/rust/pull/34619), improved [primitive integers documentation](https://github.com/rust-lang/rust/pull/34709), fixed [unnecessarily mutable reference in doc example](https://github.com/rust-lang/rust/pull/34717) and added [doc examples for `io::Error::from_raw_os_error`](https://github.com/rust-lang/rust/pull/34612).
* [@Xmasreturns](https://github.com/Xmasreturns) updated [glossary.md](https://github.com/rust-lang/rust/pull/34602).
* [@jaredmanning](https://github.com/jaredmanning) fixed [spacing in for loop enumeration example](https://github.com/rust-lang/rust/pull/34625).
* [@sylvestre](https://github.com/sylvestre) fixed [typos](https://github.com/rust-lang/rust/pull/34626).
* [@durka](https://github.com/durka) documented [DoubleEndedIterator::next_back](https://github.com/rust-lang/rust/pull/34732).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez), added [examples for std::Error module](https://github.com/rust-lang/rust/pull/34750), improved [std::any module doc](https://github.com/rust-lang/rust/pull/34749), added [missing examples for std::cell types](https://github.com/rust-lang/rust/pull/34736), removed [invalid CSS rule for doc titles](https://github.com/rust-lang/rust/pull/34685), improved [boxed docs](https://github.com/rust-lang/rust/pull/34740), improved [slice docs](https://github.com/rust-lang/rust/pull/34725). fixed [`std::path::Path::file_name()` doc](https://github.com/rust-lang/rust/pull/34659), removed [useless doc comment for slice](https://github.com/rust-lang/rust/pull/34723) and improved [DoubleEndedIterator examples](https://github.com/rust-lang/rust/pull/34688).

# Meetings

Next meeting will be on Wednesday 13th of July 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
