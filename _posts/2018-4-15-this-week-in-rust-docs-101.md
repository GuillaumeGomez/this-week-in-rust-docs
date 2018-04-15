---
layout: post
title: This Week in Rust Docs 101
date: 2018-4-15
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

A(n) (super ultra giga incredibly) old issue has now a [fix PR](https://github.com/rust-lang/rust/pull/49954): https://github.com/rust-lang/rust/issues/18167

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) moved [the "important traits" button to beside the type in rustdoc](https://github.com/rust-lang/rust/pull/49286) and ported [the -C option from rustc into rustdoc](https://github.com/rust-lang/rust/pull/49956).
* [@klnusbaum](https://github.com/klnusbaum) provided [better borrow checker error message](https://github.com/rust-lang/rust/pull/48708).
* [@PramodBisht](https://github.com/PramodBisht) fixed [doc comments present after a particular syntax error cause an unhelpful error message to be output](https://github.com/rust-lang/rust/pull/48946).
* [@zackmdavis](https://github.com/zackmdavis) pointed [to value in "value assigned is never read" lint](https://github.com/rust-lang/rust/pull/49197).
* [@SimonSapin](https://github.com/SimonSapin) soft-deprecated [the description() method of the Error trait](https://github.com/rust-lang/rust/pull/49536).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.26.0](https://github.com/rust-lang/rust/pull/49523).
* [@sgrif](https://github.com/sgrif) removed [the "leak check" in favor of "universes"](https://github.com/rust-lang/rust/pull/48407).
* [@ecstatic-morse](https://github.com/ecstatic-morse) rewrote [docs for `std::ptr`](https://github.com/rust-lang/rust/pull/49767) and added [doc links to `std::os` extension traits](https://github.com/rust-lang/rust/pull/49829).
* [@steveklabnik](https://github.com/steveklabnik) added ["the Rustc book"](https://github.com/rust-lang/rust/pull/49707).
* [@da-x](https://github.com/da-x) included [scope names in diagnostics](https://github.com/rust-lang/rust/pull/49898).
* [@csmoe](https://github.com/csmoe) fixed [incorrect span in `&mut` suggestion](https://github.com/rust-lang/rust/pull/49931).
* [@Phlosioneer](https://github.com/Phlosioneer) clarified [the difference between get_mut and into_mut for OccupiedEntry](https://github.com/rust-lang/rust/pull/49743).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [repeat method on slice](https://github.com/rust-lang/rust/pull/48999), stabilized [short error format](https://github.com/rust-lang/rust/pull/49546), added [warning if a resolution failed](https://github.com/rust-lang/rust/pull/49542), added [specific never search](https://github.com/rust-lang/rust/pull/49757), added [multiple query search](https://github.com/rust-lang/rust/pull/49966), added [rustdoc settings menu](https://github.com/rust-lang/rust/pull/49954) and fix [example indent](https://github.com/rust-lang/rust/pull/49670).

# Recent doc contributions

* [@zackmdavis](https://github.com/zackmdavis) added [suggestion of `!` for erroneous identifier `not`](https://github.com/rust-lang/rust/pull/49258).
* [@ollie27](https://github.com/ollie27) added [docs for the test crate with the std docs](https://github.com/rust-lang/rust/pull/49465).
* [@gaurikholkar](https://github.com/gaurikholkar) modified [compile-fail/E0389 error message](https://github.com/rust-lang/rust/pull/48914).
* [@llogiq](https://github.com/llogiq) improved [Atomic::fetch_update docs](https://github.com/rust-lang/rust/pull/49916) and added [note for the special type inference handling for shift ops](https://github.com/rust-lang/rust/pull/49915).
* [@memoryleak47](https://github.com/memoryleak47) fixed [typo](https://github.com/rust-lang/rust/pull/49863).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [error codes for libsyntax_ext](https://github.com/rust-lang/rust/pull/48173) and added [page to list all crate's items](https://github.com/rust-lang/rust/pull/49504).

# Meetings

Next meeting will be on Tuesday 17th of April 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
