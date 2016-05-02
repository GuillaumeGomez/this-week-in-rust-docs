---
layout: post
title: This Week in Rust Docs 2
date: 2016-05-01
---

Hello and welcome to *This Week in Rust Docs*!

*This Week in Rust Docs* is openly developed [on GitHub](https://github.com/GuillaumeGomez/this-week-in-rust-docs).
If you find any errors in this week's issue, [please submit a PR](https://github.com/GuillaumeGomez/this-week-in-rust-docs/pulls).

This week's edition was edited by: [GuillaumeGomez](https://github.com/GuillaumeGomez).

# Latest news

Things are moving on: we talked about hosting crates' documentation directly on an official doc website (the hostname hasn't been decided yet). It has already been discussed a few times in the past but nothing came out. For now, we're mostly trying to sort through all of the complexity. A lot of details must be taken in account and it is still at a very early stage of discussion but it started!

The [pull request](https://github.com/rust-lang/rust/pull/32756) on the new rustc output is finally here (or almost)!

[@jonathandturner](https://github.com/jonathandturner) and [@peschkaj](https://github.com/peschkaj) are working on a style guide in order to help developers to write better library documentations.

Besides this, [@peschkaj](https://github.com/peschkaj) investigated the current doc status of the 20 biggest crates (based on number of downloads on [crates.io](https://crates.io)). Take a look at the report [The State of Rust Docs](https://facility9.com/2016/04/the-state-of-rust-docs-2016/).

# Current opened issues

For now, here are the issues opened for Rust documentation:

 * [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
 * [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They both need help to move forward so any contribution is very welcome!

# Recent doc contributions

* [@timothy-mcroy](https://github.com/timothy-mcroy) added [E0434](https://github.com/rust-lang/rust/pull/33229) and [E0501](https://github.com/rust-lang/rust/pull/33294) errors explanation.
* [@birkenfeld](https://github.com/birkenfeld) improved [E0269](https://github.com/rust-lang/rust/pull/33324) and [E0432](https://github.com/rust-lang/rust/pull/33320) errors explanation and fixed [std::thread docs](https://github.com/rust-lang/rust/pull/33326). He also clarified [std::fmt dollar syntax](https://github.com/rust-lang/rust/pull/33258).
* [@mrmiywj](https://github.com/mrmiywj) improved [E0008 error explanation](https://github.com/rust-lang/rust/pull/33260).
* [@bwinterton](https://github.com/bwinterton) improved [BTreeSet::Insert](https://github.com/rust-lang/rust/pull/33276) doc.
* [@durka](https://github.com/durka) worked on [tuple/unit structs](https://github.com/rust-lang/rust/pull/33250) in the rustbook.
* [@benaryorg](https://github.com/benaryorg) clarified documentation of [TcpStream::connect for multiple valid addresses](https://github.com/rust-lang/rust/pull/33167).
* [@fitzgen](https://github.com/fitzgen) clarified [Iterator::enumerate doc example](https://github.com/rust-lang/rust/pull/33085).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez)'s [Pull Request](https://github.com/rust-lang/rust/pull/32230) to add the `--extend-css` option to rustdoc has been merged. He also worked on [process types documentation](https://github.com/rust-lang/rust/pull/33283).

Besides all this, a lot of improvements have been made to rustdoc source code:

* [Linkify extern crates](https://github.com/rust-lang/rust/pull/33196)
* [Improve accessibility of rustdoc pages](https://github.com/rust-lang/rust/pull/33194)
* [Handle concurrent mkdir requests](https://github.com/rust-lang/rust/pull/33191)
* [Only record the same impl once](https://github.com/rust-lang/rust/pull/33153)
* [Inline all the impls](https://github.com/rust-lang/rust/pull/33133)

# Meetings

Next meeting will be on Wednesday 4th of May 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org, feel free to come!
