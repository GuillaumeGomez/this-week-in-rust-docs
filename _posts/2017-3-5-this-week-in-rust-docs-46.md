---
layout: post
title: This Week in Rust Docs 46
date: 2017-3-5
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

Nothing.

# Current opened issues

For now, here are the two big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on GitHub!

# Waiting for merge

* [@wesleywiser](https://github.com/wesleywiser) improved [the style of the sidebar in rustdoc output](https://github.com/rust-lang/rust/pull/40265).
* [@jdhorwitz](https://github.com/jdhorwitz) helped [people find String::as_bytes() for UTF-8](https://github.com/rust-lang/rust/pull/40226).
* [@steveklabnik](https://github.com/steveklabnik) added [unstable book to the bookshelf](https://github.com/rust-lang/rust/pull/40154) and extracted [nomicon to its own repo](https://github.com/rust-lang/rust/pull/40222).
* [@estebank](https://github.com/estebank) cleaned [up "pattern doesn't bind x" messages](https://github.com/rust-lang/rust/pull/39713) and pointed to [enclosing block/fn on nested unsafe](https://github.com/rust-lang/rust/pull/39202).
* [@est31](https://github.com/est31) fixed [description of closure coercion feature](https://github.com/rust-lang/rust/pull/40258).
* [@brson](https://github.com/brson) added [release notes for 1.16](https://github.com/rust-lang/rust/pull/39835).
* [@Dowwie](https://github.com/Dowwie) updated [attributes.md - Last sentence updated to reflect support for custom attributes](https://github.com/rust-lang/rust/pull/39691).
* [@APTy](https://github.com/APTy) added [docs and tests for join_multicast_{v4,v6}](https://github.com/rust-lang/rust/pull/39007).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing urls and small nits](https://github.com/rust-lang/rust/pull/39513), improved [invalid call on non-function error message](https://github.com/rust-lang/rust/pull/39814), fixed [invalid module suggestion](https://github.com/rust-lang/rust/pull/38255) and added [ref suggestion](https://github.com/rust-lang/rust/pull/37658).

# Recent doc contributions

* [@pmer](https://github.com/pmer) used ["macOS" terminology consistently](https://github.com/rust-lang/rust/pull/40102).
* [@keeperofdakeys](https://github.com/keeperofdakeys) replaced [./configure with config.toml in README.md and CONTRIBUTING.md](https://github.com/rust-lang/rust/pull/40056) and adde [notes about capacity effects to Vec::truncate()](https://github.com/rust-lang/rust/pull/39738).
* [@steveklabnik](https://github.com/steveklabnik) moved [the reference into a submodule](https://github.com/rust-lang/rust/pull/40213), updated [mdbook version](https://github.com/rust-lang/rust/pull/40151) and sorted [unstable book alphabetically](https://github.com/rust-lang/rust/pull/40153).
* [@iKevinY](https://github.com/iKevinY) fixed [link in `if let` docs](https://github.com/rust-lang/rust/pull/40170).
* [@letmaik](https://github.com/letmaik) fixed [wrong word used in book page "const and static"](https://github.com/rust-lang/rust/pull/40194).
* [@d-e-s-o](https://github.com/d-e-s-o) fixed [inconsistency in error output in guessing-game.md](https://github.com/rust-lang/rust/pull/40175).
* [@MajorBreakfast](https://github.com/MajorBreakfast) added ["the" in the docs](https://github.com/rust-lang/rust/pull/40169), improved [unit-like structs code sample in the docs](https://github.com/rust-lang/rust/pull/40144), changed ["pointers" to "references" in structs docs](https://github.com/rust-lang/rust/pull/40142), made [lifetime elision docs clearer](https://github.com/rust-lang/rust/pull/40131) and used [present perfect instead of simple past in the loop docs](https://github.com/rust-lang/rust/pull/40115).
* [@robinst](https://github.com/robinst) added [an example for how to provide stdin using std::process::Command](https://github.com/rust-lang/rust/pull/40122).
* [@king6cong](https://github.com/king6cong) fixed [typo](https://github.com/rust-lang/rust/pull/40121).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [nightly-only experimental API display](https://github.com/rust-lang/rust/pull/40057), added [missing url in sync structs](https://github.com/rust-lang/rust/pull/40081), added [missing urls and examples for Condvar docs](https://github.com/rust-lang/rust/pull/40033), improved [associated constant rendering in rustdoc](https://github.com/rust-lang/rust/pull/39944) and added [missing docs and examples for fmt::Write](https://github.com/rust-lang/rust/pull/40126).

# Meetings

Next meeting will be on Wednesday 8th of March 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
