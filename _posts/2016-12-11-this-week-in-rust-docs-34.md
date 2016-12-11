---
layout: post
title: This Week in Rust Docs 34
date: 2016-12-11
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

Since new rustc version is out, the controversial changes on docs have been merged:

 * Fold [fields for enum struct variants into a docblock in rustdoc](https://github.com/rust-lang/rust/pull/37728)
 * Add [line breaks to where clauses a la rustfmt in rustdoc](https://github.com/rust-lang/rust/pull/37190).
 * Print [more tags in rustdoc](https://github.com/rust-lang/rust/pull/37134).

Don't hesitate to give your feedbacks on them!


The way rustdoc is creating urls is problematic for the moment. A good summary of this issue can be found [here](https://github.com/rust-lang/rust/issues/36417). A few members of the Rust Doc team are preparing an RFC in order to improve this. If you want to get involved, feel free to speak about it with [Guillaume Gomez](https://github.com/GuillaumeGomez) (imperio on IRC).

Please take a look [to the next rust doc days planning reminder](https://users.rust-lang.org/t/reminder-planning-the-next-rust-doc-days/6901).

The topic to propose crates for the Rust Doc Days is still open and waiting for contributions [here](https://users.rust-lang.org/t/call-for-proposals-for-next-rust-doc-days-crates/6685). Please take a look!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on GitHub!

# Call for participation

There's now a call for participation to [display all methods of a type, even those from implicit traits in rustdoc](https://github.com/rust-lang/rust/issues/33772). This is a great way to help users find everything that a type can do. Any help on it would be very appreciated!

# Waiting for merge

* [@matklad](https://github.com/matklad) advertised [Vec in LinkedList docs](https://github.com/rust-lang/rust/pull/38297).
* [@birkenfeld](https://github.com/birkenfeld) updated [docs of slice get() and friends](https://github.com/rust-lang/rust/pull/38216).
* [@KiChjang](https://github.com/KiChjang) displayed [better error messages for E0282](https://github.com/rust-lang/rust/pull/38057).
* [@liigo](https://github.com/liigo) made a [minor fix about visibility in reference](https://github.com/rust-lang/rust/pull/38215).
* [@estebank](https://github.com/estebank) escaped [ the deprecated and unstable reason text in rustdoc](https://github.com/rust-lang/rust/pull/38244), pointed [out the known type when field doesn't satisfy bound](https://github.com/rust-lang/rust/pull/38150), provided [disambiguated syntax for candidates in E0034](https://github.com/rust-lang/rust/pull/38168) and showed [span for trait that doesn't implement Copy](https://github.com/rust-lang/rust/pull/37493).
* [@federicomenaquintero](https://github.com/federicomenaquintero) documented [the optional extra arguments to assert_eq!() / assert_ne!()](https://github.com/rust-lang/rust/pull/38247).
* [@durka](https://github.com/durka) fixed [doctests with non-feature crate attrs in rustdoc](https://github.com/rust-lang/rust/pull/38161).
* [@ollie27](https://github.com/ollie27) removed [broken src links from reexported items from macros in rustdoc](https://github.com/rust-lang/rust/pull/38264).
* [@frewsxcv](https://github.com/frewsxcv) improved [`BTreeSet` documentation](https://github.com/rust-lang/rust/pull/38208) and implemented [`fmt::Debug` for all structures in libstd](https://github.com/rust-lang/rust/pull/38006).
* [@rkruppe](https://github.com/rkruppe) used [abort() over loop {} for panic in the Book](https://github.com/rust-lang/rust/pull/38138).
* [@Cobrand](https://github.com/Cobrand) improved [and fixed mpsc documentation](https://github.com/rust-lang/rust/pull/37941).
* [@sourcefrog](https://github.com/sourcefrog) explained [meaning of Result iters and link to factory functions](https://github.com/rust-lang/rust/pull/38158) and avoided [using locally installed Source Code Pro font (fixes #24355).](https://github.com/rust-lang/rust/pull/38164).
* [@michael-zapata](https://github.com/michael-zapata) harmonised [rustdoc error messages](https://github.com/rust-lang/rust/pull/38179).
* [@wezm](https://github.com/wezm) simplified [notes on testing and concurrency](https://github.com/rust-lang/rust/pull/38013).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) improved [unix socket doc](https://github.com/rust-lang/rust/pull/38236), added [cast suggestions](https://github.com/rust-lang/rust/pull/38099), fix [invalid module suggestion](https://github.com/rust-lang/rust/pull/38255), added [more examples to UpdSocket](https://github.com/rust-lang/rust/pull/38067) and added [ref suggestion](https://github.com/rust-lang/rust/pull/37658).

# Recent doc contributions

* [@estebank](https://github.com/estebank) showed [`Trait` instead of `<Struct as Trait>` in E0323](https://github.com/rust-lang/rust/pull/38065).
* [@jonathandturner](https://github.com/jonathandturner) pointed [arg num mismatch errors back to their definition](https://github.com/rust-lang/rust/pull/38121).
* [@ollie27](https://github.com/ollie27) added [sort lines in search index and implementors js in rustdoc](https://github.com/rust-lang/rust/pull/38105).
* [@Cobrand](https://github.com/Cobrand) updated [book/ffi to use catch_unwind](https://github.com/rust-lang/rust/pull/38225).
* [@frewsxcv](https://github.com/frewsxcv) added [docs for last undocumented `Default` `impl`.](https://github.com/rust-lang/rust/pull/38186).
* [@durka](https://github.com/durka) fixed [reference definition of :tt](https://github.com/rust-lang/rust/pull/38163).
* [@cardoe](https://github.com/cardoe) fixed: [small typo in bootstrap/README](https://github.com/rust-lang/rust/pull/38073).
* [@tarka](https://github.com/tarka) made [a minor fix to testing concurrency section](https://github.com/rust-lang/rust/pull/38112).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [small typo](https://github.com/rust-lang/rust/pull/38153), added [missing examples for panicking objects](https://github.com/rust-lang/rust/pull/38123), added [checkup for return statement outside of a function](https://github.com/rust-lang/rust/pull/37780), added [examples for exit function](https://github.com/rust-lang/rust/pull/38151), add [missing links to Rc doc](https://github.com/rust-lang/rust/pull/38189), added [missing examples for Ipv6Addr](https://github.com/rust-lang/rust/pull/37859), added [part of missing UdpSocket's urls and examples](https://github.com/rust-lang/rust/pull/38020), added [missing examples for IpAddr enum](https://github.com/rust-lang/rust/pull/38077), added [cloned example for Option](https://github.com/rust-lang/rust/pull/38090) and added [Component examples](https://github.com/rust-lang/rust/pull/38141).

# Meetings

Next meeting will be on Wednesday 14th of December 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
