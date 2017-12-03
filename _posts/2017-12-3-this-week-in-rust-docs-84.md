---
layout: post
title: This Week in Rust Docs 84
date: 2017-12-3
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

* [@estebank](https://github.com/estebank) displayed [`\t` in diagnostics code as four spaces](https://github.com/rust-lang/rust/pull/45953), highlighted [code on diagnostics when underlined](https://github.com/rust-lang/rust/pull/45752) and showed [closure signature on type errors](https://github.com/rust-lang/rust/pull/46350).
* [@JRegimbal](https://github.com/JRegimbal) changed ["Types/modules" title of search tab to be more accurate](https://github.com/rust-lang/rust/pull/45898).
* [@canndrew](https://github.com/canndrew) added [docs for never primitive](https://github.com/rust-lang/rust/pull/46232).
* [@tbu-](https://github.com/tbu-) clarified [what `-D warnings` or `-F warnings` does](https://github.com/rust-lang/rust/pull/46136).
* [@nak3](https://github.com/nak3) fixed [invalid docs path for compiler plugins](https://github.com/rust-lang/rust/pull/46463).
* [@zackmdavis](https://github.com/zackmdavis) added [type error method suggestions use whitelisted identity-like conversions](https://github.com/rust-lang/rust/pull/46461).
* [@SimonSapin](https://github.com/SimonSapin) documented [the size of bool](https://github.com/rust-lang/rust/pull/46156).
* [@tromey](https://github.com/tromey) fixed [documentation for DecodeUtf16Error](https://github.com/rust-lang/rust/pull/46432).
* [@steveklabnik](https://github.com/steveklabnik) mentionned [the name of ? in Result's docs](https://github.com/rust-lang/rust/pull/46431).
* [@archer884](https://github.com/archer884) changed [const error message to use 'literal'](https://github.com/rust-lang/rust/pull/46341).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.23.0](https://github.com/rust-lang/rust/pull/46327).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings for markdown doc generation](https://github.com/rust-lang/rust/pull/46247), speedup [search loading when search url is received in rust docs](https://github.com/rust-lang/rust/pull/46221), fixed [deduplication of items in rust docs search](https://github.com/rust-lang/rust/pull/46433), fixed [search results overlap](https://github.com/rust-lang/rust/pull/46454), moved [colors to main.css](https://github.com/rust-lang/rust/pull/46444) and removed [display of hidden types in rustdoc](https://github.com/rust-lang/rust/pull/46359).

# Recent doc contributions

* [@estebank](https://github.com/estebank) accounted [for missing keyword in fn/struct definition](https://github.com/rust-lang/rust/pull/45997), suggested [using slice when encountering `let x = ""[..];`](https://github.com/rust-lang/rust/pull/46249), used [suggestions instead of notes ref mismatches](https://github.com/rust-lang/rust/pull/46256), pointed [to next token when it is in the expected line](https://github.com/rust-lang/rust/pull/46381), highlighted [`&` when type matches on type mismatch error](https://github.com/rust-lang/rust/pull/46349) and shortened [output of E0391](https://github.com/rust-lang/rust/pull/46282).
* [@colinmarsh19](https://github.com/colinmarsh19) added [a note "please remove this semicolon"](https://github.com/rust-lang/rust/pull/46258).
* [@frewsxcv](https://github.com/frewsxcv) improved [documentation for slice swap/copy/clone operations](https://github.com/rust-lang/rust/pull/46219).
* [@lucasem](https://github.com/lucasem) fixed [typo in core::marker](https://github.com/rust-lang/rust/pull/46234).
* [@davidalber](https://github.com/davidalber) added [`eprint*!` to the list of macros in the `format!` family](https://github.com/rust-lang/rust/pull/46201).
* [@ollie27](https://github.com/ollie27) fixed [issues with cross-crate inlined associated items in rustdoc](https://github.com/rust-lang/rust/pull/46384).
* [@SimonSapin](https://github.com/SimonSapin) documented [non-obvious behavior of fmt::UpperHex & co for negative integers](https://github.com/rust-lang/rust/pull/46285) and expanded [docs of <$Int>::from_str_radix, based on that of char::to_digit](https://github.com/rust-lang/rust/pull/46240).
* [@chrisduerr](https://github.com/chrisduerr) fixed [rustdoc item summaries that are headers](https://github.com/rust-lang/rust/pull/46387).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [global doc search](https://github.com/rust-lang/rust/pull/46175), removed [invalid doc link](https://github.com/rust-lang/rust/pull/46224), inverted [colors in important traits tooltip](https://github.com/rust-lang/rust/pull/46392) and fixed [invalid HTML escape](https://github.com/rust-lang/rust/pull/46326).

# Meetings

Next meeting will be on Tuesday 5th of December 2017 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
