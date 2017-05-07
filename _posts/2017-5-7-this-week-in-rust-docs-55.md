---
layout: post
title: This Week in Rust Docs 55
date: 2017-5-7
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

After a long debate, it has been decided to keep hoedown testing/rendering by default in rustdoc. However, you can test pulldown by running rustdoc with `-Z unstable-options enable-commonmark`.

The jquery dependency [is being removed](https://github.com/rust-lang/rust/pull/41307) from the rustdoc javascript. When navigating in the docs, please check if everything's working as expected!

# Current opened issues

For now, here are the two big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@estebank](https://github.com/estebank) pointed [at fields that make the type recursive](https://github.com/rust-lang/rust/pull/40857), emitted [diagnostic when using `const` storing `Fn` as pattern](https://github.com/rust-lang/rust/pull/41434), made [unsatisfied trait bounds note multiline](https://github.com/rust-lang/rust/pull/41489), used [diagnostics for trace_macro instead of println](https://github.com/rust-lang/rust/pull/41520) and removed [duplicated errors for closure type mismatch](https://github.com/rust-lang/rust/pull/41760).
* [@irfanhudda](https://github.com/irfanhudda) improved [documentation of next_power_of_two](https://github.com/rust-lang/rust/pull/40706).
* [@icefoxen](https://github.com/icefoxen) made [a tiny update to rustdoc CSS](https://github.com/rust-lang/rust/pull/40719).
* [@abonander](https://github.com/abonander) documented [the `proc_macro` feature in the Unstable Book](https://github.com/rust-lang/rust/pull/41476).
* [@mandeep](https://github.com/mandeep) added [generic example of std::ops::Add in doc comments](https://github.com/rust-lang/rust/pull/41612).
* [@brson](https://github.com/brson) updated [release notes for 1.17](https://github.com/rust-lang/rust/pull/41548).
* [@steveklabnik](https://github.com/steveklabnik) improved [docs on `Arc<T>` and Send/Sync](https://github.com/rust-lang/rust/pull/41536) and added [more ways to create a PathBuf to docs](https://github.com/rust-lang/rust/pull/41531).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) allowed [# to appear in rustdoc code output.](https://github.com/rust-lang/rust/pull/41785) and made a [minor cleanup of UX guidelines.](https://github.com/rust-lang/rust/pull/41791).
* [@Idolf](https://github.com/Idolf) supported [#![deny(missing_docs)] together with #[proc_macro_derive]](https://github.com/rust-lang/rust/pull/41747).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) reduced [HTML output in rustdoc](https://github.com/rust-lang/rust/pull/41384), added [better error message when == operator is badly used](https://github.com/rust-lang/rust/pull/41559), added [help message if a FnOnce is moved](https://github.com/rust-lang/rust/pull/41772) and made [--extend-css stable](https://github.com/rust-lang/rust/pull/41700).

# Recent doc contributions

* [@estebank](https://github.com/estebank) cleaned [up callable type mismatch errors](https://github.com/rust-lang/rust/pull/41488).
* [@topecongiro](https://github.com/topecongiro) updated [docs of 'fence'](https://github.com/rust-lang/rust/pull/41217).
* [@alexeyzab](https://github.com/alexeyzab) fixed [error message for mismatched types](https://github.com/rust-lang/rust/pull/41547).
* [@z1mvader](https://github.com/z1mvader) rewrote [the thread struct docs](https://github.com/rust-lang/rust/pull/41543).
* [@frewsxcv](https://github.com/frewsxcv) added [links between `slice::{copy,clone}_from_slice` in docs](https://github.com/rust-lang/rust/pull/41784), fixed [incorrect hex value in doc comment example](https://github.com/rust-lang/rust/pull/41688), simplified [types in `std::option` doc comment example](https://github.com/rust-lang/rust/pull/41749) and made [improvements to `std::time::Duration` doc examples](https://github.com/rust-lang/rust/pull/41720).
* [@acdenisSK](https://github.com/acdenisSK) fixed ["an" usage](https://github.com/rust-lang/rust/pull/41786).
* [@rap2hpoutre](https://github.com/rap2hpoutre) added [an example to std::thread::Result type](https://github.com/rust-lang/rust/pull/41768).
* [@mgattozzi](https://github.com/mgattozzi) updated [ChildStdin/ChildStdout docs to be clearer](https://github.com/rust-lang/rust/pull/41721).
* [@bholley](https://github.com/bholley) documented [the reasoning for the Acquire/Release handshake when dropping Arcs](https://github.com/rust-lang/rust/pull/41730).
* [@cuviper](https://github.com/cuviper) fixed [links in RELEASES.md for 1.10.0 through 1.12.0](https://github.com/rust-lang/rust/pull/41613).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) removed [ANTLR grammar](https://github.com/rust-lang/rust/pull/41705) and unignored [tests which work fine now](https://github.com/rust-lang/rust/pull/41629).
* [@oli-obk](https://github.com/oli-obk) minimized [single span suggestions into a label](https://github.com/rust-lang/rust/pull/40851).
* [@hsivonen](https://github.com/hsivonen) explained [why zero-length slices require a non-null pointer](https://github.com/rust-lang/rust/pull/41602).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) removed [jquery dependency](https://github.com/rust-lang/rust/pull/41307) and add [option to display warnings in rustdoc](https://github.com/rust-lang/rust/pull/41678).

# Meetings

Next meeting will be on Wednesday 10th of May 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
