---
layout: post
title: This Week in Rust Docs 57
date: 2017-5-21
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

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@F001](https://github.com/F001) fixed [comma after struct update syntax](https://github.com/rust-lang/rust/pull/41848).
* [@gamazeps](https://github.com/gamazeps) added [`'static` and `Send` constraints explanations to `thread::spawn`](https://github.com/rust-lang/rust/pull/41980) and expanded [`detach` documentation in `thread::JoinHande`](https://github.com/rust-lang/rust/pull/41981).
* [@Aaronepower](https://github.com/Aaronepower) updated [releases notes for 1.18](https://github.com/rust-lang/rust/pull/41953).
* [@neosilky](https://github.com/neosilky) updated [to trait bounds CSS in rustdoc](https://github.com/rust-lang/rust/pull/42131).
* [@kennytm](https://github.com/kennytm) introduced ['ui-run' test to compiletest](https://github.com/rust-lang/rust/pull/41968).
* [@mjkillough](https://github.com/mjkillough) documented [direct implementations on type aliases.](https://github.com/rust-lang/rust/pull/42027).
* [@oli-obk](https://github.com/oli-obk) changed [some notes into suggestions](https://github.com/rust-lang/rust/pull/42033).
* [@frewsxcv](https://github.com/frewsxcv) added [a few entries to the Unstable Book.](https://github.com/rust-lang/rust/pull/42122).
* [@euclio](https://github.com/euclio) removed ["much" from unicode diagnostic](https://github.com/rust-lang/rust/pull/42120).
* [@alex-ozdemir](https://github.com/alex-ozdemir) made [clearer error message for Duplicate Definition](https://github.com/rust-lang/rust/pull/42076).
* [@Idolf](https://github.com/Idolf) supported [#![deny(missing_docs)] together with #[proc_macro_derive]](https://github.com/rust-lang/rust/pull/41747).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [better error message when == operator is badly used](https://github.com/rust-lang/rust/pull/41559), made [--extend-css stable](https://github.com/rust-lang/rust/pull/41700) and added [warnings when rustdoc html rendering differs](https://github.com/rust-lang/rust/pull/41991).

# Recent doc contributions

* [@estebank](https://github.com/estebank) made [unsatisfied trait bounds note multiline](https://github.com/rust-lang/rust/pull/41489).
* [@abonander](https://github.com/abonander) documented [the `proc_macro` feature in the Unstable Book](https://github.com/rust-lang/rust/pull/41476).
* [@est31](https://github.com/est31) added [lint for unused macros](https://github.com/rust-lang/rust/pull/41907).
* [@gamazeps](https://github.com/gamazeps) explained [why `thread::yield_now` could be used](https://github.com/rust-lang/rust/pull/41982), improved [`thread::Builder`'s doc](https://github.com/rust-lang/rust/pull/41994) and added [links to the `thread::LocalKey` doc](https://github.com/rust-lang/rust/pull/41995).
* [@dhardy](https://github.com/dhardy) added [loop_break_value documentation for The Book](https://github.com/rust-lang/rust/pull/41857).
* [@excaliburHisSheath](https://github.com/excaliburHisSheath) improved [docs in os::windows::ffi and os::windows::fs](https://github.com/rust-lang/rust/pull/41870).
* [@froydnj](https://github.com/froydnj) fixed [confusion about parts required for float formatting](https://github.com/rust-lang/rust/pull/41859).
* [@cuviper](https://github.com/cuviper) gave [a nicer error for non-Unicode arguments to rustc and rustdoc](https://github.com/rust-lang/rust/pull/42092).
* [@maccoda](https://github.com/maccoda) improved [std::env docs](https://github.com/rust-lang/rust/pull/42091).
* [@ollie27](https://github.com/ollie27) fixed [implementors list in Rustdoc's javascript](https://github.com/rust-lang/rust/pull/42096), corrected [some stability versions](https://github.com/rust-lang/rust/pull/42111) and displayed [`extern "C" fn` instead of `extern fn` in rustdoc](https://github.com/rust-lang/rust/pull/42001).
* [@citizen428](https://github.com/citizen428) added [documentation for `ExitStatus`](https://github.com/rust-lang/rust/pull/42024).
* [@seeekr](https://github.com/seeekr) fixed [typo in libstd/sync/mpsc/mod.rs docs](https://github.com/rust-lang/rust/pull/42079).
* [@pravic](https://github.com/pravic) fixed [regression introduced by jQuery removal](https://github.com/rust-lang/rust/pull/42080).
* [@tshepang](https://github.com/tshepang) improved [std::env docs](https://github.com/rust-lang/rust/pull/42070).
* [@faso](https://github.com/faso) fixed [a typo in contributing.md](https://github.com/rust-lang/rust/pull/42028).
* [@rap2hpoutre](https://github.com/rap2hpoutre) improved [collapse toggle render (css)](https://github.com/rust-lang/rust/pull/42011).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [help message if a FnOnce is moved](https://github.com/rust-lang/rust/pull/41772).

# Meetings

Next meeting will be on Wednesday 24th of May 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
