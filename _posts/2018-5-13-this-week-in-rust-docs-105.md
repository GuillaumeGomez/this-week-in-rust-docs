---
layout: post
title: This Week in Rust Docs 105
date: 2018-5-13
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
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@sgrif](https://github.com/sgrif) removed [the "leak check" in favor of "universes"](https://github.com/rust-lang/rust/pull/48407).
* [@ecstatic-morse](https://github.com/ecstatic-morse) rewrote [docs for `std::ptr`](https://github.com/rust-lang/rust/pull/49767).
* [@da-x](https://github.com/da-x) included [scope names in diagnostics](https://github.com/rust-lang/rust/pull/49898).
* [@Phlosioneer](https://github.com/Phlosioneer) clarified [the difference between get_mut and into_mut for OccupiedEntry](https://github.com/rust-lang/rust/pull/49743).
* [@mulkieran](https://github.com/mulkieran) made [some documentation fixes for the Write trait](https://github.com/rust-lang/rust/pull/50255).
* [@fkjogu](https://github.com/fkjogu) documented [round-off error in `.mod_euc()`-method](https://github.com/rust-lang/rust/pull/50342).
* [@petrochenkov](https://github.com/petrochenkov) added [deprecation lint for duplicated `macro_export`s](https://github.com/rust-lang/rust/pull/50143).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) deprecated [`#![doc(passes, plugins, no_default_passes)]` in rustdoc](https://github.com/rust-lang/rust/pull/50669) and replaced [most (e)println! statements with structured warnings/errors in rustdoc](https://github.com/rust-lang/rust/pull/50541).
* [@F001](https://github.com/F001) added [lint for multiple associated types](https://github.com/rust-lang/rust/pull/50682).
* [@ollie27](https://github.com/ollie27) added [support for pub(restricted) in rustdoc](https://github.com/rust-lang/rust/pull/50691).
* [@adevore](https://github.com/adevore) added [example writing a &str for fs::write](https://github.com/rust-lang/rust/pull/50624).
* [@sanxiyn](https://github.com/sanxiyn) updated [the man page with additional --print options](https://github.com/rust-lang/rust/pull/50594).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) stabilized [short error format](https://github.com/rust-lang/rust/pull/49546), made [some rustdoc improvements](https://github.com/rust-lang/rust/pull/50259), fixed [extern prelude failure in rustdoc](https://github.com/rust-lang/rust/pull/50617) and added [minification process](https://github.com/rust-lang/rust/pull/50632).

# Recent doc contributions

* [@ibabushkin](https://github.com/ibabushkin) refactored [auto trait handling in librustdoc to be accessible from librustc](https://github.com/rust-lang/rust/pull/49711).
* [@rizakrko](https://github.com/rizakrko) added [missing implementation hint](https://github.com/rust-lang/rust/pull/50161).
* [@clarcharr](https://github.com/clarcharr) mentionned [`Result<!, E>` in never docs](https://github.com/rust-lang/rust/pull/49988).
* [@zackmdavis](https://github.com/zackmdavis) removed [crazy suggestion for unreachable braced pub-use](https://github.com/rust-lang/rust/pull/50476).
* [@leodasvacas](https://github.com/leodasvacas) improve [error reporting in Copy derive](https://github.com/rust-lang/rust/pull/50536).
* [@Screwtapello](https://github.com/Screwtapello) updated [canonicalize docs](https://github.com/rust-lang/rust/pull/50602).
* [@glandium](https://github.com/glandium) restored [RawVec::reserve* documentation](https://github.com/rust-lang/rust/pull/50591) and cleaned up [a `use` in a raw_vec test](https://github.com/rust-lang/rust/pull/50527).
* [@ExpHP](https://github.com/ExpHP) moved ["See also" disambiguation links for primitive types to top](https://github.com/rust-lang/rust/pull/50588).
* [@frewsxcv](https://github.com/frewsxcv) clarified [in the docs that `mul_add` is not always faster](https://github.com/rust-lang/rust/pull/50572).
* [@Manishearth](https://github.com/Manishearth) added [some explanations for #[must_use]](https://github.com/rust-lang/rust/pull/50511).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.26.0](https://github.com/rust-lang/rust/pull/49523).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) prevented [infinite recursion of modules in rustdoc](https://github.com/rust-lang/rust/pull/50305) and fixed [rustdoc pathes search](https://github.com/rust-lang/rust/pull/50432).

# Meetings

Next meeting will be on Tuesday 15th of May 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
