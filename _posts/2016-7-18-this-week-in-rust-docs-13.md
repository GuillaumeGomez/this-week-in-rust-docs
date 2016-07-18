---
layout: post
title: This Week in Rust Docs 13
date: 2016-07-18
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

The ["More api documentation conventions" RFC](https://github.com/rust-lang/rfcs/pull/1574) has been merged!

# Current opened issues

For now, here are the two big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They both need help to move forward so any contribution is very welcome!

There are currently around 50 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on github!

# Call for participation

There's now a call for participation to [display all methods of a type, even those from implicit traits in rustdoc](https://github.com/rust-lang/rust/issues/33772). This is a great way to help users find everything that a type can do. Any help on it would be very appreciated!

# Waiting for merge

* [@durka](https://github.com/durka) documented [DoubleEndedIterator::next_back](https://github.com/rust-lang/rust/pull/34732).
* [@shepmaster](https://github.com/shepmaster) improved [{String,Vec}::from_raw_parts documentation](https://github.com/rust-lang/rust/pull/34884).
* [@xitep](https://github.com/xitep) made [`.enumerate()` example self-explanatory](https://github.com/rust-lang/rust/pull/34880).
* [@frewsxcv](https://github.com/frewsxcv) indicated [where `std::slice` structs originate from](https://github.com/rust-lang/rust/pull/34875) and partially [rewrote/expanded `Vec::truncate` documentation](https://github.com/rust-lang/rust/pull/34853).
* [@Manishearth](https://github.com/Manishearth) clarified [UnsafeCell docs](https://github.com/rust-lang/rust/pull/34520).
* [@estebank](https://github.com/estebank) added [a specific error message for missplaced doc comments](https://github.com/rust-lang/rust/pull/33922).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [examples for VecDeque](https://github.com/rust-lang/rust/pull/34855) and added [examples for LinkedList](https://github.com/rust-lang/rust/pull/34854).

# Recent doc contributions

* [@ollie27](https://github.com/ollie27) fixed [methods in seach results in rustdoc](https://github.com/rust-lang/rust/pull/34752).
* [@alexandermerritt](https://github.com/alexandermerritt) made [docs for `clone_from_slice` consistent with `copy_from_slice`](https://github.com/rust-lang/rust/pull/34745).
* [@izgzhen](https://github.com/izgzhen) improved [arc doc](https://github.com/rust-lang/rust/pull/34733).
* [@davidko](https://github.com/davidko) fixed [a few typos in The Book](https://github.com/rust-lang/rust/pull/34770).
* [@glandium](https://github.com/glandium) added [a mention to the fact that writeln! and println! always use LF](https://github.com/rust-lang/rust/pull/34777).
* [@wuranbo](https://github.com/wuranbo) fixed [ffi referenced rust-snappy which couldn't compile](https://github.com/rust-lang/rust/pull/34799).
* [@frewsxcv](https://github.com/frewsxcv) added [where `std::vec` structs originate from](https://github.com/rust-lang/rust/pull/34818), made [various `std::process` doc](https://github.com/rust-lang/rust/pull/34737) and added [doc example for `std::process::ExitStatus::success`](https://github.com/rust-lang/rust/pull/34794).
* [@steveklabnik](https://github.com/steveklabnik) fixed up [documentation around no_std](https://github.com/rust-lang/rust/pull/34838).
* [@tshepang](https://github.com/tshepang) made a few doc [fixes](https://github.com/rust-lang/rust/pulls?utf8=%E2%9C%93&q=is%3Apr%20is%3Aclosed%2034849%2034848).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [examples for FpCategory](https://github.com/rust-lang/rust/pull/34804) and added [libsyntax error code explanations](https://github.com/rust-lang/rust/pull/34637).

# Meetings

Next meeting will be on Wednesday 20th of July 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
