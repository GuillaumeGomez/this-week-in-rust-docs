---
layout: post
title: This Week in Rust Docs 68
date: 2017-8-13
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

The [rewrite of rustdoc](https://github.com/steveklabnik/rustdoc) is still under heavy development. Don't hesitate to give it a try!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@oli-obk](https://github.com/oli-obk) added [lint casting signed integers smaller than `isize` to raw pointers](https://github.com/rust-lang/rust/pull/43641).
* [@ruuda](https://github.com/ruuda) pointed ["deref coercions" links to new book](https://github.com/rust-lang/rust/pull/43631).
* [@nrc](https://github.com/nrc) fixed [include! in doc tests](https://github.com/rust-lang/rust/pull/43782).
* [@pengowen123](https://github.com/pengowen123) fixed [unused_result lint triggering when a function returns `()`, `!` or an empty enum](https://github.com/rust-lang/rust/pull/43813).
* [@Eijebong](https://github.com/Eijebong) fixed [some typos](https://github.com/rust-lang/rust/pull/43814).
* [@frewsxcv](https://github.com/frewsxcv) improved [doc examples for `include*` macros.](https://github.com/rust-lang/rust/pull/43819).
* [@gaurikholkar](https://github.com/gaurikholkar) added [E0623 for structs](https://github.com/rust-lang/rust/pull/43700).
* [@steveklabnik](https://github.com/steveklabnik) wrote [the "passes" chapter of the rustdoc book](https://github.com/rust-lang/rust/pull/43790).
* [@mattico](https://github.com/mattico) added [lint for int to ptr cast](https://github.com/rust-lang/rust/pull/43339).
* [@qnighy](https://github.com/qnighy) added [hints when intercrate ambiguity causes overlap.](https://github.com/rust-lang/rust/pull/43426).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings when rustdoc html rendering differs](https://github.com/rust-lang/rust/pull/41991), removed [suggest methods in certain cases](https://github.com/rust-lang/rust/pull/43829) and added [missing links doc](https://github.com/rust-lang/rust/pull/43803).

# Recent doc contributions

* [@RalfJung](https://github.com/RalfJung) clarified [wording for E0122](https://github.com/rust-lang/rust/pull/43176).
* [@kennytm](https://github.com/kennytm) exposed [all OS-specific modules in libstd doc](https://github.com/rust-lang/rust/pull/43348) and type-checked [`break value;` even outside of `loop {}`](https://github.com/rust-lang/rust/pull/43745).
* [@estebank](https://github.com/estebank) pointed [at return type always when type mismatch against it](https://github.com/rust-lang/rust/pull/43484).
* [@Aaronepower](https://github.com/Aaronepower) updated [release notes for 1.20](https://github.com/rust-lang/rust/pull/43627).
* [@ruuda](https://github.com/ruuda) detected [relative urls in tidy check](https://github.com/rust-lang/rust/pull/43632).
* [@zackmdavis](https://github.com/zackmdavis) de-orphaned [extended information](https://github.com/rust-lang/rust/pull/43709), added [`#[must_use]` for functions](https://github.com/rust-lang/rust/pull/43728) and made the [e05XX odyssey](https://github.com/rust-lang/rust/pull/43726).
* [@ollie27](https://github.com/ollie27) removed [external impls to implementors js in rustdoc](https://github.com/rust-lang/rust/pull/43736), stopped [using URL shortener in docs](https://github.com/rust-lang/rust/pull/43715) and fixed [broken CSS in search results in rustdoc](https://github.com/rust-lang/rust/pull/43760).
* [@lukaramu](https://github.com/lukaramu) improved [std::ops docs](https://github.com/rust-lang/rust/pull/43724).
* [@tchajed](https://github.com/tchajed) updated [GitHub pull request documentation link](https://github.com/rust-lang/rust/pull/43823).
* [@steveklabnik](https://github.com/steveklabnik) added [doc tests in rustdoc](https://github.com/rust-lang/rust/pull/43812) and documented [the doc attribute](https://github.com/rust-lang/rust/pull/43792).
* [@Eijebong](https://github.com/Eijebong) fixed [some typos](https://github.com/rust-lang/rust/pull/43794).
* [@natboehm](https://github.com/natboehm) provided [more explanation for Deref in String docs](https://github.com/rust-lang/rust/pull/43721).
* [@j-browne](https://github.com/j-browne) fixed [broken links in Arc documentation](https://github.com/rust-lang/rust/pull/43793).
* [@prisme60](https://github.com/prisme60) fixed [typo corersponding -> corresponding](https://github.com/rust-lang/rust/pull/43783).
* [@mattico](https://github.com/mattico) fixed [typo in unicode char definition](https://github.com/rust-lang/rust/pull/43779).
* [@ubsan](https://github.com/ubsan) fixed [a typo](https://github.com/rust-lang/rust/pull/43773).
* [@pornel](https://github.com/pornel) corrected [the extern constant syntax in hint](https://github.com/rust-lang/rust/pull/43720).
* [@ivanbakel](https://github.com/ivanbakel) fixed [mutable vars being marked used when they weren't](https://github.com/rust-lang/rust/pull/43582).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) removed [warn on unused field on union](https://github.com/rust-lang/rust/pull/43397), fixed [rustdoc error on '\0'](https://github.com/rust-lang/rust/pull/43691), added [union and const colors](https://github.com/rust-lang/rust/pull/43558), improved [headers linking](https://github.com/rust-lang/rust/pull/43747), improved [file docs](https://github.com/rust-lang/rust/pull/43791), improved [enum variants display in rustdoc](https://github.com/rust-lang/rust/pull/43795), improved [error message when duplicate names for type and trait method](https://github.com/rust-lang/rust/pull/43737) and added [missing error code for private method](https://github.com/rust-lang/rust/pull/43699).

# Meetings

Next meeting will be on Wednesday 16th of August 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
