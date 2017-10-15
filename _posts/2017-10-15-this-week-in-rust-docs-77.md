---
layout: post
title: This Week in Rust Docs 77
date: 2017-10-15
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

The switch to [Pulldown](https://github.com/google/pulldown-cmark) for the rust doc rendering has finally [started](https://github.com/rust-lang/rust/pull/41991)!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) made [rustdoc optimizations](https://github.com/rust-lang/rust/pull/44613), included [external files in documentation in rustdoc (RFC 1990)](https://github.com/rust-lang/rust/pull/44781) and showed [in docs whether the return type of a function impls Iterator/Read/Write](https://github.com/rust-lang/rust/pull/45039).
* [@steveklabnik](https://github.com/steveklabnik) deprecated [several flags in rustdoc](https://github.com/rust-lang/rust/pull/44138).
* [@estebank](https://github.com/estebank) suggested [syntax when finding method on array](https://github.com/rust-lang/rust/pull/44970), warned [when assigning a block that doesn't have an implicit return](https://github.com/rust-lang/rust/pull/44881) and referred [to types using the local identifier](https://github.com/rust-lang/rust/pull/44642).
* [@sunjay](https://github.com/sunjay) documented [the process for when rustfmt/rls break](https://github.com/rust-lang/rust/pull/45098).
* [@jacwah](https://github.com/jacwah) mentionned [Clone and refs in --explain E0382](https://github.com/rust-lang/rust/pull/45082).
* [@Nemo157](https://github.com/Nemo157) rendered [cfg(feature) requirements in documentation](https://github.com/rust-lang/rust/pull/44994).
* [@goffrie](https://github.com/goffrie) provided [the full span of method calls to `check_argument_types`](https://github.com/rust-lang/rust/pull/45123).
* [@Havvy](https://github.com/Havvy) made [a list of all lang items in unstable book](https://github.com/rust-lang/rust/pull/45181).
* [@frewsxcv](https://github.com/frewsxcv) expanded [docs/examples for TCP `set_nonblocking` methods](https://github.com/rust-lang/rust/pull/45227).
* [@0xAX](https://github.com/0xAX) fixed [a typo in src/bootstrap/README.md](https://github.com/rust-lang/rust/pull/45264).
* [@SimonSapin](https://github.com/SimonSapin) fixed [out of date unstable book entries for `alloc_*` features](https://github.com/rust-lang/rust/pull/45217).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [short error message-format](https://github.com/rust-lang/rust/pull/44636), improved [sidebar rendering and added methods list](https://github.com/rust-lang/rust/pull/45187), save [selected search tab](https://github.com/rust-lang/rust/pull/45281), saved [the highlighted item when switching tab](https://github.com/rust-lang/rust/pull/45288), removed [terribly useless and problematic margin when searching on mobile](https://github.com/rust-lang/rust/pull/45280), fixed [arrow display](https://github.com/rust-lang/rust/pull/45289), hid [help when search bar is focused](https://github.com/rust-lang/rust/pull/45290) and limited [the sidebar height](https://github.com/rust-lang/rust/pull/45212).

# Recent doc contributions

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) documented [trait impls when the type appears in the trait's generics](https://github.com/rust-lang/rust/pull/44969) and let [rustdoc print the crate version into docs](https://github.com/rust-lang/rust/pull/44989).
* [@kennytm](https://github.com/kennytm) improved [doc-test: in Markdown tests, Use all of `<h1>` to `<h6>` as the test name](https://github.com/rust-lang/rust/pull/44867).
* [@federicomenaquintero](https://github.com/federicomenaquintero) improved [docs for CStr, CString, OsStr, OsString](https://github.com/rust-lang/rust/pull/44855).
* [@shepmaster](https://github.com/shepmaster) don't [encourage people to ignore threading errors in the docs](https://github.com/rust-lang/rust/pull/44962).
* [@oli-obk](https://github.com/oli-obk) upgraded [some comments to doc comments](https://github.com/rust-lang/rust/pull/45172).
* [@petrochenkov](https://github.com/petrochenkov) fixed [a mistake in release notes for 1.21.0](https://github.com/rust-lang/rust/pull/45171).
* [@sinkuu](https://github.com/sinkuu) made [a better error message for missing tuple pattern in args](https://github.com/rust-lang/rust/pull/45069).
* [@stjepang](https://github.com/stjepang) increased [padding between consecutive impls in rustdoc](https://github.com/rust-lang/rust/pull/45245).
* [@Gankro](https://github.com/Gankro) clarified [how needs_drop is conservative](https://github.com/rust-lang/rust/pull/45253).
* [@laumann](https://github.com/laumann) added [suggestions for misspelled labels](https://github.com/rust-lang/rust/pull/45173).
* [@Badel2](https://github.com/Badel2) made [a better error message for comma after base struct](https://github.com/rust-lang/rust/pull/45178).
* [@jean-lourenco](https://github.com/jean-lourenco) improved [compile error output when using arguments instead of types](https://github.com/rust-lang/rust/pull/45122).
* [@johnthagen](https://github.com/johnthagen) fixed [typos](https://github.com/rust-lang/rust/pull/45116) and clarified [RAM usage during build in README](https://github.com/rust-lang/rust/pull/45136).
* [@tinaun](https://github.com/tinaun) documented [a few more unstable feature gates](https://github.com/rust-lang/rust/pull/45166).
* [@camsteffen](https://github.com/camsteffen) fixed [rustc documentation typo](https://github.com/rust-lang/rust/pull/45105).
* [@rkruppe](https://github.com/rkruppe) fixed [typo in codegen test](https://github.com/rust-lang/rust/pull/45089).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [tabs for search for better information access](https://github.com/rust-lang/rust/pull/45055), usize [index message for vec](https://github.com/rust-lang/rust/pull/45133) and made [improvements in the mobile sidebar](https://github.com/rust-lang/rust/pull/45240).

# Meetings

Next meeting will be on Wednesday 18th of October 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
