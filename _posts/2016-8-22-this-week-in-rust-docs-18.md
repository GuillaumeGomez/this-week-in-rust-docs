---
layout: post
title: This Week in Rust Docs 18
date: 2016-08-22
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

* [@matthew-piziak](https://github.com/matthew-piziak) improved [documentation for `Fn*` traits](https://github.com/rust-lang/rust/pull/35810), replaced [`BitAnd` example with something more evocative of bitwise AND](https://github.com/rust-lang/rust/pull/35809), demonstrated that [`RHS != Self` use cases for `Add` and `Sub`](https://github.com/rust-lang/rust/pull/35793), added [evocative examples for `Shl` and `Shr`](https://github.com/rust-lang/rust/pull/35863), replaced [`Rem` example with something more evocative](https://github.com/rust-lang/rust/pull/35861), replaced [`Mul` example with something more evocative of multiplication](https://github.com/rust-lang/rust/pull/35860), replaced [`Index` example with something more evocative of indexing](https://github.com/rust-lang/rust/pull/35864), made [more evocative examples for `Sub` and `SubAssign`](https://github.com/rust-lang/rust/pull/35876), replaced [`println!` statements with `assert!`ions in `std::ptr` examples](https://github.com/rust-lang/rust/pull/35878), added [example for `Rc::would_unwrap`](https://github.com/rust-lang/rust/pull/35881), added [links to interesting items in `std::ptr` documentation ](https://github.com/rust-lang/rust/pull/35880) and added [a panic example to std::from_utf8_unchecked](https://github.com/rust-lang/rust/pull/35890).
* [@F001](https://github.com/F001) fixed [documentation in cell mod](https://github.com/rust-lang/rust/pull/35895).
* [@CryZe](https://github.com/CryZe) fixed ["Furthermore" Typo in String Docs](https://github.com/rust-lang/rust/pull/35879).
* [@alevy](https://github.com/alevy) fixed [a minor typo in CONTRIBUTING.md](https://github.com/rust-lang/rust/pull/35889).
* [@munyari](https://github.com/munyari) added [reference to `Self` in traits chapter (book)](https://github.com/rust-lang/rust/pull/35891).
* [@frewsxcv](https://github.com/frewsxcv) indicated [where `core::result::IntoIter` is created](https://github.com/rust-lang/rust/pull/35845) and made [various refactorings in the rustdoc module](https://github.com/rust-lang/rust/pull/35867).
* [@Stebalien](https://github.com/Stebalien) clarified/fixed [formatting docs concerning fmt::Result/fmt::Error](https://github.com/rust-lang/rust/pull/35862).
* [@jhod0](https://github.com/jhod0) added [diagnostics for rustc_metadata](https://github.com/rust-lang/rust/pull/34970).
* [@estebank](https://github.com/estebank) added [a specific error message for misplaced doc comments](https://github.com/rust-lang/rust/pull/33922).
* [@ollie27](https://github.com/ollie27) removed [item types from some title pages from rustdoc](https://github.com/rust-lang/rust/pull/35003).
* [@steveklabnik](https://github.com/steveklabnik) made it clear that [the reference isn't normative](https://github.com/rust-lang/rust/pull/35102).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) improved [Path and PathBuf docs](https://github.com/rust-lang/rust/pull/35786), added [new error code tests](https://github.com/rust-lang/rust/pull/35824) and fixed [formatting generation for rustdoc code examples](https://github.com/rust-lang/rust/pull/35012).


# Recent doc contributions

This week (too), I'll split between the [new error code format](https://github.com/rust-lang/rust/issues/35233) contributions and the others. Let's start by the first one:

* [@trixnz](https://github.com/trixnz): [E0428](https://github.com/rust-lang/rust/pull/35831)
* [@mlayne](https://github.com/mlayne): [E0232](https://github.com/rust-lang/rust/pull/35812)
* [@pliniker](https://github.com/pliniker): [E0084](https://github.com/rust-lang/rust/pull/35804)
* [@clementmiao](https://github.com/clementmiao): [E0396](https://github.com/rust-lang/rust/pull/35780), [E0395](https://github.com/rust-lang/rust/pull/35778)
* [@KiChjang](https://github.com/KiChjang): [E0053](https://github.com/rust-lang/rust/pull/35765)
* [@crypto-universe](https://github.com/crypto-universe): [E0407](https://github.com/rust-lang/rust/pull/35756)
* [@DevShep](https://github.com/DevShep): [E0009](https://github.com/rust-lang/rust/pull/35744)
* [@circuitfox](https://github.com/circuitfox): [E0403](https://github.com/rust-lang/rust/pull/35739)
* [@pythoneer](https://github.com/pythoneer): [E0005](https://github.com/rust-lang/rust/pull/35731)
* [@mikhail-m1](https://github.com/mikhail-m1): [E0409](https://github.com/rust-lang/rust/pull/35726), [E0375](https://github.com/rust-lang/rust/pull/35686)
* [@knight42](https://github.com/knight42): [E0394 and E0422](https://github.com/rust-lang/rust/pull/35722)
* [@yossi-k](https://github.com/yossi-k): [E0322](https://github.com/rust-lang/rust/pull/35672)
* [@canaltinova](https://github.com/canaltinova): [E0392](https://github.com/rust-lang/rust/pull/35671)
* [@RockyTV](https://github.com/RockyTV): [E0365](https://github.com/rust-lang/rust/pull/35670)

Others contributions:

* [@matthew-piziak](https://github.com/matthew-piziak) replaced [`Neg` example with something more evocative of negation](https://github.com/rust-lang/rust/pull/35830), replaced [`Not` example with something more evocative](https://github.com/rust-lang/rust/pull/35827), replaced [`AddAssign` example with something more evocative of addition](https://github.com/rust-lang/rust/pull/35806), demonstrated [`RHS != Self` use cases for `Mul` and `Div`](https://github.com/rust-lang/rust/pull/35800), replaced [`Add` example with something more evocative of addition](https://github.com/rust-lang/rust/pull/35709).
* [@terrynsun](https://github.com/terrynsun) updated [E0207 label to report parameter type](https://github.com/rust-lang/rust/pull/35660).
* [@CryZe](https://github.com/CryZe) improved [`No stdlib` and related documentation](https://github.com/rust-lang/rust/pull/35663).
* [@crypto-universe](https://github.com/crypto-universe) updated [test for E0221](https://github.com/rust-lang/rust/pull/35770).
* [@ErikUggeldahl](https://github.com/ErikUggeldahl) fixed [very minor spelling typo in The Book](https://github.com/rust-lang/rust/pull/35781).
* [@cantino](https://github.com/cantino) fixed [minor typo](https://github.com/rust-lang/rust/pull/35794).
* [@wdv4758h](https://github.com/wdv4758h) fixed [incorrect label messages for missing unsafe blocks (E0133)](https://github.com/rust-lang/rust/pull/35818).
* [@frewsxcv](https://github.com/frewsxcv) added [a few doc examples for `std::ffi::OsStr`](https://github.com/rust-lang/rust/pull/35775).
* [@ollie27](https://github.com/ollie27) fixed [a couple of issues with search results in rustdoc](https://github.com/rust-lang/rust/pull/35655).
* [@jonathandturner](https://github.com/jonathandturner) fixed [wording in error messages](https://github.com/rust-lang/rust/pull/35839) and moved ['doesn't live long enough' errors to labels](https://github.com/rust-lang/rust/pull/35732).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [new error code tests](https://github.com/rust-lang/rust/pull/35680) and fixed [issue #11004](https://github.com/rust-lang/rust/pull/35749).

# Meetings

Next meeting will be on Wednesday 24th of August 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
