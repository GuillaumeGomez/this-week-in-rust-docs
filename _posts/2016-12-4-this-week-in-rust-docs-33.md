---
layout: post
title: This Week in Rust Docs 33
date: 2016-12-4
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

* [Error code list which need to be updated to new format](https://github.com/rust-lang/rust/issues/35233)
* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on GitHub!

# Call for participation

There's now a call for participation to [display all methods of a type, even those from implicit traits in rustdoc](https://github.com/rust-lang/rust/issues/33772). This is a great way to help users find everything that a type can do. Any help on it would be very appreciated!

# Waiting for merge

* [@estebank](https://github.com/estebank) pointed [out the known type when field doesn't satisfy bound](https://github.com/rust-lang/rust/pull/38150), supported [`is_letter()` on `char`](https://github.com/rust-lang/rust/pull/38125), showed [span for trait that doesn't implement Copy](https://github.com/rust-lang/rust/pull/37493), warned [when an import list is empty](https://github.com/rust-lang/rust/pull/38085) and detected [missing `;` on methods with return type `()`](https://github.com/rust-lang/rust/pull/36409).
* [@KiChjang](https://github.com/KiChjang) displayed [better error messages for E0282](https://github.com/rust-lang/rust/pull/38057).
* [@wezm](https://github.com/wezm) simplified [notes on testing and concurrency](https://github.com/rust-lang/rust/pull/38013).
* [@jonathandturner](https://github.com/jonathandturner) pointed [arg num mismatch errors back to their definition](https://github.com/rust-lang/rust/pull/38121).
* [@brson](https://github.com/brson) updated [book for rustup](https://github.com/rust-lang/rust/pull/38122).
* [@linclark](https://github.com/linclark) added [error explanation for E0328](https://github.com/rust-lang/rust/pull/38108).
* [@ollie27](https://github.com/ollie27) added [sort lines in search index and implementors js in rustdoc](https://github.com/rust-lang/rust/pull/38105).
* [@zackmdavis](https://github.com/zackmdavis) note [individual lint name in messages set via lint group attribute](https://github.com/rust-lang/rust/pull/38103).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [small typo](https://github.com/rust-lang/rust/pull/38153), added [more examples to UpdSocket](https://github.com/rust-lang/rust/pull/38067), added [missing examples for panicking objects](https://github.com/rust-lang/rust/pull/38123), casted [suggestions](https://github.com/rust-lang/rust/pull/38099), added [checkup for return statement outside of a function](https://github.com/rust-lang/rust/pull/37780), added [examples for exit function](https://github.com/rust-lang/rust/pull/38151) and added [information in case of markdown block code test failure](https://github.com/rust-lang/rust/pull/36320).

# Recent doc contributions

* [@alygin](https://github.com/alygin) fixed [error explanation formatting](https://github.com/rust-lang/rust/pull/38007).
* [@liigo](https://github.com/liigo) got [back missing crate-name when --playground-url is used in rustdoc](https://github.com/rust-lang/rust/pull/37911).
* [@sourcefrog](https://github.com/sourcefrog) documented [that Process::command will search the PATH](https://github.com/rust-lang/rust/pull/38018) and made [a clearer description of std::path::MAIN_SEPARATOR](https://github.com/rust-lang/rust/pull/38019).
* [@mikhail-m1](https://github.com/mikhail-m1) added [hint to fix error for immutable ref in arg](https://github.com/rust-lang/rust/pull/37863).
* [@estebank](https://github.com/estebank) showed [multiline spans in full if short enough](https://github.com/rust-lang/rust/pull/37369) and showed [`Trait` instead of `<Struct as Trait>` in E0323](https://github.com/rust-lang/rust/pull/38065).
* [@cardoe](https://github.com/cardoe) fixed [small typo in bootstrap/README](https://github.com/rust-lang/rust/pull/38073).
* [@jethrogb](https://github.com/jethrogb) updated [items section in reference](https://github.com/rust-lang/rust/pull/38130).
* [@tarka](https://github.com/tarka) fixed [testing concurrency section](https://github.com/rust-lang/rust/pull/38112).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [examples for TcpListener struct](https://github.com/rust-lang/rust/pull/37983), added [part of missing UdpSocket's urls and examples](https://github.com/rust-lang/rust/pull/38020), added [missing examples for Ipv6Addr](https://github.com/rust-lang/rust/pull/37859), added [missing examples for IpAddr enum](https://github.com/rust-lang/rust/pull/38077), added [cloned example for Option](https://github.com/rust-lang/rust/pull/38090) and added [Component examples](https://github.com/rust-lang/rust/pull/38141).

# Meetings

Next meeting will be on Wednesday 7th of December 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
