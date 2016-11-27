---
layout: post
title: This Week in Rust Docs 32
date: 2016-11-27
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

* [@alygin](https://github.com/alygin) fixed [error explanation formatting](https://github.com/rust-lang/rust/pull/38007).
* [@liigo](https://github.com/liigo) got [back missing crate-name when --playground-url is used in rustdoc](https://github.com/rust-lang/rust/pull/37911) and added [suggestions "#[macro_use]" for all undefined macros](https://github.com/rust-lang/rust/pull/37910).
* [@sourcefrog](https://github.com/sourcefrog) documented [that Process::command will search the PATH](https://github.com/rust-lang/rust/pull/38018) and made [a clearer description of std::path::MAIN_SEPARATOR](https://github.com/rust-lang/rust/pull/38019).
* [@Cobrand](https://github.com/Cobrand) improved [and fixed mpsc documentation](https://github.com/rust-lang/rust/pull/37941).
* [@wezm](https://github.com/wezm) simplified [notes on testing and concurrency](https://github.com/rust-lang/rust/pull/38013).
* [@mikhail-m1](https://github.com/mikhail-m1) added [hint to fix error for immutable ref in arg](https://github.com/rust-lang/rust/pull/37863).
* [@sanxiyn](https://github.com/sanxiyn) warned [unused type parameters](https://github.com/rust-lang/rust/pull/37946) and warned [unused type aliases](https://github.com/rust-lang/rust/pull/37631).
* [@estebank](https://github.com/estebank) showed [multiline spans in full if short enough](https://github.com/rust-lang/rust/pull/37369) and detected [missing `;` on methods with return type `()`](https://github.com/rust-lang/rust/pull/36409).
* [@steveklabnik](https://github.com/steveklabnik) replaced [rustup.sh with rustup.rs in The Book](https://github.com/rust-lang/rust/pull/37934).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [examples for TcpListener struct](https://github.com/rust-lang/rust/pull/37983), added [part of missing UdpSocket's urls and examples](https://github.com/rust-lang/rust/pull/38020), added [information in case of markdown block code test failure](https://github.com/rust-lang/rust/pull/36320), added [checkup for return statement outside of a function](https://github.com/rust-lang/rust/pull/37780), added [missing examples for Ipv6Addr](https://github.com/rust-lang/rust/pull/37859), started [of implementation of proposal for E0308](https://github.com/rust-lang/rust/pull/37388), added [ref suggestion](https://github.com/rust-lang/rust/pull/37658) and removed [unneeded tricky macro doc](https://github.com/rust-lang/rust/pull/37870).

# Recent doc contributions

* [@eddyb](https://github.com/eddyb) separated [test collection from the main "clean"-ing pipeline in rustdoc](https://github.com/rust-lang/rust/pull/37890).
* [@estebank](https://github.com/estebank) provided [hint when cast needs a dereference](https://github.com/rust-lang/rust/pull/37442).
* [@birkenfeld](https://github.com/birkenfeld) fixed [duplicate bullet points in feature list](https://github.com/rust-lang/rust/pull/37876).
* [@brcooley](https://github.com/brcooley) fixed [grammar error in lifetimes.md](https://github.com/rust-lang/rust/pull/37840).
* [@ojsheikh](https://github.com/ojsheikh) updated [E0088 to new error format](https://github.com/rust-lang/rust/pull/37835).
* [@steveklabnik](https://github.com/steveklabnik) clarified [the reference's status.](https://github.com/rust-lang/rust/pull/37836).
* [@sfackler](https://github.com/sfackler) fixed [two small issues in iterator docs](https://github.com/rust-lang/rust/pull/37963).
* [@vickenty](https://github.com/vickenty) followed [our own recommendations in the examples](https://github.com/rust-lang/rust/pull/38001).
* [@frewsxcv](https://github.com/frewsxcv) documented [how lock 'guard' structures are created.](https://github.com/rust-lang/rust/pull/38010).
* [@fkjogu](https://github.com/fkjogu) defined [`bound` argument in std::sync::mpsc::sync_channel in the documentation](https://github.com/rust-lang/rust/pull/37978).
* [@samestep](https://github.com/samestep) replaced ["radicum" with "radices"](https://github.com/rust-lang/rust/pull/37961).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing examples in SocketAddr](https://github.com/rust-lang/rust/pull/37880), added [missing urls and examples to TcpStream](https://github.com/rust-lang/rust/pull/38004) and added [missing examples to SocketAddrV6](https://github.com/rust-lang/rust/pull/37962).

# Meetings

Next meeting will be on Wednesday 30th of November 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
