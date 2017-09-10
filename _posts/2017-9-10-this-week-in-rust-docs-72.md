---
layout: post
title: This Week in Rust Docs 72
date: 2017-9-10
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

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) hid [internal types/traits from std docs via new #[doc(masked)] attribute](https://github.com/rust-lang/rust/pull/44026).
* [@gaurikholkar](https://github.com/gaurikholkar) extended [E0623 for LateBound and EarlyBound Regions](https://github.com/rust-lang/rust/pull/44079) and added [E0623 for return types - both parameters are anonymous](https://github.com/rust-lang/rust/pull/44124).
* [@steveklabnik](https://github.com/steveklabnik) deprecated [several flags in rustdoc](https://github.com/rust-lang/rust/pull/44138) and updated [mdbook](https://github.com/rust-lang/rust/pull/44430).
* [@tommyip](https://github.com/tommyip) added [doc example to String::as_mut_str](https://github.com/rust-lang/rust/pull/44453) and added [doc example to String::as_str](https://github.com/rust-lang/rust/pull/44449).
* [@smt923](https://github.com/smt923) added [short doc examples for str::from_utf8_mut](https://github.com/rust-lang/rust/pull/44472).
* [@toidiu](https://github.com/toidiu) updated [documentation to demonstrate mutability](https://github.com/rust-lang/rust/pull/44467).
* [@napen123](https://github.com/napen123) added [doc examples for str::as_bytes_mut](https://github.com/rust-lang/rust/pull/44457).
* [@frehberg](https://github.com/frehberg) extended [UdpSocket API doc](https://github.com/rust-lang/rust/pull/44378).
* [@est31](https://github.com/est31) moved [the man directory to a subdirectory](https://github.com/rust-lang/rust/pull/44413).
* [@joshlf](https://github.com/joshlf) documented [std::thread::LocalKey limitation with initializers](https://github.com/rust-lang/rust/pull/44396).
* [@laumann](https://github.com/laumann) added [suggestions for misspelled method names](https://github.com/rust-lang/rust/pull/44297).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) stabilised [compile_fail](https://github.com/rust-lang/rust/pull/43949), added [deref suggestion](https://github.com/rust-lang/rust/pull/43870), fixed [rendering of const keyword for functions](https://github.com/rust-lang/rust/pull/44254), added [display of cfg in rustdoc](https://github.com/rust-lang/rust/pull/44165), codeblock [color](https://github.com/rust-lang/rust/pull/44397), reduced [false positives number in rustdoc html diff](https://github.com/rust-lang/rust/pull/44347) and removed [small id false positive in rustdoc html diff](https://github.com/rust-lang/rust/pull/44350).

# Recent doc contributions

* [@qnighy](https://github.com/qnighy) added [hints when intercrate ambiguity causes overlap](https://github.com/rust-lang/rust/pull/43426).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [new "Implementations on Foreign Types" section to traits in rustdoc](https://github.com/rust-lang/rust/pull/43849) and expanded [on using rustup custom toolchains in CONTRIBUTING.md](https://github.com/rust-lang/rust/pull/44194).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) added [rustdoc tests](https://github.com/rust-lang/rust/pull/44274).
* [@MarkMcCaskey](https://github.com/MarkMcCaskey) updated [unimplemented! docs](https://github.com/rust-lang/rust/pull/44206).
* [@kennytm](https://github.com/kennytm) removed [invalid doctest from bootstrap.py](https://github.com/rust-lang/rust/pull/44268).
* [@WiSaGaN](https://github.com/WiSaGaN) fixed [link typo in 1.20.0 release notes](https://github.com/rust-lang/rust/pull/44330).
* [@jakllsch](https://github.com/jakllsch) included [docs in extended distribution only if enabled](https://github.com/rust-lang/rust/pull/44321).
* [@lu-zero](https://github.com/lu-zero) removed [the incorrect documentation for from_str](https://github.com/rust-lang/rust/pull/44328).
* [@RalfJung](https://github.com/RalfJung) removed [dead test functions from rustbook](https://github.com/rust-lang/rust/pull/44313).
* [@kallisti5](https://github.com/kallisti5) gave [an example to get UNIX_EPOCH in seconds in `std::time`](https://github.com/rust-lang/rust/pull/44315).

# Meetings

Next meeting will be on Wednesday 13th of September 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
