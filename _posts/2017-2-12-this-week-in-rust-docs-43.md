---
layout: post
title: This Week in Rust Docs 43
date: 2017-2-12
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

The `rustdoc --test` output has been updated. Now it looks like this (or at least it'll when [#39743](https://github.com/rust-lang/rust/pull/39743) will get merged):

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

* [@keeperofdakeys](https://github.com/keeperofdakeys) added [notes about capacity effects to Vec::truncate()](https://github.com/rust-lang/rust/pull/39738).
* [@frewsxcv](https://github.com/frewsxcv) documented [the return value of zero-size/zero-heap pointer types](https://github.com/rust-lang/rust/pull/39757).
* [@shepmaster](https://github.com/shepmaster) improved [grammar on field init docs](https://github.com/rust-lang/rust/pull/39760) and removed [duplicated "parameter" in E0089 text](https://github.com/rust-lang/rust/pull/39758).
* [@Rufflewind](https://github.com/Rufflewind) resolved [ambiguities in the Generics in the Book](https://github.com/rust-lang/rust/pull/39748).
* [@JordiPolo](https://github.com/JordiPolo) substituted [try! for ? in the Result documentation](https://github.com/rust-lang/rust/pull/39756).
* [@jimmycuadra](https://github.com/jimmycuadra) included [a stability span only if needed in rustdoc](https://github.com/rust-lang/rust/pull/39740).
* [@Dowwie](https://github.com/Dowwie) updated [attributes.md - Last sentence updated to reflect support for custom attributes](https://github.com/rust-lang/rust/pull/39691).
* [@estebank](https://github.com/estebank) cleaned up ["pattern doesn't bind x" messages](https://github.com/rust-lang/rust/pull/39713).
* [@notriddle](https://github.com/notriddle) added [the item type to the tooltip](https://github.com/rust-lang/rust/pull/39697).
* [@ollie27](https://github.com/ollie27) showed [attributes on all item types in rustdoc](https://github.com/rust-lang/rust/pull/39654).
* [@zackmdavis](https://github.com/zackmdavis) used [help rather than span note for no method error; a slight rephrasing](https://github.com/rust-lang/rust/pull/39441).
* [@oli-obk](https://github.com/oli-obk) distinguished [guesses from suggestions](https://github.com/rust-lang/rust/pull/39458).
* [@jrmuizel](https://github.com/jrmuizel) removed [obsolete documentation about drop-flags](https://github.com/rust-lang/rust/pull/39304).
* [@APTy](https://github.com/APTy) added [docs and tests for join_multicast_{v4,v6}](https://github.com/rust-lang/rust/pull/39007).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [tested item in the rustdoc --test output](https://github.com/rust-lang/rust/pull/39743), added [missing urls and small nits](https://github.com/rust-lang/rust/pull/39513) and fixed [invalid module suggestion](https://github.com/rust-lang/rust/pull/38255).

# Recent doc contributions

* [@zackmdavis](https://github.com/zackmdavis) improved [error message when two-arg assert_eq! receives a trailing comma](https://github.com/rust-lang/rust/pull/39554).
* [@keeperofdakeys](https://github.com/keeperofdakeys) gave [a better error message for unknown derive messages](https://github.com/rust-lang/rust/pull/39444).
* [@cengizIO](https://github.com/cengizIO) improved [error message for uninferrable types #38812](https://github.com/rust-lang/rust/pull/39361).
* [@JordiPolo](https://github.com/JordiPolo) changed [deprecation warning to indicate custom derive support was removed](https://github.com/rust-lang/rust/pull/39545).
* [@nagisa](https://github.com/nagisa) expanded [documentation of process::exit and exec](https://github.com/rust-lang/rust/pull/38518).
* [@mgattozzi](https://github.com/mgattozzi) fixed [full path being output with `rustdoc -h`](https://github.com/rust-lang/rust/pull/39312).
* [@rspeer](https://github.com/rspeer) fixed [a misleading statement in`Iterator.nth()`](https://github.com/rust-lang/rust/pull/39174).
* [@bluecereal](https://github.com/bluecereal) updated [if-let.md](https://github.com/rust-lang/rust/pull/38436).
* [@phungleson](https://github.com/phungleson) fixed [short hand struct doc](https://github.com/rust-lang/rust/pull/39459) and removed [suggestions to use things which weren't found either](https://github.com/rust-lang/rust/pull/39443).
* [@chriskrycho](https://github.com/chriskrycho) documented [RFC 1623: static lifetime elision.](https://github.com/rust-lang/rust/pull/37928).
* [@durka](https://github.com/durka) removed [lie about #[cfg] from reference](https://github.com/rust-lang/rust/pull/39374) and changed [span_notes to notes in E0368/E0369](https://github.com/rust-lang/rust/pull/39707).
* [@brson](https://github.com/brson) updated [1.15.1 relnotes](https://github.com/rust-lang/rust/pull/39710).
* [@sgrif](https://github.com/sgrif) explicitly mentioned [that `Vec::reserve` is based on len not capacity](https://github.com/rust-lang/rust/pull/39701).
* [@Aaronepower](https://github.com/Aaronepower) updated [nightly book with installing nightly instructions](https://github.com/rust-lang/rust/pull/39725).
* [@jethrogb](https://github.com/jethrogb) updated [set operations documentation](https://github.com/rust-lang/rust/pull/39708).
* [@ollie27](https://github.com/ollie27) improved [impl disambiguation in rustdoc](https://github.com/rust-lang/rust/pull/39589).
* [@Gheoan](https://github.com/Gheoan) added [missing comma](https://github.com/rust-lang/rust/pull/39620).
* [@steveklabnik](https://github.com/steveklabnik) re-wrote [the doc index page](https://github.com/rust-lang/rust/pull/39593).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [Debug implementations for libcollection structs](https://github.com/rust-lang/rust/pull/39002), displayed [correct filename with --test option](https://github.com/rust-lang/rust/pull/39597), added [missing urls on join_paths](https://github.com/rust-lang/rust/pull/39649) and added [missing urls for current_dir](https://github.com/rust-lang/rust/pull/39621).

# Meetings

Next meeting will be on Wednesday 15th of February 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
