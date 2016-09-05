---
layout: post
title: This Week in Rust Docs 20
date: 2016-09-05
---

Hello and welcome to *This Week in Rust Docs*!

*This Week in Rust Docs* is openly developed [on GitHub](https://github.com/GuillaumeGomez/this-week-in-rust-docs).
If you find any errors in this week's issue, [please submit a PR](https://github.com/GuillaumeGomez/this-week-in-rust-docs/pulls).

And of course, don't forget to look at the docs:

* [Stable](https://doc.rust-lang.org/)
* [Beta](http://doc.rust-lang.org/beta/)
* [Nightly](http://doc.rust-lang.org/nightly/)

This week's edition was edited by [Matthew Piziak](https://github.com/matthew-piziak).

# Latest news (getting a bit old but still gold!)

Please take a look [to the next rust doc days planning reminder](https://users.rust-lang.org/t/reminder-planning-the-next-rust-doc-days/6901).

The topic to propose crates for the Rust Doc Days is still open and waiting for contributions [here](https://users.rust-lang.org/t/call-for-proposals-for-next-rust-doc-days-crates/6685). Please take a look!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [Error code list which need to be updated to new format](https://github.com/rust-lang/rust/issues/35233)
* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on GitHub!

# Call for participation

There's now a call for participation to [display all methods of a type, even those from implicit traits in rustdoc](https://github.com/rust-lang/rust/issues/33772). This is a great way to help users find everything that a type can do. Any help on it would be very appreciated!

# Waiting for merge

* [@matthew-piziak](https://github.com/matthew-piziak) added [links to interesting items in `std::ptr` documentation](https://github.com/rust-lang/rust/pull/35880) and [refactored range examples](https://github.com/rust-lang/rust/pull/35759)
* [@frewsxcv](https://github.com/frewsxcv) indicated [where `core::result::IntoIter` is created](https://github.com/rust-lang/rust/pull/35845)
* [@steveklabnik](https://github.com/steveklabnik) made it clear that [reference isn't normative](https://github.com/rust-lang/rust/pull/35102)
* [@ollie27](https://github.com/ollie27) fixed [associated consts in search results](https://github.com/rust-lang/rust/pull/36078)
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [formatting generation for rustdoc code examples](https://github.com/rust-lang/rust/pull/35012) and [added missing urls](https://github.com/rust-lang/rust/pull/36243)
* [@Cobrand](Cobrand) added [mention of `make tidy`](https://github.com/rust-lang/rust/pull/36241)
* [@c4rlo](https://github.com/c4rlo) fixed [a "\\" in a table heading to be "/"](https://github.com/rust-lang/rust/pull/36204)
* [@apasel422](https://github.com/apasel422) cleaned up [thread-local storage docs](https://github.com/rust-lang/rust/pull/36263)


# Recent doc contributions

This week (too), I'll split between the [new error code format](https://github.com/rust-lang/rust/issues/35233) contributions and the others. Let's start by the first one:

* [@KiChjang](https://github.com/KiChjang): [E0379](https://github.com/rust-lang/rust/pull/35480)
* [@EugeneGonzalez](https://github.com/EugeneGonzalez): [E0528](https://github.com/rust-lang/rust/pull/36205) and [E0259](https://github.com/rust-lang/rust/pull/35773)
* [@abhiQmar](https://github.com/abhiQmar): [E0076](https://github.com/rust-lang/rust/pull/36050) and [E0558](https://github.com/rust-lang/rust/pull/36223)
* [@mikhail-m1](https://github.com/mikhail-m1): [E0451](https://github.com/rust-lang/rust/pull/36054) and [E0265](https://github.com/rust-lang/rust/pull/36147)
* [@birryree](https://github.com/birryree): [E0194](https://github.com/rust-lang/rust/pull/36148)
* [@paulfanelli](https://github.com/paulfanelli): [E0463](https://github.com/rust-lang/rust/pull/36060)
* [@acrrd](https://github.com/acrrd): [E0318](https://github.com/rust-lang/rust/pull/36079)
* [@0xmohit](https://github.com/0xmohit): [E0260](https://github.com/rust-lang/rust/pull/36100), [E0520](https://github.com/rust-lang/rust/pull/36135)
* [@zjhmale](https://github.com/zjhmale): [E0393](https://github.com/rust-lang/rust/pull/36114)
* [@gavinb](https://github.com/gavinb): [E0164, E0615, and E0184](https://github.com/rust-lang/rust/pull/36125)
* [@athulappadan](https://github.com/athulappadan): [E0034](https://github.com/rust-lang/rust/pull/36136)

Other contributions:

* [@matthew-piziak](https://github.com/matthew-piziak) improved [documentation for `Fn*` traits](https://github.com/rust-lang/rust/pull/35810), added [evocative examples for `Shl` and `Shr`](https://github.com/rust-lang/rust/pull/35863), added [evocative examples for `BitOr` and `BitXor`](https://github.com/rust-lang/rust/pull/35926), replaced [`BitAndAssign` example with something more evocative](https://github.com/rust-lang/rust/pull/35927), improved [`BitAnd` trait documentation](https://github.com/rust-lang/rust/pull/35993), added [a simple example for `thread::current()`](https://github.com/rust-lang/rust/pull/35997), implemented [accumulate vector and assert for `RangeFrom` and `RangeInclusive` examples](https://github.com/rust-lang/rust/pull/35758), showed [how iterating over `RangeTo` and `RangeToInclusive` fails](https://github.com/rust-lang/rust/pull/35771), and [demonstrated `RHS != Self` use cases for `Add` and `Sub`](https://github.com/rust-lang/rust/pull/35793)
* [@F001](https://github.com/F001) fixed [documentation in the `cell` module](https://github.com/rust-lang/rust/pull/35895)
* [@regexident](https://github.com/regexident) updated a [code sample in chapter on syntax extensions](https://github.com/rust-lang/rust/pull/35962)
* [@frewsxcv](https://github.com/frewsxcv) noticed that [rustbook chapters/sections should be ordered lists](https://github.com/rust-lang/rust/pull/36130)
* [@tshepang](https://github.com/tshepang) made the [`TcpListener` example more simple](https://github.com/rust-lang/rust/pull/36134)
* [@dns2utf8](https://github.com/dns2utf8) updated [the man pages](https://github.com/rust-lang/rust/pull/36152)
* [@fanzier](https://github.com/fanzier) fixed a [typo in `PartialOrd ` docs](https://github.com/rust-lang/rust/pull/36165)
* [@wdv4758h](https://github.com/wdv4758h) changed [`rustc::plugin` to `rustc_plugin` in a doc comment](https://github.com/rust-lang/rust/pull/36169)
* [@birkenfeld](https://github.com/birkenfeld) explained [why `Box`/`Rc`/`Arc` methods do not take `self`](https://github.com/rust-lang/rust/pull/35418)
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) improved [`Path` and `PathBuf` docs](https://github.com/rust-lang/rust/pull/35786)
* [@durka](https://github.com/durka) indicated [where to copy `config.toml.example`](https://github.com/rust-lang/rust/pull/36231)
* [@skade](https://github.com/skade) documented [`try!`'s error conversion behavior](https://github.com/rust-lang/rust/pull/36099)

# Meetings

Next meeting will be on Wednesday 7th of September 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
