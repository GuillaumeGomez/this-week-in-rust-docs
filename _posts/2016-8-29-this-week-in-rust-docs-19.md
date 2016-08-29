---
layout: post
title: This Week in Rust Docs 19
date: 2016-08-29
---

Hello and welcome to *This Week in Rust Docs*!

*This Week in Rust Docs* is openly developed [on GitHub](https://github.com/GuillaumeGomez/this-week-in-rust-docs).
If you find any errors in this week's issue, [please submit a PR](https://github.com/GuillaumeGomez/this-week-in-rust-docs/pulls).

And of course, don't forget to look at the docs:

* [Stable](https://doc.rust-lang.org/)
* [Beta](http://doc.rust-lang.org/beta/)
* [Nightly](http://doc.rust-lang.org/nightly/)

This week's edition was edited by: [GuillaumeGomez](https://github.com/GuillaumeGomez).

# Latest news (getting a bit old but still gold!)

Please take a look [to the next rust doc days planning reminder](https://users.rust-lang.org/t/reminder-planning-the-next-rust-doc-days/6901).

The topic to propose crates for the Rust Doc Days is still open and waiting for contributions [here](https://users.rust-lang.org/t/call-for-proposals-for-next-rust-doc-days-crates/6685). Please take a look!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [Error code list which need to be updated to new format](https://github.com/rust-lang/rust/issues/35233)
* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 50 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on github!

# Call for participation

There's now a call for participation to [display all methods of a type, even those from implicit traits in rustdoc](https://github.com/rust-lang/rust/issues/33772). This is a great way to help users find everything that a type can do. Any help on it would be very appreciated!

# Waiting for merge

* [@matthew-piziak](https://github.com/matthew-piziak) improved [documentation for `Fn*` traits](https://github.com/rust-lang/rust/pull/35810), demonstrated that [`RHS != Self` use cases for `Add` and `Sub`](https://github.com/rust-lang/rust/pull/35793), added [evocative examples for `Shl` and `Shr`](https://github.com/rust-lang/rust/pull/35863), added [links to interesting items in `std::ptr` documentation ](https://github.com/rust-lang/rust/pull/35880) and added [a panic example to std::from_utf8_unchecked](https://github.com/rust-lang/rust/pull/35890).
* [@F001](https://github.com/F001) fixed [documentation in cell mod](https://github.com/rust-lang/rust/pull/35895).
* [@frewsxcv](https://github.com/frewsxcv) indicated [where `core::result::IntoIter` is created](https://github.com/rust-lang/rust/pull/35845).
* [@Stebalien](https://github.com/Stebalien) clarified/fixed [formatting docs concerning fmt::Result/fmt::Error](https://github.com/rust-lang/rust/pull/35862).
* [@steveklabnik](https://github.com/steveklabnik) made it clear that [the reference isn't normative](https://github.com/rust-lang/rust/pull/35102).
* [@ollie27](https://github.com/ollie27) fixed [associated consts in search results in rustdoc](https://github.com/rust-lang/rust/pull/36078).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing urls into convert module](https://github.com/rust-lang/rust/pull/36083), improved [Path and PathBuf docs](https://github.com/rust-lang/rust/pull/35786) and fixed [formatting generation for rustdoc code examples](https://github.com/rust-lang/rust/pull/35012).


# Recent doc contributions

This week (too), I'll split between the [new error code format](https://github.com/rust-lang/rust/issues/35233) contributions and the others. Let's start by the first one:

* [@crypto-universe](https://github.com/crypto-universe): [E0426](https://github.com/rust-lang/rust/pull/35835), [E0426](https://github.com/rust-lang/rust/pull/35835)
* [@mikhail-m1](https://github.com/mikhail-m1): [E0450](https://github.com/rust-lang/rust/pull/36044)
* [@0xmohit](https://github.com/0xmohit): [E0453](https://github.com/rust-lang/rust/pull/35989), [E0277](https://github.com/rust-lang/rust/pull/35985), [E0445 and E0454](https://github.com/rust-lang/rust/pull/35961)
* [@creativcoder](https://github.com/creativcoder): [E0195](https://github.com/rust-lang/rust/pull/35939)
* [@shyaamsundhar](https://github.com/shyaamsundhar): [E0435, E0437 and E0438](https://github.com/rust-lang/rust/pull/35858)
* [@kyrias](https://github.com/kyrias): [E0424](https://github.com/rust-lang/rust/pull/35841)

Others contributions:

* [@matthew-piziak](https://github.com/matthew-piziak) replaced [`Div` example with something more evocative of division](https://github.com/rust-lang/rust/pull/35936), added [example for `Rc::would_unwrap`](https://github.com/rust-lang/rust/pull/35881), replaced [`println!` statements with `assert!`ions in `std::ptr` examples](https://github.com/rust-lang/rust/pull/35878), added [more evocative examples for `Sub` and `SubAssign`](https://github.com/rust-lang/rust/pull/35876), replaced [`Index` example with something more evocative of indexing](https://github.com/rust-lang/rust/pull/35864), replaced [`Rem` example with something more evocative](https://github.com/rust-lang/rust/pull/35861), replaced [`Mul` example with something more evocative of multiplication](https://github.com/rust-lang/rust/pull/35860), replaced [`BitAnd` example with something more evocative of bitwise AND](https://github.com/rust-lang/rust/pull/35809)
* [@estebank](https://github.com/estebank) added [a specific error message for misplaced doc comments](https://github.com/rust-lang/rust/pull/33922).
* [@frewsxcv](https://github.com/frewsxcv) made [various refactorings in the rustdoc module](https://github.com/rust-lang/rust/pull/35867).
* [@CryZe](https://github.com/CryZe) fixed ["Furthermore" Typo in String Docs](https://github.com/rust-lang/rust/pull/35879).
* [@alevy](https://github.com/alevy) fixed [a minor typo in CONTRIBUTING.md](https://github.com/rust-lang/rust/pull/35889).
* [@munyari](https://github.com/munyari) added [reference to `Self` in traits chapter in The Book](https://github.com/rust-lang/rust/pull/35891).
* [@kyrias](https://github.com/kyrias) improved [E0094 underline](https://github.com/rust-lang/rust/pull/35980).
* [@tshepang](https://github.com/tshepang) added [trailing commas](https://github.com/rust-lang/rust/pull/35948).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added new error code tests[here](https://github.com/rust-lang/rust/pull/36003) and [here](https://github.com/rust-lang/rust/pull/35920).

# Meetings

Next meeting will be on Wednesday 31st of August 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
