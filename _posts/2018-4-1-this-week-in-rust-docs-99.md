---
layout: post
title: This Week in Rust Docs 99
date: 2018-4-1
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

We're back from the all-hands week in Berlin. A lot of things are coming. More information soon?

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@FraGag](https://github.com/FraGag) improved [documentation of Clone and Copy implementors](https://github.com/rust-lang/rust/pull/48171).
* [@tinaun](https://github.com/tinaun) removed [erroneous error message when checking impl trait params](https://github.com/rust-lang/rust/pull/48709).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) suppressed [the default allow(unused) under --display-warnings in rustdoctest](https://github.com/rust-lang/rust/pull/49064), moved [the "important traits" button to beside the type in rustdoc](https://github.com/rust-lang/rust/pull/49286) and added [an --edition flag to compile docs/doctests with a certain edition in rustdoc](https://github.com/rust-lang/rust/pull/49451).
* [@klnusbaum](https://github.com/klnusbaum) provided [better borrow checker error message](https://github.com/rust-lang/rust/pull/48708).
* [@krk](https://github.com/krk) added [submodule fetch instructions](https://github.com/rust-lang/rust/pull/49338).
* [@PramodBisht](https://github.com/PramodBisht) fixed [doc comments present after a particular syntax error cause an unhelpful error message to be output](https://github.com/rust-lang/rust/pull/48946).
* [@zackmdavis](https://github.com/zackmdavis) added [suggestion of `!` for erroneous identifier `not`](https://github.com/rust-lang/rust/pull/49258) and pointed [to value in "value assigned is never read" lint](https://github.com/rust-lang/rust/pull/49197).
* [@SimonSapin](https://github.com/SimonSapin) soft-deprecated [the description() method of the Error trait](https://github.com/rust-lang/rust/pull/49536).
* [@frewsxcv](https://github.com/frewsxcv) clarified [network byte order conversions for integer / IP address conversions](https://github.com/rust-lang/rust/pull/49418).
* [@Phlosioneer](https://github.com/Phlosioneer) added [test for rustdoc ignore test](https://github.com/rust-lang/rust/pull/49532) and fixed [escaped backslash in windows file not found message](https://github.com/rust-lang/rust/pull/49478).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.26.0](https://github.com/rust-lang/rust/pull/49523).
* [@sgrif](https://github.com/sgrif) removed [the "leak check" in favor of "universes"](https://github.com/rust-lang/rust/pull/48407).
* [@ollie27](https://github.com/ollie27) added [docs for the test crate with the std docs](https://github.com/rust-lang/rust/pull/49465).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [error codes for libsyntax_ext](https://github.com/rust-lang/rust/pull/48173), removed [unneeded trait implementations titles](https://github.com/rust-lang/rust/pull/49335), added [repeat method on slice](https://github.com/rust-lang/rust/pull/48999), stabilized [short error format](https://github.com/rust-lang/rust/pull/49546), added [page to list all crate's items](https://github.com/rust-lang/rust/pull/49504), added [warning if a resolution failed](https://github.com/rust-lang/rust/pull/49542), added [support for variant and types fields for intra links](https://github.com/rust-lang/rust/pull/49512), added [missing anchor for union type fields](https://github.com/rust-lang/rust/pull/49516), fixed [targetted value background](https://github.com/rust-lang/rust/pull/49515) and fixed [anchor position on fields](https://github.com/rust-lang/rust/pull/49510).

# Recent doc contributions

* [@Phlosioneer](https://github.com/Phlosioneer) documented [when types have OS-dependent sizes](https://github.com/rust-lang/rust/pull/48932).
* [@pthariensflame](https://github.com/pthariensflame) made [a minor message/label formatting consistency fix](https://github.com/rust-lang/rust/pull/49351).
* [@chisophugis](https://github.com/chisophugis) fixed [confusing doc for `scan`](https://github.com/rust-lang/rust/pull/49353).
* [@sinkuu](https://github.com/sinkuu) added [support for universal_impl_trait in rustdoc](https://github.com/rust-lang/rust/pull/49304).
* [@cuviper](https://github.com/cuviper) corrected [a typo in RELEASES.md](https://github.com/rust-lang/rust/pull/49486).
* [@joshtriplett](https://github.com/joshtriplett) fixed [documentation for size of `Option<NonNull<T>>`](https://github.com/rust-lang/rust/pull/49473).
* [@frewsxcv](https://github.com/frewsxcv) explicitly mentionned [`Option` in `?` error message](https://github.com/rust-lang/rust/pull/49446), clarified ["length" wording in `Vec::with_capacity`](https://github.com/rust-lang/rust/pull/49452) and removed [hidden `foo` functions from doc examples; use `Termination` trait](https://github.com/rust-lang/rust/pull/49357).
* [@lukaslueg](https://github.com/lukaslueg) updated [CONTRIBUTING.md](https://github.com/rust-lang/rust/pull/49426).
* [@alercah](https://github.com/alercah) added [missing '?' to format grammar](https://github.com/rust-lang/rust/pull/49401).
* [@ehuss](https://github.com/ehuss) fixed [diagnostic colors on Windows 10 console](https://github.com/rust-lang/rust/pull/49399).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [impl assoc constant link not working](https://github.com/rust-lang/rust/pull/49333), proposed [a variant if it is an enum for E0599](https://github.com/rust-lang/rust/pull/49223), added [primitive intra-links](https://github.com/rust-lang/rust/pull/49459), hid [type declarations by default](https://github.com/rust-lang/rust/pull/49412), renamed [main theme into light theme](https://github.com/rust-lang/rust/pull/49445), fixed [tooltip position](https://github.com/rust-lang/rust/pull/49443), fixed [search appearance](https://github.com/rust-lang/rust/pull/49405), fixed [collapse toggle insertions on impl with docs](https://github.com/rust-lang/rust/pull/49429), fixed [trait implementation not collapsing docs](https://github.com/rust-lang/rust/pull/49439) and fixed [text overlap](https://github.com/rust-lang/rust/pull/49442).

# Meetings

Next meeting will be on Tuesday 3rd of April 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
