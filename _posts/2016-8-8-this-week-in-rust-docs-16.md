---
layout: post
title: This Week in Rust Docs 16
date: 2016-08-08
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

The [doc team RFC](https://github.com/rust-lang/rfcs/pull/1683#issuecomment-237384575) has entered its final comment period!

A new RFC has been opened: [Add API documentation front page styleguide](https://github.com/rust-lang/rfcs/pull/1687).

A topic to propose crates for the Rust Doc Days has been created [here](https://users.rust-lang.org/t/call-for-proposals-for-next-rust-doc-days-crates/6685). Please take a look!

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

* [@qolop](https://github.com/qolop) fixed [typo (privledge->privilege)](https://github.com/rust-lang/rust/pull/34941).
* [@jhod0](https://github.com/jhod0) added [diagnostics for rustc_metadata](https://github.com/rust-lang/rust/pull/34970).
* [@estebank](https://github.com/estebank) added [a specific error message for misplaced doc comments](https://github.com/rust-lang/rust/pull/33922).
* [@ollie27](https://github.com/ollie27) removed [item types from some title pages from rustdoc](https://github.com/rust-lang/rust/pull/35003).
* [@steveklabnik](https://github.com/steveklabnik) made it clear that [the reference isn't normative](https://github.com/rust-lang/rust/pull/35102).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [formatting generation for rustdoc code examples](https://github.com/rust-lang/rust/pull/35012)

# Recent doc contributions

This week, I'll split between the [new error code format](https://github.com/rust-lang/rust/issues/35233) contributions and the others. Let's start by the first one:

* [@munyari](https://github.com/munyari): [E0205](https://github.com/rust-lang/rust/pull/35468), [E0204](https://github.com/rust-lang/rust/pull/35455)
* [@terrynsun](https://github.com/terrynsun): [E0116](https://github.com/rust-lang/rust/pull/35467)
* [@Detegr](https://github.com/Detegr): [E0117 and E0118](https://github.com/rust-lang/rust/pull/35454)
* [@franleplant](https://github.com/franleplant): [E0101 and E0102](https://github.com/rust-lang/rust/pull/35443)
* [@pcn](https://github.com/pcn): [E0010](https://github.com/rust-lang/rust/pull/35439)
* [@intrepion](https://github.com/intrepion): [E0121](https://github.com/rust-lang/rust/pull/35434)
* [@razielgn](https://github.com/razielgn): [E0225](https://github.com/rust-lang/rust/pull/35421), [E0306](https://github.com/rust-lang/rust/pull/35370), [E0071](https://github.com/rust-lang/rust/pull/35285)
* [@Keats](https://github.com/Keats): [E0243 and E0244](https://github.com/rust-lang/rust/pull/35419), [E0323, E0324 and E0325](https://github.com/rust-lang/rust/pull/35372), [E0137](https://github.com/rust-lang/rust/pull/35319), [E0120](https://github.com/rust-lang/rust/pull/35298)
* [@Limeth](https://github.com/Limeth): [E0131](https://github.com/rust-lang/rust/pull/35417)
* [@silenuss](https://github.com/silenuss): [E0029](https://github.com/rust-lang/rust/pull/35413), [E0027](https://github.com/rust-lang/rust/pull/35410)
* [@KiChjang](https://github.com/KiChjang): [E0223](https://github.com/rust-lang/rust/pull/35411), [E0206](https://github.com/rust-lang/rust/pull/35402)
* [@mikhail-m1](https://github.com/mikhail-m1): [E0201](https://github.com/rust-lang/rust/pull/35394)
* [@TheZoq2](https://github.com/TheZoq2): [E0004](https://github.com/rust-lang/rust/pull/35380)
* [@trixnz](https://github.com/trixnz): [E0373](https://github.com/rust-lang/rust/pull/35376), [E0062](https://github.com/rust-lang/rust/pull/35328)
* [@mrabault](https://github.com/mrabault): [E0229](https://github.com/rust-lang/rust/pull/35374)
* [@oijazsh](https://github.com/oijazsh): [E0107](https://github.com/rust-lang/rust/pull/35373)
* [@medzin](https://github.com/medzin): [E0282](https://github.com/rust-lang/rust/pull/35366), [E0252](https://github.com/rust-lang/rust/pull/35362), [E0178](https://github.com/rust-lang/rust/pull/35296)
* [@kc1212](https://github.com/kc1212): [E0379](https://github.com/rust-lang/rust/pull/35364)
* [@Archytaus](https://github.com/Archytaus): [E0391 and E0404](https://github.com/rust-lang/rust/pull/35359)
* [@shri3k](https://github.com/shri3k): [E0040](https://github.com/rust-lang/rust/pull/35357), [E0046](https://github.com/rust-lang/rust/pull/35355)
* [@Tiwalun](https://github.com/Tiwalun): [E0106](https://github.com/rust-lang/rust/pull/35356)
* [@poveda-ruiz](https://github.com/poveda-ruiz): [E0081](https://github.com/rust-lang/rust/pull/35353)
* [@jaredwy](https://github.com/jaredwy): [E0069](https://github.com/rust-lang/rust/pull/35351)
* [@birryree](https://github.com/birryree): [E0368](https://github.com/rust-lang/rust/pull/35350), [E0060 and E0061](https://github.com/rust-lang/rust/pull/35289)
* [@nickmass](https://github.com/nickmass): [E0055](https://github.com/rust-lang/rust/pull/35333)
* [@circuitfox](https://github.com/circuitfox): [E0119](https://github.com/rust-lang/rust/pull/35326), [E0110](https://github.com/rust-lang/rust/pull/35299), [E0109](https://github.com/rust-lang/rust/pull/35266)
* [@sciyoshi](https://github.com/sciyoshi): [E0124](https://github.com/rust-lang/rust/pull/35318)
* [@yossi-k](https://github.com/yossi-k): [E0185 and E0186](https://github.com/rust-lang/rust/pull/35314), [E0079](https://github.com/rust-lang/rust/pull/35291)
* [@saml](https://github.com/saml): [E0001](https://github.com/rust-lang/rust/pull/35297)
* [@Roybie](https://github.com/Roybie): [E0172](https://github.com/rust-lang/rust/pull/35294), [E0166](https://github.com/rust-lang/rust/pull/35288)
* [@GuillaumeGomez](https://github.com/GuillaumeGomez): [E0132](https://github.com/rust-lang/rust/pull/35264)

Others contributions:

* [@dns2utf8](https://github.com/dns2utf8) added [doc for `std::thread::park_timeout`](https://github.com/rust-lang/rust/pull/35239).
* [@shantanuraj](https://github.com/shantanuraj) updated [wording on E0080](https://github.com/rust-lang/rust/pull/35283).
* [@apasel422](https://github.com/apasel422) added [doc example for `std::ffi::NulError::nul_position`](https://github.com/rust-lang/rust/pull/35182), cleaned up [`std::raw` docs](https://github.com/rust-lang/rust/pull/35281).
* [@frewsxcv](https://github.com/frewsxcv) added [doc example for `std::ffi::NulError::into_vec`](https://github.com/rust-lang/rust/pull/35436), made [a couple `std::net` doc improvements](https://github.com/rust-lang/rust/pull/35175), rewrote [rewrite `slice::chunks` doc example to not require printing](https://github.com/rust-lang/rust/pull/35134), added [doc examples for `range::RangeArgument::{start,end}`](https://github.com/rust-lang/rust/pull/35041) and rewrote [`slice::chunks` doc example to not require printing](https://github.com/rust-lang/rust/pull/35134).
* [@jongiddy](https://github.com/jongiddy) provide [a more explicit example of wildcard version in guessing game doc](https://github.com/rust-lang/rust/pull/35137).
* [@Manishearth](https://github.com/Manishearth) clarified [UnsafeCell docs](https://github.com/rust-lang/rust/pull/34520).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [doc examples for FileType struct](https://github.com/rust-lang/rust/pull/35076), added [`io::Error` doc examples](https://github.com/rust-lang/rust/pull/35109), added [doc example for `Vec`](https://github.com/rust-lang/rust/pull/35181), added [new error codes](https://github.com/rust-lang/rust/pull/35393) and added even more [error code tests](https://github.com/rust-lang/rust/pull/35363) and added even even more [error code tests](https://github.com/rust-lang/rust/pull/35274).

# Meetings

Next meeting will be on Wednesday 10th of August 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
