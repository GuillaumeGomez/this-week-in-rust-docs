---
layout: post
title: This Week in Rust Docs 14
date: 2016-07-25
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

A topic to propose crates for the Rust Doc Days has been created [here](https://users.rust-lang.org/t/call-for-proposals-for-next-rust-doc-days-crates/6685).

# Current opened issues

For now, here are the two big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They both need help to move forward so any contribution is very welcome!

There are currently around 50 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on github!

# Call for participation

There's now a call for participation to [display all methods of a type, even those from implicit traits in rustdoc](https://github.com/rust-lang/rust/issues/33772). This is a great way to help users find everything that a type can do. Any help on it would be very appreciated!

# Waiting for merge

* [@qolop](https://github.com/qolop) fixed [typo (privledge->privilege)](https://github.com/rust-lang/rust/pull/34941).
* [@jhod0](https://github.com/jhod0) added [diagnostics for rustc_metadata](https://github.com/rust-lang/rust/pull/34970).
* [@abhijeetbhagat](https://github.com/abhijeetbhagat) updated [underscore usage](https://github.com/rust-lang/rust/pull/34990) and updated [VecDeque documentation to specify direction of index 0](https://github.com/rust-lang/rust/pull/34974).
* [@rdwilliamson](https://github.com/rdwilliamson) fixed [HashMap's values_mut example to use println!](https://github.com/rust-lang/rust/pull/35001).
* [@nrc](https://github.com/nrc) simplified [rustdoc URLs](https://github.com/rust-lang/rust/pull/35020).
* [@durka](https://github.com/durka) documented [DoubleEndedIterator::next_back](https://github.com/rust-lang/rust/pull/34732).
* [@Manishearth](https://github.com/Manishearth) clarified [UnsafeCell docs](https://github.com/rust-lang/rust/pull/34520).
* [@estebank](https://github.com/estebank) added [a specific error message for missplaced doc comments](https://github.com/rust-lang/rust/pull/33922).
* [@ollie27](https://github.com/ollie27) removed [item types from some title pages from rustdoc](https://github.com/rust-lang/rust/pull/35003).
* [@frewsxcv](https://github.com/frewsxcv) rewrote/expanded [`slice::split` doc examples](https://github.com/rust-lang/rust/pull/35019).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [formatting generation for rustdoc code examples](https://github.com/rust-lang/rust/pull/35012), improved [`DirEntry` doc](https://github.com/rust-lang/rust/pull/35009), added [DirBuilder doc examples](https://github.com/rust-lang/rust/pull/34995), added [HashMap Entry enums examples](https://github.com/rust-lang/rust/pull/34935) and improved [`Open` doc](https://github.com/rust-lang/rust/pull/35010).

# Recent doc contributions

* [@mark-buer](https://github.com/mark-buer) removed [rustdoc reference to `walk_dir`](https://github.com/rust-lang/rust/pull/34895).
* [@wettowelreactor](https://github.com/wettowelreactor) fixed [some typos in char.rs](https://github.com/rust-lang/rust/pull/34977).
* [@frewsxcv](https://github.com/frewsxcv) rewrote/expanded [doc examples for `Vec::set_len`](https://github.com/rust-lang/rust/pull/34911), improved [doc examples for `slice::windows`](https://github.com/rust-lang/rust/pull/34988), added [doc examples for `Vec::{as_slice,as_mut_slice}`](https://github.com/rust-lang/rust/pull/34930), indicated [where `std::slice` structs originate from](https://github.com/rust-lang/rust/pull/34875) and partially [rewrote/expanded `Vec::truncate` documentation](https://github.com/rust-lang/rust/pull/34853).
* [@xitep](https://github.com/xitep) made [`.enumerate()` example self-explanatory](https://github.com/rust-lang/rust/pull/34880).
* [@shepmaster](https://github.com/shepmaster) improved [{String,Vec}::from_raw_parts documentation](https://github.com/rust-lang/rust/pull/34884).
 [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [Fix unwanted top margin for toggle wrapper in rustdoc CSS](https://github.com/rust-lang/rust/pull/34921), added [doc for btree_map types](https://github.com/rust-lang/rust/pull/34919), added [`BuildHasher` examples](https://github.com/rust-lang/rust/pull/34976), added [`RandomState` doc](https://github.com/rust-lang/rust/pull/34975), added [examples for VecDeque](https://github.com/rust-lang/rust/pull/34855) and added [examples for LinkedList](https://github.com/rust-lang/rust/pull/34854).

# Meetings

Next meeting will be on Wednesday 27th of July 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
