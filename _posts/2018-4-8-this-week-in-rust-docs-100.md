---
layout: post
title: This Week in Rust Docs 100
date: 2018-4-8
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

🎉 It's the hundredth post! 🎉

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
* [@zackmdavis](https://github.com/zackmdavis) added [suggestion of `!` for erroneous identifier `not`](https://github.com/rust-lang/rust/pull/49258) and pointed [to value in "value assigned is never read" lint](https://github.com/rust-lang/rust/pull/49197).
* [@SimonSapin](https://github.com/SimonSapin) soft-deprecated [the description() method of the Error trait](https://github.com/rust-lang/rust/pull/49536).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.26.0](https://github.com/rust-lang/rust/pull/49523).
* [@sgrif](https://github.com/sgrif) removed [the "leak check" in favor of "universes"](https://github.com/rust-lang/rust/pull/48407).
* [@ollie27](https://github.com/ollie27) added [docs for the test crate with the std docs](https://github.com/rust-lang/rust/pull/49465).
* [@ecstatic-morse](https://github.com/ecstatic-morse) rewrote [docs for `std::ptr`](https://github.com/rust-lang/rust/pull/49767).
* [@gaurikholkar](https://github.com/gaurikholkar) modified [compile-fail/E0389 error message](https://github.com/rust-lang/rust/pull/48914).
* [@steveklabnik](https://github.com/steveklabnik) added ["the Rustc book"](https://github.com/rust-lang/rust/pull/49707).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [error codes for libsyntax_ext](https://github.com/rust-lang/rust/pull/48173), added [repeat method on slice](https://github.com/rust-lang/rust/pull/48999), stabilized [short error format](https://github.com/rust-lang/rust/pull/49546), added [page to list all crate's items](https://github.com/rust-lang/rust/pull/49504), added [warning if a resolution failed](https://github.com/rust-lang/rust/pull/49542) and added [specific never search](https://github.com/rust-lang/rust/pull/49757).

# Recent doc contributions

* [@FraGag](https://github.com/FraGag) improved [documentation of Clone and Copy implementors](https://github.com/rust-lang/rust/pull/48171).
* [@tinaun](https://github.com/tinaun) removed [erroneous error message when checking impl trait params](https://github.com/rust-lang/rust/pull/48709).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) suppressed [the default allow(unused) under --display-warnings in rustdoctest](https://github.com/rust-lang/rust/pull/49064) and added [an --edition flag to compile docs/doctests with a certain edition in rustdoc](https://github.com/rust-lang/rust/pull/49451).
* [@frewsxcv](https://github.com/frewsxcv) clarified [network byte order conversions for integer / IP address conversions](https://github.com/rust-lang/rust/pull/49418).
* [@Phlosioneer](https://github.com/Phlosioneer) added [test for rustdoc ignore test](https://github.com/rust-lang/rust/pull/49532) and fixed [escaped backslash in windows file not found message](https://github.com/rust-lang/rust/pull/49478).
* [@steveklabnik](https://github.com/steveklabnik) updated [mdbook](https://github.com/rust-lang/rust/pull/49623) and re-wrote [the documentation index](https://github.com/rust-lang/rust/pull/49628).
* [@rolfvandekrol](https://github.com/rolfvandekrol) fixed [typo](https://github.com/rust-lang/rust/pull/49599).
* [@mbrubeck](https://github.com/mbrubeck) added [some performance guidance to std::fs and std::io docs](https://github.com/rust-lang/rust/pull/49594).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) removed [unneeded trait implementations titles](https://github.com/rust-lang/rust/pull/49335), added [support for variant and types fields for intra links](https://github.com/rust-lang/rust/pull/49512), added [missing anchor for union type fields](https://github.com/rust-lang/rust/pull/49516), fixed [targetted value background](https://github.com/rust-lang/rust/pull/49515), fixed [anchor position on fields](https://github.com/rust-lang/rust/pull/49510), fixed [anchors issue when everything is collapsed](https://github.com/rust-lang/rust/pull/49652) and fixed [url for intra link provided method](https://github.com/rust-lang/rust/pull/49603).

# Meetings

Next meeting will be on Tuesday 10th of April 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
