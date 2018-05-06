---
layout: post
title: This Week in Rust Docs 104
date: 2018-5-6
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
* [@ibabushkin](https://github.com/ibabushkin) refactored [auto trait handling in librustdoc to be accessible from librustc](https://github.com/rust-lang/rust/pull/49711).
* [@rizakrko](https://github.com/rizakrko) added [missing implementation hint](https://github.com/rust-lang/rust/pull/50161).
* [@mulkieran](https://github.com/mulkieran) made [some documentation fixes for the Write trait](https://github.com/rust-lang/rust/pull/50255).
* [@clarcharr](https://github.com/clarcharr) added [missing Wrapping methods](https://github.com/rust-lang/rust/pull/50465) and mentionned [`Result<!, E>` in never docs](https://github.com/rust-lang/rust/pull/49988).
* [@nikomatsakis](https://github.com/nikomatsakis) improved [single-use and zero-use lifetime lints](https://github.com/rust-lang/rust/pull/50440).
* [@zackmdavis](https://github.com/zackmdavis) removed [crazy suggestion for unreachable braced pub-use](https://github.com/rust-lang/rust/pull/50476).
* [@fkjogu](https://github.com/fkjogu) documented [round-off error in `.mod_euc()`-method](https://github.com/rust-lang/rust/pull/50342).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) stabilized [short error format](https://github.com/rust-lang/rust/pull/49546), prevented [infinite recursion of modules in rustdoc](https://github.com/rust-lang/rust/pull/50305), made [some rustdoc improvements](https://github.com/rust-lang/rust/pull/50259) and fixed [rustdoc pathes search](https://github.com/rust-lang/rust/pull/50432).

# Recent doc contributions

* [@Manishearth](https://github.com/Manishearth) used [enum for approximate suggestions](https://github.com/rust-lang/rust/pull/50204).
* [@z4v1er](https://github.com/z4v1er) fixed [typo](https://github.com/rust-lang/rust/pull/50217).
* [@kornelski](https://github.com/kornelski) buried [Error::description()](https://github.com/rust-lang/rust/pull/50163) and suggested [more helpful formatting string](https://github.com/rust-lang/rust/pull/50441).
* [@kennytm](https://github.com/kennytm) clarified [wordings of the `unstable_name_collision` lint](https://github.com/rust-lang/rust/pull/50360).
* [@frewsxcv](https://github.com/frewsxcv) updated [books for the next release](https://github.com/rust-lang/rust/pull/50470).
* [@sinkuu](https://github.com/sinkuu) resolved [nested `impl Trait`s in rustdoc](https://github.com/rust-lang/rust/pull/50419).
* [@varkor](https://github.com/varkor) displayed [correct unused field suggestion for nested struct patterns](https://github.com/rust-lang/rust/pull/50327) and improved [error message for #[repr(align=x)]](https://github.com/rust-lang/rust/pull/50317).
* [@ehuss](https://github.com/ehuss) fixed [some broken links in docs](https://github.com/rust-lang/rust/pull/50316).
* [@Pazzaz](https://github.com/Pazzaz) added [more links in panic docs](https://github.com/rust-lang/rust/pull/50312).
* [@ollie27](https://github.com/ollie27) fixed [links to constants in external crates in rustdoc](https://github.com/rust-lang/rust/pull/50326).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [query search order check](https://github.com/rust-lang/rust/pull/50302), fixed [invalid path generation in rustdoc search](https://github.com/rust-lang/rust/pull/50320) and renamed ["show type declaration" to "show declaration"](https://github.com/rust-lang/rust/pull/50349).

# Meetings

Next meeting will be on Tuesday 8th of May 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
