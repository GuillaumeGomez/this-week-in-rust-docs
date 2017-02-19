---
layout: post
title: This Week in Rust Docs 44
date: 2017-2-19
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

The `rustdoc --test` output has been updated and merged! Now it looks like this:

```
> rustdoc --test some_file.rs
the/path/some_file.rs - Foo::foo (line 43) ... ok
the/path/some_file.rs - Foo::bar (line 79) ... ok
```

Please take a look [to the next rust doc days planning reminder](https://users.rust-lang.org/t/reminder-planning-the-next-rust-doc-days/6901).

The topic to propose crates for the Rust Doc Days is still open and waiting for contributions [here](https://users.rust-lang.org/t/call-for-proposals-for-next-rust-doc-days-crates/6685). Please take a look!

# Current opened issues

For now, here are the two big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on GitHub!

# Waiting for merge

* [@mp4096](https://github.com/mp4096) wrote [better explanation for return values for min, max functions for the Iterator trait](https://github.com/rust-lang/rust/pull/39955).
* [@keeperofdakeys](https://github.com/keeperofdakeys) provided [suggestions for unknown macros imported with `use`](https://github.com/rust-lang/rust/pull/39953) and added [notes about capacity effects to Vec::truncate()](https://github.com/rust-lang/rust/pull/39738).
* [@steveklabnik](https://github.com/steveklabnik) ported [the reference to mdbook](https://github.com/rust-lang/rust/pull/39855) and create [the Unstable Book](https://github.com/rust-lang/rust/pull/39866).
* [@arthurprs](https://github.com/arthurprs) fix [spelling in hashmap comments](https://github.com/rust-lang/rust/pull/39937).
* [@JDemler](https://github.com/JDemler) added [Documentation for Custom Attributes and Error Reporting in Procedural Macros](https://github.com/rust-lang/rust/pull/39845).
* [@jrmuizel](https://github.com/jrmuizel) removed [obsolete documentation about drop-flags](https://github.com/rust-lang/rust/pull/39304).
* [@mina86](https://github.com/mina86) updated The Book: [binary prefixed are defined by IEC and not in SI](https://github.com/rust-lang/rust/pull/39777).
* [@Dowwie](https://github.com/Dowwie) updated [attributes.md - Last sentence updated to reflect support for custom attributes](https://github.com/rust-lang/rust/pull/39691).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) improved [associated constant rendering in rustdoc](https://github.com/rust-lang/rust/pull/39944), set [rustdoc --test files' path relative to the current directory](https://github.com/rust-lang/rust/pull/39859), improved [file not found for module error](https://github.com/rust-lang/rust/pull/39765), fixed [invalid module suggestion](https://github.com/rust-lang/rust/pull/38255) and improved [invalid call on non-function error message](https://github.com/rust-lang/rust/pull/39814).

# Recent doc contributions

* [@shepmaster](https://github.com/shepmaster) improved [grammar on field init docs](https://github.com/rust-lang/rust/pull/39760) and removed [duplicated "parameter" in E0089 text](https://github.com/rust-lang/rust/pull/39758).
* [@JordiPolo](https://github.com/JordiPolo) substituted [try! for ? in the Result documentation](https://github.com/rust-lang/rust/pull/39756).
* [@jimmycuadra](https://github.com/jimmycuadra) included [a stability span only if needed in rustdoc](https://github.com/rust-lang/rust/pull/39740).
* [@notriddle](https://github.com/notriddle) added [the item type to the tooltip](https://github.com/rust-lang/rust/pull/39697).
* [@ollie27](https://github.com/ollie27) showed [attributes on all item types in rustdoc](https://github.com/rust-lang/rust/pull/39654).
* [@stjepang](https://github.com/stjepang) fixed [wording in LocalKey documentation](https://github.com/rust-lang/rust/pull/39862).
* [@king6cong](https://github.com/king6cong) updated [sys/mod doc and mod import order adjust](https://github.com/rust-lang/rust/pull/39844), made [doc consistent with var name](https://github.com/rust-lang/rust/pull/39839) and fixed [a typo](https://github.com/rust-lang/rust/pull/39784).
* [@Stebalien](https://github.com/Stebalien) fixed [String::split_off documentation](https://github.com/rust-lang/rust/pull/39904).
* [@CBenoit](https://github.com/CBenoit) corrected [a typo in procedural macros chapter of the Book](https://github.com/rust-lang/rust/pull/39847).
* [@WRONGWAY4YOU](https://github.com/WRONGWAY4YOU) fixed [typo](https://github.com/rust-lang/rust/pull/39846).
* [@durka](https://github.com/durka) fixed [types in to_owned doctest](https://github.com/rust-lang/rust/pull/39836).
* [@DaseinPhaos](https://github.com/DaseinPhaos) updated [procedural-macros.md](https://github.com/rust-lang/rust/pull/39840).
* [@mina86](https://github.com/mina86) removed [GNU extensions in the example when they were unnecessary in The Book](https://github.com/rust-lang/rust/pull/39775).
* [@steveklabnik](https://github.com/steveklabnik) ported [books to mdbook](https://github.com/rust-lang/rust/pull/39633).
* [@ahmedcharles](https://github.com/ahmedcharles) fixed [some typos in the core::fmt docs.](https://github.com/rust-lang/rust/pull/39778).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [tested item in the rustdoc --test output](https://github.com/rust-lang/rust/pull/39743), added [missing urls for env functions](https://github.com/rust-lang/rust/pull/39928) and added [filename when running rustdoc --test on a markdown file](https://github.com/rust-lang/rust/pull/39788).

# Meetings

Next meeting will be on Wednesday 22nd of February 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
