---
layout: post
title: This Week in Rust Docs 15
date: 2016-08-01
---

Hello and welcome to *This Week in Rust Docs*!

*This Week in Rust Docs* is openly developed [on GitHub](https://github.com/GuillaumeGomez/this-week-in-rust-docs).
If you find any errors in this week's issue, [please submit a PR](https://github.com/GuillaumeGomez/this-week-in-rust-docs/pulls).

And of course, don't forget to look at the docs:

* [Stable](https://doc.rust-lang.org/)
* [Beta](http://doc.rust-lang.org/beta/)
* [Nightly](http://doc.rust-lang.org/nightly/)

This week's edition was edited by: [GuillaumeGomez](https://github.com/GuillaumeGomez).

# Latest news

A topic to propose crates for the Rust Doc Days has been created [here](https://users.rust-lang.org/t/call-for-proposals-for-next-rust-doc-days-crates/6685). Please take a look!

# Current opened issues

For now, here are the two big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They both need help to move forward so any contribution is very welcome!

There are currently around 50 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on github!

# Call for participation

There's now a call for participation to [display all methods of a type, even those from implicit traits in rustdoc](https://github.com/rust-lang/rust/issues/33772). This is a great way to help users find everything that a type can do. Any help on it would be very appreciated!

# Waiting for merge

* [@frewsxcv](https://github.com/frewsxcv) added [doc examples for `range::RangeArgument::{start,end}`](https://github.com/rust-lang/rust/pull/35041) and rewrote [`slice::chunks` doc example to not require printing](https://github.com/rust-lang/rust/pull/35134).
* [@jongiddy](https://github.com/jongiddy) provide [a more explicit example of wildcard version in guessing game doc](https://github.com/rust-lang/rust/pull/35137).
* [@qolop](https://github.com/qolop) fixed [typo (privledge->privilege)](https://github.com/rust-lang/rust/pull/34941).
* [@jhod0](https://github.com/jhod0) added [diagnostics for rustc_metadata](https://github.com/rust-lang/rust/pull/34970).
* [@nrc](https://github.com/nrc) simplified [rustdoc URLs](https://github.com/rust-lang/rust/pull/35020).
* [@Manishearth](https://github.com/Manishearth) clarified [UnsafeCell docs](https://github.com/rust-lang/rust/pull/34520).
* [@estebank](https://github.com/estebank) added [a specific error message for misplaced doc comments](https://github.com/rust-lang/rust/pull/33922).
* [@ollie27](https://github.com/ollie27) removed [item types from some title pages from rustdoc](https://github.com/rust-lang/rust/pull/35003).
* [@steveklabnik](https://github.com/steveklabnik) made it clear that [the reference isn't normative](https://github.com/rust-lang/rust/pull/35102).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [doc examples for FileType struct](https://github.com/rust-lang/rust/pull/35076), added [`io::Error` doc examples](https://github.com/rust-lang/rust/pull/35109) and fixed [formatting generation for rustdoc code examples](https://github.com/rust-lang/rust/pull/35012).

# Recent doc contributions

* [@knight42](https://github.com/knight42) added [more intuitive explanation of strings formatting](https://github.com/rust-lang/rust/pull/35050).
* [@munyari](https://github.com/munyari) added [docs for assert! and debug_assert!](https://github.com/rust-lang/rust/pull/35072).
* [@vadimcn](https://github.com/vadimcn) fixed [typos](https://github.com/rust-lang/rust/pull/35066).
* [@rdwilliamson](https://github.com/rdwilliamson) fixed [HashMap's values_mut example to use println!](https://github.com/rust-lang/rust/pull/35001).
* [@abhijeetbhagat](https://github.com/abhijeetbhagat) updated [underscore usage](https://github.com/rust-lang/rust/pull/34990) and updated [VecDeque documentation to specify direction of index 0](https://github.com/rust-lang/rust/pull/34974).
* [@durka](https://github.com/durka) documented [DoubleEndedIterator::next_back](https://github.com/rust-lang/rust/pull/34732).
* [@frewsxcv](https://github.com/frewsxcv) rewrote/expanded [`slice::split` doc examples](https://github.com/rust-lang/rust/pull/35019).
* [@frewsxcv](https://github.com/frewsxcv) rewrote [`collections::LinkedList::append` doc example](https://github.com/rust-lang/rust/pull/35104) and added [documentation example for `str::Chars::as_str`](https://github.com/rust-lang/rust/pull/35062).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [`std::fs` docs](https://github.com/rust-lang/rust/pull/35087), improved [`DirEntry` doc](https://github.com/rust-lang/rust/pull/35009), added [HashMap Entry enums examples](https://github.com/rust-lang/rust/pull/34935), improved [`Open` doc](https://github.com/rust-lang/rust/pull/35010) and added [DirBuilder doc examples](https://github.com/rust-lang/rust/pull/34995).

# Meetings

Next meeting will be on Wednesday 3rd of August 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
