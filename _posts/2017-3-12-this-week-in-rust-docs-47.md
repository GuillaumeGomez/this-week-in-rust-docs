---
layout: post
title: This Week in Rust Docs 47
date: 2017-3-12
---

Hello and welcome to *This Week in Rust Docs*!

*This Week in Rust Docs* is openly developed [on GitHub](https://github.com/GuillaumeGomez/this-week-in-rust-docs).
If you find any errors in this week's issue, [please submit a PR](https://github.com/GuillaumeGomez/this-week-in-rust-docs/pulls).

And of course, don't forget to look at the docs:

* [Stable](https://doc.rust-lang.org/)
* [Beta](http://doc.rust-lang.org/beta/)
* [Nightly](http://doc.rust-lang.org/nightly/)

This week's edition was edited by [Guillaume Gomez](https://github.com/GuillaumeGomez).

# Latest news

Nothing.

# Current opened issues

For now, here are the two big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on GitHub!

# Waiting for merge

* [@Dowwie](https://github.com/Dowwie) updated [attributes.md - Last sentence updated to reflect support for custom attributes](https://github.com/rust-lang/rust/pull/39691).
* [@frewsxcv](https://github.com/frewsxcv) added [basic documentation/examples for six unstable features.](https://github.com/rust-lang/rust/pull/40452).
* [@tschottdorf](https://github.com/tschottdorf) improved [wording in the -{W,A,F,D} options](https://github.com/rust-lang/rust/pull/40453).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing urls and small nits](https://github.com/rust-lang/rust/pull/39513), improved [invalid call on non-function error message](https://github.com/rust-lang/rust/pull/39814), fixed [invalid module suggestion](https://github.com/rust-lang/rust/pull/38255), added [ref suggestion](https://github.com/rust-lang/rust/pull/37658) and replaced [hoedown with pulldown in rustdoc](https://github.com/rust-lang/rust/pull/40338).

# Recent doc contributions

* [@wesleywiser](https://github.com/wesleywiser) improved [the style of the sidebar in rustdoc output](https://github.com/rust-lang/rust/pull/40265).
* [@jdhorwitz](https://github.com/jdhorwitz) helped [people find String::as_bytes() for UTF-8](https://github.com/rust-lang/rust/pull/40226).
* [@steveklabnik](https://github.com/steveklabnik) added [unstable book to the bookshelf](https://github.com/rust-lang/rust/pull/40154) and extracted [nomicon to its own repo](https://github.com/rust-lang/rust/pull/40222).
* [@estebank](https://github.com/estebank) cleaned up ["pattern doesn't bind x" messages](https://github.com/rust-lang/rust/pull/39713), pointed to [enclosing block/fn on nested unsafe](https://github.com/rust-lang/rust/pull/39202) and fixed [incorrect span label formatting](https://github.com/rust-lang/rust/pull/40287).
* [@est31](https://github.com/est31) fixed [description of closure coercion feature](https://github.com/rust-lang/rust/pull/40258).
* [@brson](https://github.com/brson) added [release notes for 1.16](https://github.com/rust-lang/rust/pull/39835).
* [@bjorn3](https://github.com/bjorn3) improved [docs of rusty parts of typeck](https://github.com/rust-lang/rust/pull/40146).
* [@Nashenas88](https://github.com/Nashenas88) fixed [missing backtick typo](https://github.com/rust-lang/rust/pull/40345).
* [@oli-obk](https://github.com/oli-obk) fixed [a typo in the docs](https://github.com/rust-lang/rust/pull/40316).
* [@sinkuu](https://github.com/sinkuu) fixed [suggestion span error with a line containing multibyte characters](https://github.com/rust-lang/rust/pull/40092).
* [@DirkyJerky](https://github.com/DirkyJerky) clarified [docs in `VecDeque::resize`](https://github.com/rust-lang/rust/pull/40423).
* [@tbu-](https://github.com/tbu-) distinguished [the ways `CStr::from_bytes_with_nul` can fail](https://github.com/rust-lang/rust/pull/40386), documented [why `str.to_{lower,upper}case` return `String`](https://github.com/rust-lang/rust/pull/40335) and clarified [handling of `src` in `ptr::write`](https://github.com/rust-lang/rust/pull/40333).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) fixed [normalization error](https://github.com/rust-lang/rust/pull/40268).
* [@crazymerlyn](https://github.com/crazymerlyn) updated [link to COMPILER_TESTS.md in CONTRIBUTING.md](https://github.com/rust-lang/rust/pull/40326).
* [@joelgallant](https://github.com/joelgallant) made some [README formatting in configure/make section](https://github.com/rust-lang/rust/pull/40321).
* [@mmatyas](https://github.com/mmatyas) fixed [text formatting in README](https://github.com/rust-lang/rust/pull/40292).
* [@malbarbo](https://github.com/malbarbo) removed [extra space in test description (of a mod test)](https://github.com/rust-lang/rust/pull/40293).
* [@oconnor663](https://github.com/oconnor663) clarified [docs for Args and ArgsOs](https://github.com/rust-lang/rust/pull/40283).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [associated consts display](https://github.com/rust-lang/rust/pull/40419), added [missing example for Display::fmt](https://github.com/rust-lang/rust/pull/40299), cleaned up [rustdoc css](https://github.com/rust-lang/rust/pull/40278) and added [missing urls in some macros doc](https://github.com/rust-lang/rust/pull/40327).

# Meetings

Next meeting will be on Wednesday 15th of March 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
