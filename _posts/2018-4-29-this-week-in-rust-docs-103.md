---
layout: post
title: This Week in Rust Docs 103
date: 2018-4-29
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

We added [settings into generated documentation](https://github.com/rust-lang/rust/pull/49954) so you can have your own setup. We'll add more options soon to make rust documentation browsing more personal and comfortable for everyone!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) moved [the "important traits" button to beside the type in rustdoc](https://github.com/rust-lang/rust/pull/49286).
* [@sgrif](https://github.com/sgrif) removed [the "leak check" in favor of "universes"](https://github.com/rust-lang/rust/pull/48407).
* [@ecstatic-morse](https://github.com/ecstatic-morse) rewrote [docs for `std::ptr`](https://github.com/rust-lang/rust/pull/49767).
* [@da-x](https://github.com/da-x) included [scope names in diagnostics](https://github.com/rust-lang/rust/pull/49898).
* [@Phlosioneer](https://github.com/Phlosioneer) clarified [the difference between get_mut and into_mut for OccupiedEntry](https://github.com/rust-lang/rust/pull/49743).
* [@ibabushkin](https://github.com/ibabushkin) refactored [auto trait handling in librustdoc to be accessible from librustc](https://github.com/rust-lang/rust/pull/49711).
* [@Manishearth](https://github.com/Manishearth) added [edition-gated keywords](https://github.com/rust-lang/rust/pull/49611) and used [enum for approximate suggestions](https://github.com/rust-lang/rust/pull/50204).
* [@z4v1er](https://github.com/z4v1er) fixed [typo](https://github.com/rust-lang/rust/pull/50217).
* [@rizakrko](https://github.com/rizakrko) added [missing implementation hint](https://github.com/rust-lang/rust/pull/50161).
* [@mulkieran](https://github.com/mulkieran) made [some documentation fixes for the Write trait](https://github.com/rust-lang/rust/pull/50255).
* [@kornelski](https://github.com/kornelski) buried [Error::description()](https://github.com/rust-lang/rust/pull/50163).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) stabilized [short error format](https://github.com/rust-lang/rust/pull/49546), prevented [infinite recursion of modules in rustdoc](https://github.com/rust-lang/rust/pull/50305), added [query search order check](https://github.com/rust-lang/rust/pull/50302) and made [some rustdoc improvements](https://github.com/rust-lang/rust/pull/50259).

# Recent doc contributions

* [@PramodBisht](https://github.com/PramodBisht) fixed [doc comments present after a particular syntax error cause an unhelpful error message to be output](https://github.com/rust-lang/rust/pull/48946).
* [@ecstatic-morse](https://github.com/ecstatic-morse) added [doc links to `std::os` extension traits](https://github.com/rust-lang/rust/pull/49829).
* [@steveklabnik](https://github.com/steveklabnik) added ["the Rustc book"](https://github.com/rust-lang/rust/pull/49707).
* [@andjo403](https://github.com/andjo403) made [rustdoc tests follow the jobserver limit of threads](https://github.com/rust-lang/rust/pull/50134).
* [@dmizuk](https://github.com/dmizuk) marked [`ptr::Unique` with `#[doc(hidden)]`](https://github.com/rust-lang/rust/pull/49858).
* [@ralfbiedert](https://github.com/ralfbiedert) added [missing `.` in docs](https://github.com/rust-lang/rust/pull/50219).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [repeat method on slice](https://github.com/rust-lang/rust/pull/48999), added [rustdoc settings menu](https://github.com/rust-lang/rust/pull/49954), fixed [search bar bug](https://github.com/rust-lang/rust/pull/50118), fixed [search load page failure](https://github.com/rust-lang/rust/pull/50284), added [setting to go to item if there is only one result](https://github.com/rust-lang/rust/pull/50229), added [more doc aliases](https://github.com/rust-lang/rust/pull/50231) and made [js improvements](https://github.com/rust-lang/rust/pull/50214).

# Meetings

Next meeting will be on Tuesday 1st of May 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
