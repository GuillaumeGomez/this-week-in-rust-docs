---
layout: post
title: This Week in Rust Docs 56
date: 2017-5-14
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

# Current opened issues

For now, here are the two big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@estebank](https://github.com/estebank) made [unsatisfied trait bounds note multiline](https://github.com/rust-lang/rust/pull/41489).
* [@icefoxen](https://github.com/icefoxen) made [a tiny update to rustdoc CSS](https://github.com/rust-lang/rust/pull/40719).
* [@abonander](https://github.com/abonander) documented [the `proc_macro` feature in the Unstable Book](https://github.com/rust-lang/rust/pull/41476).
* [@F001](https://github.com/F001) updated [backtrace formating text tips](https://github.com/rust-lang/rust/pull/41989) and fixed [comma after struct update syntax](https://github.com/rust-lang/rust/pull/41848).
* [@est31](https://github.com/est31) added [lint for unused macros](https://github.com/rust-lang/rust/pull/41907).
* [@gamazeps](https://github.com/gamazeps) added [`'static` and `Send` constraints explanations to `thread::spawn`](https://github.com/rust-lang/rust/pull/41980), expanded [`detach` documentation in `thread::JoinHande`](https://github.com/rust-lang/rust/pull/41981) and explained [why `thread::yield_now` could be used](https://github.com/rust-lang/rust/pull/41982).
* [@Aaronepower](https://github.com/Aaronepower) updated [releases notes for 1.18](https://github.com/rust-lang/rust/pull/41953).
* [@kosta](https://github.com/kosta) improved [error message 'can't qualify macro invocation with '](https://github.com/rust-lang/rust/pull/41909).
* [@dhardy](https://github.com/dhardy) add [loop_break_value documentation for The Book](https://github.com/rust-lang/rust/pull/41857).
* [@excaliburHisSheath](https://github.com/excaliburHisSheath) improved [docs in os::windows::ffi and os::windows::fs](https://github.com/rust-lang/rust/pull/41870).
* [@froydnj](https://github.com/froydnj) fixed [confusion about parts required for float formatting](https://github.com/rust-lang/rust/pull/41859).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) reduced [HTML output in rustdoc](https://github.com/rust-lang/rust/pull/41384), added [better error message when == operator is badly used](https://github.com/rust-lang/rust/pull/41559), added [help message if a FnOnce is moved](https://github.com/rust-lang/rust/pull/41772) and made [--extend-css stable](https://github.com/rust-lang/rust/pull/41700).

# Recent doc contributions

* [@estebank](https://github.com/estebank) pointed [at fields that make the type recursive](https://github.com/rust-lang/rust/pull/40857) and used [diagnostics for trace_macro instead of println](https://github.com/rust-lang/rust/pull/41520).
* [@mandeep](https://github.com/mandeep) added [generic example of std::ops::Add in doc comments](https://github.com/rust-lang/rust/pull/41612).
* [@brson](https://github.com/brson) updated [release notes for 1.17](https://github.com/rust-lang/rust/pull/41548).
* [@steveklabnik](https://github.com/steveklabnik) improved [docs on `Arc<T>` and Send/Sync](https://github.com/rust-lang/rust/pull/41536) and added [more ways to create a PathBuf to docs](https://github.com/rust-lang/rust/pull/41531).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) allowed [# to appear in rustdoc code output](https://github.com/rust-lang/rust/pull/41785) and made a [minor cleanup of UX guidelines](https://github.com/rust-lang/rust/pull/41791).
* [@oli-obk](https://github.com/oli-obk) refactored [suggestion diagnostic API to allow for multiple suggestions](https://github.com/rust-lang/rust/pull/41876) and upgraded [some comments to doc comments](https://github.com/rust-lang/rust/pull/41912).
* [@gamazeps](https://github.com/gamazeps) improved [`thread::panicking` documentation](https://github.com/rust-lang/rust/pull/41811), improved [`thread::Thread` and `thread::Builder` documentations](https://github.com/rust-lang/rust/pull/41814), improved [`thread::spawn` documentation](https://github.com/rust-lang/rust/pull/41854) and improved [the thread::park and thread::unpark documentation](https://github.com/rust-lang/rust/pull/41809).
* [@mglagla](https://github.com/mglagla) fixed [typo in Iterator::size_hint example comment](https://github.com/rust-lang/rust/pull/41916).
* [@Eijebong](https://github.com/Eijebong) broke [words in the location box of the sidebar in rustdoc](https://github.com/rust-lang/rust/pull/41951).
* [@mbrubeck](https://github.com/mbrubeck) removed [wrong or outdated info from CString docs.](https://github.com/rust-lang/rust/pull/41860).
* [@RalfJung](https://github.com/RalfJung) fixed [typo in Unique::empty doc](https://github.com/rust-lang/rust/pull/41886).
* [@Migi](https://github.com/Migi) fixed [typo in subst.rs](https://github.com/rust-lang/rust/pull/41842).
* [@z1mvader](https://github.com/z1mvader) fixed [argument inference for closures when coercing into 'fn'](https://github.com/rust-lang/rust/pull/41838).
* [@jz0425](https://github.com/jz0425) updated [rustc-ux-guidelines](https://github.com/rust-lang/rust/pull/41836).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [anchor invalid redirection to search](https://github.com/rust-lang/rust/pull/41950), added [markdown-[before|after]-content options](https://github.com/rust-lang/rust/pull/41826), fixed [search when looking to sources](https://github.com/rust-lang/rust/pull/41921) and improved [E0477 error message](https://github.com/rust-lang/rust/pull/41862).

# Meetings

Next meeting will be on Wednesday 17th of May 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
