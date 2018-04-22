---
layout: post
title: This Week in Rust Docs 102
date: 2018-4-22
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

We added [settings into generated documentation](ttps://github.com/rust-lang/rust/pull/49954) so you can have your own setup. We'll add more options soon to make rust documentation browsing more personal and comfortable for everyone!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) moved [the "important traits" button to beside the type in rustdoc](https://github.com/rust-lang/rust/pull/49286).
* [@klnusbaum](https://github.com/klnusbaum) provided [better borrow checker error message](https://github.com/rust-lang/rust/pull/48708).
* [@PramodBisht](https://github.com/PramodBisht) fixed [doc comments present after a particular syntax error cause an unhelpful error message to be output](https://github.com/rust-lang/rust/pull/48946).
* [@zackmdavis](https://github.com/zackmdavis) pointed [to value in "value assigned is never read" lint](https://github.com/rust-lang/rust/pull/49197).
* [@sgrif](https://github.com/sgrif) removed [the "leak check" in favor of "universes"](https://github.com/rust-lang/rust/pull/48407).
* [@ecstatic-morse](https://github.com/ecstatic-morse) rewrote [docs for `std::ptr`](https://github.com/rust-lang/rust/pull/49767) and added [doc links to `std::os` extension traits](https://github.com/rust-lang/rust/pull/49829).
* [@steveklabnik](https://github.com/steveklabnik) added ["the Rustc book"](https://github.com/rust-lang/rust/pull/49707).
* [@da-x](https://github.com/da-x) included [scope names in diagnostics](https://github.com/rust-lang/rust/pull/49898).
* [@Phlosioneer](https://github.com/Phlosioneer) clarified [the difference between get_mut and into_mut for OccupiedEntry](https://github.com/rust-lang/rust/pull/49743).
* [@ibabushkin](https://github.com/ibabushkin) refactored [auto trait handling in librustdoc to be accessible from librustc](https://github.com/rust-lang/rust/pull/49711).
* [@mattico](https://github.com/mattico) updated [mdbook](https://github.com/rust-lang/rust/pull/50147).
* [@andjo403](https://github.com/andjo403) made [rustdoc tests follow the jobserver limit of threads](https://github.com/rust-lang/rust/pull/50134).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [repeat method on slice](https://github.com/rust-lang/rust/pull/48999), stabilized [short error format](https://github.com/rust-lang/rust/pull/49546), added [rustdoc settings menu](https://github.com/rust-lang/rust/pull/49954) and fixed [search bar bug](https://github.com/rust-lang/rust/pull/50118).

# Recent doc contributions

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) ported [the -C option from rustc into rustdoc](https://github.com/rust-lang/rust/pull/49956).
* [@csmoe](https://github.com/csmoe) fixed [incorrect span in `&mut` suggestion](https://github.com/rust-lang/rust/pull/49931).
* [@krk](https://github.com/krk) clarified [E0015 message](https://github.com/rust-lang/rust/pull/50031).
* [@varkor](https://github.com/varkor) added [rustdoc to x.py check](https://github.com/rust-lang/rust/pull/50062).
* [@Zoxc](https://github.com/Zoxc) improved [query cycle error message](https://github.com/rust-lang/rust/pull/49950).
* [@ollie27](https://github.com/ollie27) removed [private paths in all.html in rustdoc](https://github.com/rust-lang/rust/pull/50032).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warning if a resolution failed](https://github.com/rust-lang/rust/pull/49542), added [specific never search](https://github.com/rust-lang/rust/pull/49757) and added [multiple query search](https://github.com/rust-lang/rust/pull/49966).

# Meetings

Next meeting will be on Tuesday 24th of April 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
