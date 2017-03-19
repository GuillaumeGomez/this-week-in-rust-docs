---
layout: post
title: This Week in Rust Docs 48
date: 2017-3-19
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
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing urls and small nits](https://github.com/rust-lang/rust/pull/39513), fixed [invalid module suggestion](https://github.com/rust-lang/rust/pull/38255), added [ref suggestion](https://github.com/rust-lang/rust/pull/37658) and replaced [hoedown with pulldown in rustdoc](https://github.com/rust-lang/rust/pull/40338).

# Recent doc contributions

* [@frewsxcv](https://github.com/frewsxcv) added [basic documentation/examples for six unstable features](https://github.com/rust-lang/rust/pull/40452), made [a few improvements to the `core::hash` top-level docs](https://github.com/rust-lang/rust/pull/40505), added [doc examples for `OsStr`, `OsString`](https://github.com/rust-lang/rust/pull/40458), removed [function invokation parens from documentation links](https://github.com/rust-lang/rust/pull/40456) and updated [usages of 'OSX' (and other old names) to 'macOS'](https://github.com/rust-lang/rust/pull/40457).
* [@tschottdorf](https://github.com/tschottdorf) improved [wording in the -{W,A,F,D} options](https://github.com/rust-lang/rust/pull/40453).
* [@projektir](https://github.com/projektir) using [X headings #39850](https://github.com/rust-lang/rust/pull/40496), removed [doc about highlighting code in other languages #40301](https://github.com/rust-lang/rust/pull/40466) and updated [README.md to point to the correct doc location](https://github.com/rust-lang/rust/pull/40467).
* [@tshepang](https://github.com/tshepang) fixed some [style issues](https://github.com/rust-lang/rust/pull/40463).
* [@llogiq](https://github.com/llogiq) fixed [grammar format](https://github.com/rust-lang/rust/pull/40495).
* [@steveklabnik](https://github.com/steveklabnik) added [sort_unstable to unstable book](https://github.com/rust-lang/rust/pull/40586), linked [core::slice to std::slice](https://github.com/rust-lang/rust/pull/40520) and removed [incorrect feature from the 1.16 relnotes](https://github.com/rust-lang/rust/pull/40517).
* [@kevinmehall](https://github.com/kevinmehall) fixed [documentation for Vec::dedup_by.](https://github.com/rust-lang/rust/pull/40536).
* [@ericfindlay](https://github.com/ericfindlay) corrected [very minor documentation detail about Unicode and Japanese](https://github.com/rust-lang/rust/pull/40499).
* [@wesleywiser](https://github.com/wesleywiser) fixed [sidebar not extending to the bottom of the page](https://github.com/rust-lang/rust/pull/40497).
* [@tbu-](https://github.com/tbu-) reworded [the non-dropping of `src` for `ptr::write{,_unaligned}`](https://github.com/rust-lang/rust/pull/40387).
* [@brson](https://github.com/brson) made [docs required again](https://github.com/rust-lang/rust/pull/40526).

# Meetings

Next meeting will be on Wednesday 22nd of March 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
