---
layout: post
title: This Week in Rust Docs 17
date: 2016-08-15
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

The [doc team RFC](https://github.com/rust-lang/rfcs/pull/1683#issuecomment-237384575) has been merged. The rust doc team is now official! Take a look [here](https://www.rust-lang.org/en-US/team.html#Documentation-team).

A new RFC has been opened: [Add API documentation front page styleguide](https://github.com/rust-lang/rfcs/pull/1687).

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

* [@jhod0](https://github.com/jhod0) added [diagnostics for rustc_metadata](https://github.com/rust-lang/rust/pull/34970).
* [@estebank](https://github.com/estebank) added [a specific error message for misplaced doc comments](https://github.com/rust-lang/rust/pull/33922).
* [@ollie27](https://github.com/ollie27) removed [item types from some title pages from rustdoc](https://github.com/rust-lang/rust/pull/35003).
* [@steveklabnik](https://github.com/steveklabnik) made it clear that [the reference isn't normative](https://github.com/rust-lang/rust/pull/35102).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) centered [content of the generated docs](https://github.com/rust-lang/rust/pull/35682), added [new error code tests](https://github.com/rust-lang/rust/pull/35680) and fixed [formatting generation for rustdoc code examples](https://github.com/rust-lang/rust/pull/35012)

# Recent doc contributions

This week, I'll split between the [new error code format](https://github.com/rust-lang/rust/issues/35233) contributions and the others. Let's start by the first one:

* [@munyari](https://github.com/munyari): [E0214](https://github.com/rust-lang/rust/pull/35470), [E0038](https://github.com/rust-lang/rust/pull/35537)
* [@garekkream](https://github.com/garekkream): [E0162](https://github.com/rust-lang/rust/pull/35524), [E0302](https://github.com/rust-lang/rust/pull/35644), [E0301](https://github.com/rust-lang/rust/pull/35643)
* [@hank-der-hafenarbeiter](https://github.com/hank-der-hafenarbeiter): [E0221](https://github.com/rust-lang/rust/pull/35507), [E0045](https://github.com/rust-lang/rust/pull/35541), [E0433](https://github.com/rust-lang/rust/pull/35536)
* [@razielgn](https://github.com/razielgn): [E0026](https://github.com/rust-lang/rust/pull/35504)
* [@srdja](https://github.com/srdja): [E0007 and E0008](https://github.com/rust-lang/rust/pull/35530)
* [@Vassah](https://github.com/Vassah): [E0091 and E0092](https://github.com/rust-lang/rust/pull/35528)
* [@clementmiao](https://github.com/clementmiao): [E0067](https://github.com/rust-lang/rust/pull/35616), [E0070](https://github.com/rust-lang/rust/pull/35615)
* [@crypto-universe](https://github.com/crypto-universe): [E0254](https://github.com/rust-lang/rust/pull/35596)
* [@shyaamsundhar](https://github.com/shyaamsundhar): [E0248, E0267 and E0268](https://github.com/rust-lang/rust/pull/35586)
* [@circuitfox](https://github.com/circuitfox): [E0072](https://github.com/rust-lang/rust/pull/35576), [E0128](https://github.com/rust-lang/rust/pull/35555)
* [@wdv4758h](https://github.com/wdv4758h): [E0138](https://github.com/rust-lang/rust/pull/35573), [E0133](https://github.com/rust-lang/rust/pull/35565)
* [@lukehinds](https://github.com/lukehinds): [E0253](https://github.com/rust-lang/rust/pull/35558)
* [@Limeth](https://github.com/Limeth): [E0263](https://github.com/rust-lang/rust/pull/35557)
* [@theypsilon](https://github.com/theypsilon): [E0384](https://github.com/rust-lang/rust/pull/35552), [E0094](https://github.com/rust-lang/rust/pull/35646)

Others contributions:

* [@IvanUkhov](https://github.com/IvanUkhov) fixed [a couple of typos in RawVec](https://github.com/rust-lang/rust/pull/35661).
* [@pietroalbini](https://github.com/pietroalbini): fixed [docs typo in std::os::unix::net::SocketAddr::is_unnamed](https://github.com/rust-lang/rust/pull/35569).
* [@matthew-piziak](https://github.com/matthew-piziak) fixed [small typos in std::convert documentation](https://github.com/rust-lang/rust/pull/35622).
* [@cvubrugier](https://github.com/cvubrugier) fixed [the hidden find() functions in The Book](https://github.com/rust-lang/rust/pull/35620).
* [@tshepang](https://github.com/tshepang) fixed [`&str` calling in the doc](https://github.com/rust-lang/rust/pull/35597).
* [@qolop](https://github.com/qolop) fixed [typo (privledge->privilege)](https://github.com/rust-lang/rust/pull/34941).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [E0132 error display](https://github.com/rust-lang/rust/pull/35477) and added [new error code tests](https://github.com/rust-lang/rust/pull/35431).

# Meetings

Next meeting will be on Wednesday 17th of August 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
