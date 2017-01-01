---
layout: post
title: This Week in Rust Docs 37
date: 2017-1-1
---

Hello and welcome to *This Week in Rust Docs* and happy new year!

*This Week in Rust Docs* is openly developed [on GitHub](https://github.com/GuillaumeGomez/this-week-in-rust-docs).
If you find any errors in this week's issue, [please submit a PR](https://github.com/GuillaumeGomez/this-week-in-rust-docs/pulls).

And of course, don't forget to look at the docs:

* [Stable](https://doc.rust-lang.org/)
* [Beta](http://doc.rust-lang.org/beta/)
* [Nightly](http://doc.rust-lang.org/nightly/)

This week's edition was edited by [Guillaume Gomez](https://github.com/GuillaumeGomez).

# Latest news

Please take a look [to the next rust doc days planning reminder](https://users.rust-lang.org/t/reminder-planning-the-next-rust-doc-days/6901).

The topic to propose crates for the Rust Doc Days is still open and waiting for contributions [here](https://users.rust-lang.org/t/call-for-proposals-for-next-rust-doc-days-crates/6685). Please take a look!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on GitHub!

# Waiting for merge

* [@brson](https://github.com/brson) removed [all "consider using an explicit lifetime parameter" suggestions](https://github.com/rust-lang/rust/pull/37057).
* [@estebank](https://github.com/estebank) suggested [solutions for `fn foo(&foo: Foo)`](https://github.com/rust-lang/rust/pull/38605), escaped [the deprecated and unstable reason text in rustdoc](https://github.com/rust-lang/rust/pull/38244), disambiguated [Implementors when the type name is not unique in rustdoc](https://github.com/rust-lang/rust/pull/38414) and provide [disambiguated syntax for candidates in E0034](https://github.com/rust-lang/rust/pull/38168).
* [@frewsxcv](https://github.com/frewsxcv) clarified [behavior of `VecDeque::insert`](https://github.com/rust-lang/rust/pull/38581), made [improvements to 'include' macro documentation](https://github.com/rust-lang/rust/pull/38457) and clarified [zero-value behavior of `ctlz`/`cttz` intrinsics](https://github.com/rust-lang/rust/pull/38310).
* [@bombless](https://github.com/bombless) fixed [doc for `escape_debug`](https://github.com/rust-lang/rust/pull/38629).
* [@nagisa](https://github.com/nagisa) expanded [documentation of process::exit and exec](https://github.com/rust-lang/rust/pull/38518).
* [@rkruppe](https://github.com/rkruppe) replaced [loop {} with abort() for panic in The Book](https://github.com/rust-lang/rust/pull/38138).
* [@chris-morgan](https://github.com/chris-morgan) fixed [rustdoc highlighting of `&` and `*`](https://github.com/rust-lang/rust/pull/38569).
* [@linclark](https://github.com/linclark) added [error explanation for E0328](https://github.com/rust-lang/rust/pull/38108).
* [@birkenfeld](https://github.com/birkenfeld) update [docs of slice get() and friends](https://github.com/rust-lang/rust/pull/38216).
* [@federicomenaquintero](https://github.com/federicomenaquintero) documented [the optional extra arguments to assert_eq!() / assert_ne!()](https://github.com/rust-lang/rust/pull/38247).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [ref suggestion](https://github.com/rust-lang/rust/pull/37658), added [missing example for Thread struct](https://github.com/rust-lang/rust/pull/38548), added [Instant doc](https://github.com/rust-lang/rust/pull/38362), added [information in case of markdown block code test failure in rustdoc](https://github.com/rust-lang/rust/pull/36320) and fixed [invalid module suggestion](https://github.com/rust-lang/rust/pull/38255).

# Recent doc contributions

* [@frewsxcv](https://github.com/frewsxcv) clarified [phrasing of MSYS2 dependencies in README.md](https://github.com/rust-lang/rust/pull/38517) and documented [foreign variadic functions in TRPL and the reference.](https://github.com/rust-lang/rust/pull/38630).
* [@ollie27](https://github.com/ollie27) fixed [invalid HTML in stability notices in rustdoc](https://github.com/rust-lang/rust/pull/38329) and fixed [broken CSS for trait items in rustdoc](https://github.com/rust-lang/rust/pull/38671).
* [@programble](https://github.com/programble) added [links to methods on all slice iterator struct docs](https://github.com/rust-lang/rust/pull/38711).
* [@jseyfried](https://github.com/jseyfried) fixed [internal compiler error (ICE) in rustdoc](https://github.com/rust-lang/rust/pull/38537).
* [@lucis-fluxum](https://github.com/lucis-fluxum) fixed [typo in PartialOrd docs](https://github.com/rust-lang/rust/pull/38693).
* [@agl](https://github.com/agl) added ["an" before "i32"](https://github.com/rust-lang/rust/pull/38662) and add [missing apostrophe.](https://github.com/rust-lang/rust/pull/38659).
* [@kellerkindt](https://github.com/kellerkindt) and suddenly [a german word :O](https://github.com/rust-lang/rust/pull/38628).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) improved [builder docs](https://github.com/rust-lang/rust/pull/38491), added [missing urls in Arc docs](https://github.com/rust-lang/rust/pull/38587), add [missing urls in AtomicBool docs](https://github.com/rust-lang/rust/pull/38611), added [missing urls for AtomicPtr](https://github.com/rust-lang/rust/pull/38635), added [missing urls for atomic_int macros types](https://github.com/rust-lang/rust/pull/38649) and added [missing urls for atomic fn docs](https://github.com/rust-lang/rust/pull/38674).

# Meetings

Next meeting will be on Wednesday 4th of January 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
