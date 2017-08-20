---
layout: post
title: This Week in Rust Docs 69
date: 2017-8-20
---

Hello and welcome to *This Week in Rust Docs*!

*This Week in Rust Docs* is openly developed [on GitHub](https://github.com/GuillaumeGomez/this-week-in-rust-docs).
If you find any errors in this week's issue, [please submit a PR](https://github.com/GuillaumeGomez/this-week-in-rust-docs/pulls).

And of course, don't forget to look at the docs:

* [Stable](https://doc.rust-lang.org/)
* [Beta](https://doc.rust-lang.org/beta/)
* [Nightly](https://doc.rust-lang.org/nightly/)

This week's edition was edited by [Guillaume Gomez](https://github.com/GuillaumeGomez).

# Latest news

The [rewrite of rustdoc](https://github.com/steveklabnik/rustdoc) is still under heavy development. Don't hesitate to give it a try!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@oli-obk](https://github.com/oli-obk) added [lint casting signed integers smaller than `isize` to raw pointers](https://github.com/rust-lang/rust/pull/43641) and improved [placement of `use` suggestions](https://github.com/rust-lang/rust/pull/43929).
* [@ruuda](https://github.com/ruuda) pointed ["deref coercions" links to new book](https://github.com/rust-lang/rust/pull/43631).
* [@gaurikholkar](https://github.com/gaurikholkar) added [E0623 for structs](https://github.com/rust-lang/rust/pull/43700) and improved [error message for one named, one anonymous lifetime parameters - underline Type](https://github.com/rust-lang/rust/pull/43851).
* [@qnighy](https://github.com/qnighy) added [hints when intercrate ambiguity causes overlap](https://github.com/rust-lang/rust/pull/43426).
* [@shanavas786](https://github.com/shanavas786) fixed [typo in doc](https://github.com/rust-lang/rust/pull/43996).
* [@huntiep](https://github.com/huntiep) improved [Try error messages](https://github.com/rust-lang/rust/pull/43984).
* [@estebank](https://github.com/estebank) pointed [out missing if conditional](https://github.com/rust-lang/rust/pull/43854).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [new "Implementations on Foreign Types" section to traits in rustdoc](https://github.com/rust-lang/rust/pull/43849).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings when rustdoc html rendering differs](https://github.com/rust-lang/rust/pull/41991), added [missing links in docs](https://github.com/rust-lang/rust/pull/43978), removed [outline when details have focus](https://github.com/rust-lang/rust/pull/43977), compile [fail stable](https://github.com/rust-lang/rust/pull/43949), removed [duplicates in rustdoc](https://github.com/rust-lang/rust/pull/43966) and added [deref suggestion](https://github.com/rust-lang/rust/pull/43870).

# Recent doc contributions

* [@nrc](https://github.com/nrc) fixed [include! in doc tests](https://github.com/rust-lang/rust/pull/43782) and uplifted [fix for include! in doc tests to beta](https://github.com/rust-lang/rust/pull/43922).
* [@Eijebong](https://github.com/Eijebong) fixed [some typos](https://github.com/rust-lang/rust/pull/43814).
* [@frewsxcv](https://github.com/frewsxcv) improved [doc examples for `include*` macros](https://github.com/rust-lang/rust/pull/43819), made [a minor Iterator::filter_map description rewording](https://github.com/rust-lang/rust/pull/43965), made [a minor rewrite of char primitive unicode intro](https://github.com/rust-lang/rust/pull/43919), clarified [writable behavior of readonly-named `Permissions` methods](https://github.com/rust-lang/rust/pull/43883) and rewrote/reorganized [docs for stack size/thread names for spawned threads](https://github.com/rust-lang/rust/pull/43848).
* [@steveklabnik](https://github.com/steveklabnik) wrote [the "passes" chapter of the rustdoc book](https://github.com/rust-lang/rust/pull/43790), updated [the books for next release](https://github.com/rust-lang/rust/pull/43914) and shipped [the rustdoc book](https://github.com/rust-lang/rust/pull/43863).
* [@topecongiro](https://github.com/topecongiro) fixed [bad span for attributes](https://github.com/rust-lang/rust/pull/43933).
* [@anthonyclays](https://github.com/anthonyclays) fixed [typo in RefCell::get_mut](https://github.com/rust-lang/rust/pull/43928).
* [@Songbird0](https://github.com/Songbird0) improved [E0106 - field lifetimes](https://github.com/rust-lang/rust/pull/43912).
* [@adrian5](https://github.com/adrian5) fixed [typo in doc](https://github.com/rust-lang/rust/pull/43915).
* [@partim](https://github.com/partim) documented [that `std::hash::Hasher::finish()` does not reset the hasher](https://github.com/rust-lang/rust/pull/43905).
* [@Fourchaux](https://github.com/Fourchaux) fixed [typos & us spellings](https://github.com/rust-lang/rust/pull/43891).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) put [auto-hidden docblock labels in line with the toggle in rustdoc](https://github.com/rust-lang/rust/pull/43862).
* [@lukaramu](https://github.com/lukaramu) added [missing newline in Deref docs to fix rendering](https://github.com/rust-lang/rust/pull/43868).
* [@ollie27](https://github.com/ollie27) removed [external impls to implementors js in rustdoc](https://github.com/rust-lang/rust/pull/43736).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing links doc](https://github.com/rust-lang/rust/pull/43803), udpdated [error message for unsized union field](https://github.com/rust-lang/rust/pull/43901), added [help for static method invalid use](https://github.com/rust-lang/rust/pull/43864), removed [useless help part](https://github.com/rust-lang/rust/pull/43867) and added [a note to unused variables](https://github.com/rust-lang/rust/pull/43850).

# Meetings

Next meeting will be on Wednesday 23rd of August 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
