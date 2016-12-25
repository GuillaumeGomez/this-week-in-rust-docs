---
layout: post
title: This Week in Rust Docs 36
date: 2016-12-25
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

* [@frewsxcv](https://github.com/frewsxcv) clarified [behavior of `VecDeque::insert`](https://github.com/rust-lang/rust/pull/38581), clarified [phrasing of MSYS2 dependencies in README.md](https://github.com/rust-lang/rust/pull/38517), made [improvements to 'include' macro documentation](https://github.com/rust-lang/rust/pull/38457) and clarified [zero-value behavior of `ctlz`/`cttz` intrinsics](https://github.com/rust-lang/rust/pull/38310).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) improved [builder docs](https://github.com/rust-lang/rust/pull/38491), added [missing urls in Arc docs](https://github.com/rust-lang/rust/pull/38587), added [missing example for Thread struct](https://github.com/rust-lang/rust/pull/38548), added [ref suggestion](https://github.com/rust-lang/rust/pull/37658), improved [instant doc](https://github.com/rust-lang/rust/pull/38362), added [information in case of markdown block code test failure](https://github.com/rust-lang/rust/pull/36320) and fixed [invalid module suggestion](https://github.com/rust-lang/rust/pull/38255).
* [@estebank](https://github.com/estebank) escaped [the deprecated and unstable reason text in rustdoc](https://github.com/rust-lang/rust/pull/38244).
* [@nagisa](https://github.com/nagisa) expanded [documentation of process::exit and exec](https://github.com/rust-lang/rust/pull/38518).
* [@rkruppe](https://github.com/rkruppe) used [abort() over loop {} for panic in The Book](https://github.com/rust-lang/rust/pull/38138).
* [@chris-morgan](https://github.com/chris-morgan) fixed [rustdoc highlighting of `&` and `*`](https://github.com/rust-lang/rust/pull/38569).
* [@ollie27](https://github.com/ollie27) fixed [invalid HTML in stability notices in rustdoc](https://github.com/rust-lang/rust/pull/38329).
* [@linclark](https://github.com/linclark) added [error explanation for E0328.](https://github.com/rust-lang/rust/pull/38108).
* [@chriskrycho](https://github.com/chriskrycho) documented [RFC 1623: static lifetime elision.](https://github.com/rust-lang/rust/pull/37928).
* [@federicomenaquintero](https://github.com/federicomenaquintero) documented [the optional extra arguments to assert_eq!() / assert_ne!()](https://github.com/rust-lang/rust/pull/38247).

# Recent doc contributions

* [@frewsxcv](https://github.com/frewsxcv) improved [the API examples for `std::fs::File`](https://github.com/rust-lang/rust/pull/38443), documented [platform-specific differences for `std::process::exit`](https://github.com/rust-lang/rust/pull/38397), improved [documentation for `core::hash::BuildHasherDefault`](https://github.com/rust-lang/rust/pull/38334), improved [`BTreeSet` documentation](https://github.com/rust-lang/rust/pull/38208) and implement [`fmt::Debug` for all structures in libstd.](https://github.com/rust-lang/rust/pull/38006).
* [@brson](https://github.com/brson) wrote [the 1.14 release notes](https://github.com/rust-lang/rust/pull/38427).
* [@ollie27](https://github.com/ollie27) fixed [short summaries in search results in rustdoc](https://github.com/rust-lang/rust/pull/38330).
* [@estebank](https://github.com/estebank) pointed out [the known type when field doesn't satisfy bound](https://github.com/rust-lang/rust/pull/38150) and explained [why/when `.lines()` returns an error](https://github.com/rust-lang/rust/pull/38505).
* [@matklad](https://github.com/matklad) advertised [Vec in LinkedList docs](https://github.com/rust-lang/rust/pull/38297).
* [@sourcefrog](https://github.com/sourcefrog) explained [the meaning of Result iters and link to factory functions](https://github.com/rust-lang/rust/pull/38158).
* [@tshepang](https://github.com/tshepang) fixed [a formatting nit in rustdoc](https://github.com/rust-lang/rust/pull/38395).
* [@wezm](https://github.com/wezm) simplified [notes on testing and concurrency](https://github.com/rust-lang/rust/pull/38013).
* [@jonhoo](https://github.com/jonhoo) expanded [E0309 explanation with motivating example](https://github.com/rust-lang/rust/pull/38315).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) improved [thread docs](https://github.com/rust-lang/rust/pull/38433), improved [unix socket doc](https://github.com/rust-lang/rust/pull/38236), improved [duration doc](https://github.com/rust-lang/rust/pull/38346), added [JoinHandle missing examples](https://github.com/rust-lang/rust/pull/38572), added [missing examples in some thread functions](https://github.com/rust-lang/rust/pull/38513) and added [cast suggestions](https://github.com/rust-lang/rust/pull/38099).
* [@DirkyJerky](https://github.com/DirkyJerky) created [hyperlink to correct documentation](https://github.com/rust-lang/rust/pull/38554).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) properly calculated [line length for where clauses](https://github.com/rust-lang/rust/pull/38497).
* [@clarcharr](https://github.com/clarcharr) removed [@import normalize.css](https://github.com/rust-lang/rust/pull/38480).
* [@stjepang](https://github.com/stjepang) made [a minor fix in the merge_sort comments](https://github.com/rust-lang/rust/pull/38432).

# Meetings

Next meeting will be on Wednesday 28th of December 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
