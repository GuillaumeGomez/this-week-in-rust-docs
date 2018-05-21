---
layout: post
title: This Week in Rust Docs 106
date: 2018-5-21
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

Some improvements on JS size are being worked on. More to come soon!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/projects/1)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@Phlosioneer](https://github.com/Phlosioneer) clarified [the difference between get_mut and into_mut for OccupiedEntry](https://github.com/rust-lang/rust/pull/49743).
* [@mulkieran](https://github.com/mulkieran) made [some documentation fixes for the Write trait](https://github.com/rust-lang/rust/pull/50255).
* [@fkjogu](https://github.com/fkjogu) documented [round-off error in `.mod_euc()`-method](https://github.com/rust-lang/rust/pull/50342).
* [@petrochenkov](https://github.com/petrochenkov) added [deprecation lint for duplicated `macro_export`s](https://github.com/rust-lang/rust/pull/50143).
* [@F001](https://github.com/F001) added [lint for multiple associated types](https://github.com/rust-lang/rust/pull/50682).
* [@frewsxcv](https://github.com/frewsxcv) provided [more context for what the {f32,f64}::EPSILON values represent](https://github.com/rust-lang/rust/pull/50919).
* [@davidtwco](https://github.com/davidtwco) added [rustdoc documentation to compiler docs](https://github.com/rust-lang/rust/pull/50892).
* [@mandeep](https://github.com/mandeep) added [doc comment to hiding portions of code example](https://github.com/rust-lang/rust/pull/50852).
* [@simartin](https://github.com/simartin) improved [error diagnostic with missing commas after struct fields](https://github.com/rust-lang/rust/pull/50914).
* [@d-e-s-o](https://github.com/d-e-s-o) fixed [typo in cell.rs](https://github.com/rust-lang/rust/pull/50913).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) used ["short form" doc(cfg) printing even when combined with other conditionals in rustdoc](https://github.com/rust-lang/rust/pull/50875).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) stabilized [short error format](https://github.com/rust-lang/rust/pull/49546), fixed [extern prelude failure in rustdoc](https://github.com/rust-lang/rust/pull/50617) and added [E0665](https://github.com/rust-lang/rust/pull/50846).

# Recent doc contributions

* [@ecstatic-morse](https://github.com/ecstatic-morse) rewrote [docs for `std::ptr`](https://github.com/rust-lang/rust/pull/49767).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) deprecated [`#![doc(passes, plugins, no_default_passes)]` in rustdoc](https://github.com/rust-lang/rust/pull/50669) and replaced [most (e)println! statements with structured warnings/errors in rustdoc](https://github.com/rust-lang/rust/pull/50541).
* [@ollie27](https://github.com/ollie27) added [support for pub(restricted) in rustdoc](https://github.com/rust-lang/rust/pull/50691).
* [@adevore](https://github.com/adevore) added [example writing a &str for fs::write](https://github.com/rust-lang/rust/pull/50624).
* [@sanxiyn](https://github.com/sanxiyn) updated [the man page with additional --print options](https://github.com/rust-lang/rust/pull/50594).
* [@shepmaster](https://github.com/shepmaster) fixed [UnsafeCell doc typos and minor flow improvements](https://github.com/rust-lang/rust/pull/50898).
* [@frewsxcv](https://github.com/frewsxcv) fixed [incorrect statement about return value for Iterator::zip](https://github.com/rust-lang/rust/pull/50719).
* [@robinkrahl](https://github.com/robinkrahl) reordered [description for snippets in rustdoc documentation](https://github.com/rust-lang/rust/pull/50858).
* [@shamiao](https://github.com/shamiao) fixed [a typo in signed-integer::from_str_radix()](https://github.com/rust-lang/rust/pull/50797).
* [@sinkuu](https://github.com/sinkuu) fixed [rustdoc panic with `impl Trait` in type parameters](https://github.com/rust-lang/rust/pull/50728).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) made [some rustdoc improvements](https://github.com/rust-lang/rust/pull/50259), added [minification process](https://github.com/rust-lang/rust/pull/50632), added [auto-impl for primitive type](https://github.com/rust-lang/rust/pull/50533) and added [missing error codes in libsyntax-ext asm](https://github.com/rust-lang/rust/pull/50752).

# Meetings

Next meeting will be on Tuesday 22nd of May 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
