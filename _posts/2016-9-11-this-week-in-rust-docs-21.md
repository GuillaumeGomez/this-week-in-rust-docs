---
layout: post
title: This Week in Rust Docs 21
date: 2016-09-11
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

In the last meetup, we discussed about the possibilty to "expand" examples in the doc in order to show the full code. The goal is to prevent issues from copy/paste where `try`/`?` are used.

Another thing was that it should be more obvious that the code examples could actually be run online. To this issue, a PR has already be opened [here](https://github.com/rust-lang/rust/pull/36334).

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

* [@athulappadan](https://github.com/athulappadan) added [Documentation about what Default does for each type](https://github.com/rust-lang/rust/pull/36396).
* [@EdorianDark](https://github.com/EdorianDark) inserted [examples with universal function call syntax](https://github.com/rust-lang/rust/pull/36248).
* [@liigo](https://github.com/liigo) removed [the `docblock-short` collapse](https://github.com/rust-lang/rust/pull/36293).
* [@kylog](https://github.com/kylog) fixed [a typo in The Book](https://github.com/rust-lang/rust/pull/36380).
* [@dangcheng](https://github.com/dangcheng) fixed [a mistake (File::open -> File::create) in The Book](https://github.com/rust-lang/rust/pull/36374).
* [@frewsxcv](https://github.com/frewsxcv) added [basic doc example for `std::panic::set_hook`](https://github.com/rust-lang/rust/pull/36390).
* [@c4rlo](https://github.com/c4rlo) fixed [a "\\" in a table heading to be "/"](https://github.com/rust-lang/rust/pull/36204).
* [@matthew-piziak](https://github.com/matthew-piziak) added [links to interesting items in `std::ptr` documentation](https://github.com/rust-lang/rust/pull/35880) and [refactored range examples](https://github.com/rust-lang/rust/pull/35759), added [`default` docstrings for `String`, `AtomicBool`, and `Generics`](https://github.com/rust-lang/rust/pull/36364) and updated [docstrings for `mem::update` and `mem::swap`](https://github.com/rust-lang/rust/pull/36366).
* [@steveklabnik](https://github.com/steveklabnik) made it clear that [reference isn't normative](https://github.com/rust-lang/rust/pull/35102).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [metadata diagnostics](https://github.com/rust-lang/rust/pull/36102), added [urls when they were needed](https://github.com/rust-lang/rust/pull/36363), fixed [formatting generation for rustdoc code examples](https://github.com/rust-lang/rust/pull/35012) and set [run button transparent instead of invisible](https://github.com/rust-lang/rust/pull/36334).


# Recent doc contributions

This week (too), I'll split between the [new error code format](https://github.com/rust-lang/rust/issues/35233) contributions and the others. Let's start by the first one:

* [@Cobrand](https://github.com/Cobrand): [E0559](https://github.com/rust-lang/rust/pull/36267)
* [@abhiQmar](https://github.com/abhiQmar): [E0558](https://github.com/rust-lang/rust/pull/36223)
* [@razielgn](https://github.com/razielgn): [E0493](https://github.com/rust-lang/rust/pull/36212)
* [@EugeneGonzalez](https://github.com/EugeneGonzalez): [E0529](https://github.com/rust-lang/rust/pull/36210)

Other contributions:

* [@JDemler](https://github.com/JDemler) fixed [typo in nomicon](https://github.com/rust-lang/rust/pull/36326).
* [@fanzier](https://github.com/fanzier) fixed [typo in PartialOrd docs](https://github.com/rust-lang/rust/pull/36165).
* [@johnthagen](https://github.com/johnthagen) updated [nightly docs supported Windows versions to match Getting Started page](https://github.com/rust-lang/rust/pull/36225).
* [@Sawyer47](https://github.com/Sawyer47) removed [incorrect methods inherited through Deref by filtering them](https://github.com/rust-lang/rust/pull/36266).
* [@tshepang](https://github.com/tshepang) fixed [doc coercion](https://github.com/rust-lang/rust/pull/36314).
* [@frewsxcv](https://github.com/frewsxcv) indicated [where `core::result::IntoIter` is created](https://github.com/rust-lang/rust/pull/35845) and added [doc example for `std::time::Instant::elapsed`](https://github.com/rust-lang/rust/pull/36311).
* [@ollie27](https://github.com/ollie27) fixed [associated consts in search results](https://github.com/rust-lang/rust/pull/36078).
* [@Cobrand](https://github.com/Cobrand) added [mention of `make tidy`](https://github.com/rust-lang/rust/pull/36241) and added [mention of `make tidy` into contributing.md file](https://github.com/rust-lang/rust/pull/36241).
* [@apasel422](https://github.com/apasel422) cleaned up [thread-local storage docs](https://github.com/rust-lang/rust/pull/36263).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing urls](https://github.com/rust-lang/rust/pull/36243), added [new error code tests](https://github.com/rust-lang/rust/pull/36141), added missing urls [here](https://github.com/rust-lang/rust/pull/36298) and [here](https://github.com/rust-lang/rust/pull/36243).

# Meetings

Next meeting will be on Wednesday 14th of September 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
