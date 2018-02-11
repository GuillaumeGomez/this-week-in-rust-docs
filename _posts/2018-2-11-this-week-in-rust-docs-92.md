---
layout: post
title: This Week in Rust Docs 92
date: 2018-2-11
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

The roadmap for 2018 is still in discussion. More information soon!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@estebank](https://github.com/estebank) added [`-Zteach` documentation](https://github.com/rust-lang/rust/pull/47843), reworded [E0044 and message for `!Send` types](https://github.com/rust-lang/rust/pull/48138) and detected [possibly non-Rust closure syntax during parse](https://github.com/rust-lang/rust/pull/47763).
* [@partim](https://github.com/partim) improved [documentation for Borrow, AsRef, and friends](https://github.com/rust-lang/rust/pull/46518).
* [@dbrgn](https://github.com/dbrgn) whitelisted [based suggestions](https://github.com/rust-lang/rust/pull/46815).
* [@vi](https://github.com/vi) added [foldable impl blocks in rustdoc](https://github.com/rust-lang/rust/pull/47894).
* [@wesleywiser](https://github.com/wesleywiser) fixed [how paths are printed by error messages during bootstrap](https://github.com/rust-lang/rust/pull/47731).
* [@Aaron1011](https://github.com/Aaron1011) generated [documentation for auto-trait impls](https://github.com/rust-lang/rust/pull/47833).
* [@PramodBisht](https://github.com/PramodBisht) changed [color of struct link from #ff794d to #2dbfb8 for Rust docs](https://github.com/rust-lang/rust/pull/47806).
* [@matthiaskrgr](https://github.com/matthiaskrgr) fixed [typo: endianess to endianness (this also changes function names!)](https://github.com/rust-lang/rust/pull/48133).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) showed [better warning for trying to cast non-u8 scalar to char](https://github.com/rust-lang/rust/pull/48033).

# Recent doc contributions

* [@estebank](https://github.com/estebank) added [filtering options to `rustc_on_unimplemented`](https://github.com/rust-lang/rust/pull/47613).
* [@clarcharr](https://github.com/clarcharr) documented [std::os::raw](https://github.com/rust-lang/rust/pull/46962).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [documentation from doc(include) to analysis data](https://github.com/rust-lang/rust/pull/47496).
* [@steveklabnik](https://github.com/steveklabnik) updated [rust book](https://github.com/rust-lang/rust/pull/47753).
* [@varkor](https://github.com/varkor) documented [the behaviour of infinite iterators on potentially-computable methods](https://github.com/rust-lang/rust/pull/47547), created [a directory for --out-dir if it does not already exist](https://github.com/rust-lang/rust/pull/47854) and warned [when rustc output conflicts with existing directories](https://github.com/rust-lang/rust/pull/47203).
* [@Manishearth](https://github.com/Manishearth) fixed [rustdoc ICE on macros defined within functions](https://github.com/rust-lang/rust/pull/47959) and bailed [early for linky things in intra-docs-links](https://github.com/rust-lang/rust/pull/48064).
* [@frewsxcv](https://github.com/frewsxcv) clarified [shared file handler behavior of File::try_clone](https://github.com/rust-lang/rust/pull/47958).
* [@zackmdavis](https://github.com/zackmdavis) declined [to lint technically-unnecessary parens in function or method arguments inside of nested macros](https://github.com/rust-lang/rust/pull/47896), corrected [unused field pattern suggestions](https://github.com/rust-lang/rust/pull/47922) and corrected [E0619 span re method call receivers whose type must be known](https://github.com/rust-lang/rust/pull/48028).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.24.0](https://github.com/rust-lang/rust/pull/47286).
* [@matthiaskrgr](https://github.com/matthiaskrgr) fixed [typo: substract -> subtract](https://github.com/rust-lang/rust/pull/48107), fixed [typos in src/{bootstrap,ci,etc,lib{backtrace,core,fmt_macros}}](https://github.com/rust-lang/rust/pull/48120) and fixed [typos in config.toml.example](https://github.com/rust-lang/rust/pull/48031).
* [@ollie27](https://github.com/ollie27) hid [`-> ()` in cross crate inlined Fn bounds](https://github.com/rust-lang/rust/pull/48051).
* [@RalfJung](https://github.com/RalfJung) warned [about more ignored bounds in type aliases](https://github.com/rust-lang/rust/pull/48020).
* [@Badel2](https://github.com/Badel2) documented [that associated constants prevent a trait from being made into an object](https://github.com/rust-lang/rust/pull/48026).
* [@mbrubeck](https://github.com/mbrubeck) fixed [info about generic impls in AsMut docs](https://github.com/rust-lang/rust/pull/48003).
* [@jaystrictor](https://github.com/jaystrictor) removed ['the this' in doc comments](https://github.com/rust-lang/rust/pull/47999).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [tests for themes](https://github.com/rust-lang/rust/pull/47761), fixed [themes rendering issues on mobile](https://github.com/rust-lang/rust/pull/47810), fixed [const evaluation ICE in rustdoc](https://github.com/rust-lang/rust/pull/47862) and hide [theme button under menu in mobile mode and fix top margin issue …](https://github.com/rust-lang/rust/pull/48080).

# Meetings

Next meeting will be on Tuesday 13th of February 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
