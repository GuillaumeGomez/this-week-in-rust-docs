---
layout: post
title: This Week in Rust Docs 35
date: 2016-12-18
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

The way rustdoc is creating urls is problematic for the moment. A good summary of this issue can be found [here](https://github.com/rust-lang/rust/issues/36417). A few members of the Rust Doc team are preparing an RFC in order to improve this. If you want to get involved, feel free to speak about it with [Guillaume Gomez](https://github.com/GuillaumeGomez) (imperio on IRC).

Please take a look [to the next rust doc days planning reminder](https://users.rust-lang.org/t/reminder-planning-the-next-rust-doc-days/6901).

The topic to propose crates for the Rust Doc Days is still open and waiting for contributions [here](https://users.rust-lang.org/t/call-for-proposals-for-next-rust-doc-days-crates/6685). Please take a look!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on GitHub!

# Waiting for merge

* [@frewsxcv](https://github.com/frewsxcv) improved [the API examples for `std::fs::File`](https://github.com/rust-lang/rust/pull/38443), documented [platform-specific differences for `std::process::exit`](https://github.com/rust-lang/rust/pull/38397), improved [documentation for `core::hash::BuildHasherDefault`](https://github.com/rust-lang/rust/pull/38334) and improved [`BTreeSet` documentation](https://github.com/rust-lang/rust/pull/38208).
* [@bluecereal](https://github.com/bluecereal) updated [if-let.md](https://github.com/rust-lang/rust/pull/38436).
* [@brson](https://github.com/brson) wrote [the 1.14 release notes](https://github.com/rust-lang/rust/pull/38427).
* [@ollie27](https://github.com/ollie27) fixed [invalid HTML in stability notices in rustdoc](https://github.com/rust-lang/rust/pull/38329) and fixed [short summaries in search results in rustdoc](https://github.com/rust-lang/rust/pull/38330).
* [@estebank](https://github.com/estebank) used [struct name as span instead of entire block](https://github.com/rust-lang/rust/pull/38328), disambiguated [Implementors when the type name is not unique in rustdoc](https://github.com/rust-lang/rust/pull/38414), showed [span for trait that doesn't implement Copy](https://github.com/rust-lang/rust/pull/37493), escaped [the deprecated and unstable reason text in rustdoc](https://github.com/rust-lang/rust/pull/38244), pointed out [the known type when field doesn't satisfy bound](https://github.com/rust-lang/rust/pull/38150) and provided [disambiguated syntax for candidates in E0034](https://github.com/rust-lang/rust/pull/38168).
* [@matklad](https://github.com/matklad) advertised [Vec in LinkedList docs](https://github.com/rust-lang/rust/pull/38297).
* [@birkenfeld](https://github.com/birkenfeld) updated [docs of slice get() and friends](https://github.com/rust-lang/rust/pull/38216).
* [@sourcefrog](https://github.com/sourcefrog) explained [the meaning of Result iters and link to factory functions](https://github.com/rust-lang/rust/pull/38158).
* [@tshepang](https://github.com/tshepang) fixed [a formatting nit in rustdoc](https://github.com/rust-lang/rust/pull/38395).
* [@wezm](https://github.com/wezm) simplified [notes on testing and concurrency](https://github.com/rust-lang/rust/pull/38013).
* [@jonhoo](https://github.com/jonhoo) expanded [E0309 explanation with motivating example](https://github.com/rust-lang/rust/pull/38315).
* [@federicomenaquintero](https://github.com/federicomenaquintero) documented [the optional extra arguments to assert_eq!() / assert_ne!()](https://github.com/rust-lang/rust/pull/38247).
* [@rkruppe](https://github.com/rkruppe) used [abort() over loop {} for panic in The Book](https://github.com/rust-lang/rust/pull/38138).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) improved [thread docs](https://github.com/rust-lang/rust/pull/38433), improved [unix socket doc](https://github.com/rust-lang/rust/pull/38236), improved [duration doc](https://github.com/rust-lang/rust/pull/38346) and improved [instant doc](https://github.com/rust-lang/rust/pull/38362).

# Recent doc contributions

* [@KiChjang](https://github.com/KiChjang) displayed [better error messages for E0282](https://github.com/rust-lang/rust/pull/38057).
* [@ollie27](https://github.com/ollie27) removed [broken src links from reexported items from macros in rustdoc](https://github.com/rust-lang/rust/pull/38264).
* [@Cobrand](https://github.com/Cobrand) improved [and fixed mpsc documentation](https://github.com/rust-lang/rust/pull/37941).
* [@sourcefrog](https://github.com/sourcefrog) avoided [using locally installed Source Code Pro font in rustdoc](https://github.com/rust-lang/rust/pull/38164).
* [@michael-zapata](https://github.com/michael-zapata) harmonised [rustdoc error messages](https://github.com/rust-lang/rust/pull/38179).
* [@brson](https://github.com/brson) updated [The Book for rustup](https://github.com/rust-lang/rust/pull/38122).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [more examples to UpdSocket](https://github.com/rust-lang/rust/pull/38067).

# Meetings

Next meeting will be on Wednesday 21st of December 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
