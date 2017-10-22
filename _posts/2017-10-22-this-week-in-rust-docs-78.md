---
layout: post
title: This Week in Rust Docs 78
date: 2017-10-22
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

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) included [external files in documentation in rustdoc (RFC 1990)](https://github.com/rust-lang/rust/pull/44781), showed [in docs whether the return type of a function impls Iterator/Read/Write](https://github.com/rust-lang/rust/pull/45039) and updated [pulldown and fixed spurious rendering difference around footnotes](https://github.com/rust-lang/rust/pull/45421).
* [@frewsxcv](https://github.com/frewsxcv) improved [docs around `Once::call_once_force` and `OnceState`](https://github.com/rust-lang/rust/pull/45429).
* [@carols10cents](https://github.com/carols10cents) corrected [misspelling in error text: re-assignment => reassignment](https://github.com/rust-lang/rust/pull/45398).
* [@Technius](https://github.com/Technius) improved [std::process module docs](https://github.com/rust-lang/rust/pull/45295).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [short error message-format](https://github.com/rust-lang/rust/pull/44636), improved [sidebar rendering and added methods list](https://github.com/rust-lang/rust/pull/45187), limited [the sidebar height](https://github.com/rust-lang/rust/pull/45212) and added [missing code examples](https://github.com/rust-lang/rust/pull/45361).

# Recent doc contributions

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) made [rustdoc optimizations](https://github.com/rust-lang/rust/pull/44613).
* [@steveklabnik](https://github.com/steveklabnik) deprecated [several flags in rustdoc](https://github.com/rust-lang/rust/pull/44138) and fixed [most rendering warnings from switching to CommonMark](https://github.com/rust-lang/rust/pull/45419).
* [@sunjay](https://github.com/sunjay) documented [the process for when rustfmt/rls break](https://github.com/rust-lang/rust/pull/45098).
* [@jacwah](https://github.com/jacwah) mentionned [Clone and refs in --explain E0382](https://github.com/rust-lang/rust/pull/45082).
* [@goffrie](https://github.com/goffrie) provided [the full span of method calls to `check_argument_types`](https://github.com/rust-lang/rust/pull/45123) and marked [block exits as reachable if the block can break](https://github.com/rust-lang/rust/pull/45316).
* [@Havvy](https://github.com/Havvy) made [a list of all lang items in unstable book](https://github.com/rust-lang/rust/pull/45181).
* [@frewsxcv](https://github.com/frewsxcv) expanded [docs/examples for TCP `set_nonblocking` methods](https://github.com/rust-lang/rust/pull/45227).
* [@0xAX](https://github.com/0xAX) fixed [a typo in src/bootstrap/README.md](https://github.com/rust-lang/rust/pull/45264).
* [@SimonSapin](https://github.com/SimonSapin) fixed [out of date unstable book entries for `alloc_*` features](https://github.com/rust-lang/rust/pull/45217).
* [@topecongiro](https://github.com/topecongiro) fixed [typos in README.md](https://github.com/rust-lang/rust/pull/45407), fixed [typos in src/librustc/README.md](https://github.com/rust-lang/rust/pull/45376) and fixed [typos in librustc/ty/README.md](https://github.com/rust-lang/rust/pull/45377).
* [@Manishearth](https://github.com/Manishearth) removed ["gender" from code of conduct, keep only "gender identity and expression"](https://github.com/rust-lang/rust/pull/45418).
* [@neunenak](https://github.com/neunenak) added [explanatory text for error E0599](https://github.com/rust-lang/rust/pull/45356).
* [@christianpoveda](https://github.com/christianpoveda) added [examples of closures for str::find](https://github.com/rust-lang/rust/pull/45349).
* [@zackmdavis](https://github.com/zackmdavis) added [code suggestions for non-shorthand field pattern, no-mangle lints](https://github.com/rust-lang/rust/pull/45232) and removed ["expected statement after outer attr." after inner attr](https://github.com/rust-lang/rust/pull/45315).
* [@stjepang](https://github.com/stjepang) updated docs: [a LocalKey might start in the Valid state](https://github.com/rust-lang/rust/pull/45340).
* [@xfix](https://github.com/xfix) updated [array documentation for Clone trait changes](https://github.com/rust-lang/rust/pull/45339).
* [@dbrgn](https://github.com/dbrgn) added [missing headlines in rustdoc book](https://github.com/rust-lang/rust/pull/45308) and fixed [typo in rustdoc book](https://github.com/rust-lang/rust/pull/45307).
* [@Pirh](https://github.com/Pirh) documented [defaults for stdin, stdout, and stderr methods of Command](https://github.com/rust-lang/rust/pull/45151).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) saved [selected search tab](https://github.com/rust-lang/rust/pull/45281), saved [the highlighted item when switching tab](https://github.com/rust-lang/rust/pull/45288), removed [terribly useless and problematic margin when searching on mobile](https://github.com/rust-lang/rust/pull/45280), fixed [arrow display](https://github.com/rust-lang/rust/pull/45289), hid [help when search bar is focused](https://github.com/rust-lang/rust/pull/45290), printed [rustdoc rendering warnings all the time](https://github.com/rust-lang/rust/pull/45324) and removed [duplicated word](https://github.com/rust-lang/rust/pull/45329).

# Meetings

Next meeting will be on Tuesday 24th of October 2017 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
