---
layout: post
title: This Week in Rust Docs 58
date: 2017-5-28
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

* [@gamazeps](https://github.com/gamazeps) expanded [`detach` documentation in `thread::JoinHande`](https://github.com/rust-lang/rust/pull/41981).
* [@Aaronepower](https://github.com/Aaronepower) updated [releases notes for 1.18](https://github.com/rust-lang/rust/pull/41953).
* [@kennytm](https://github.com/kennytm) introduced ['ui-run' test to compiletest](https://github.com/rust-lang/rust/pull/41968).
* [@mjkillough](https://github.com/mjkillough) documented [direct implementations on type aliases.](https://github.com/rust-lang/rust/pull/42027).
* [@oli-obk](https://github.com/oli-obk) changed [some notes into suggestions](https://github.com/rust-lang/rust/pull/42033).
* [@alex-ozdemir](https://github.com/alex-ozdemir) made [clearer error message for Duplicate Definition](https://github.com/rust-lang/rust/pull/42076).
* [@irfanhudda](https://github.com/irfanhudda) improved [documentation of next_power_of_two](https://github.com/rust-lang/rust/pull/40706).
* [@clarcharr](https://github.com/clarcharr) clarified [docs on implementing Into](https://github.com/rust-lang/rust/pull/42126).
* [@pwoolcoc](https://github.com/pwoolcoc) added [`allow_fail` test attribute](https://github.com/rust-lang/rust/pull/42219).
* [@tommyip](https://github.com/tommyip) explained [why a closure is `FnOnce` in closure errors](https://github.com/rust-lang/rust/pull/42196).
* [@stjepang](https://github.com/stjepang) unified [the docs of PartialEq, PartialOrd and Ord](https://github.com/rust-lang/rust/pull/42260) and clarified [the docs for align_of and its variants](https://github.com/rust-lang/rust/pull/42252).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings when rustdoc html rendering differs](https://github.com/rust-lang/rust/pull/41991), updated [rustdoc man page](https://github.com/rust-lang/rust/pull/42180) and added [new error codes](https://github.com/rust-lang/rust/pull/42264).

# Recent doc contributions

* [@gamazeps](https://github.com/gamazeps) added [`'static` and `Send` constraints explanations to `thread::spawn`](https://github.com/rust-lang/rust/pull/41980).
* [@neosilky](https://github.com/neosilky) updated [to trait bounds CSS in rustdoc](https://github.com/rust-lang/rust/pull/42131).
* [@frewsxcv](https://github.com/frewsxcv) added [a few entries to the Unstable Book.](https://github.com/rust-lang/rust/pull/42122).
* [@euclio](https://github.com/euclio) removed ["much" from unicode diagnostic](https://github.com/rust-lang/rust/pull/42120).
* [@nical](https://github.com/nical) updated [to Rc and Arc documentation to favor the Rc::clone(&ptr) syntax](https://github.com/rust-lang/rust/pull/42137).
* [@citizen428](https://github.com/citizen428) updated [documentation for indexing/slicing methods](https://github.com/rust-lang/rust/pull/42236) and changed [error count messages](https://github.com/rust-lang/rust/pull/42150).
* [@king6cong](https://github.com/king6cong) reworded [doc](https://github.com/rust-lang/rust/pull/42241).
* [@charliesome](https://github.com/charliesome) fixed ['associate type' typo](https://github.com/rust-lang/rust/pull/42216).
* [@Havvy](https://github.com/Havvy) documented [drop more](https://github.com/rust-lang/rust/pull/42159).
* [@SamWhited](https://github.com/SamWhited) fixed [broken link to nomicon in Unsize docs](https://github.com/rust-lang/rust/pull/42195).
* [@projektir](https://github.com/projektir) added [links to option::Option](https://github.com/rust-lang/rust/pull/42163).
* [@ollie27](https://github.com/ollie27) fixed [names of items in cross crate reexported modules in rustdoc](https://github.com/rust-lang/rust/pull/42145).
* [@Wallacoloo](https://github.com/Wallacoloo) mentionned [Vec::into_boxed_slice in documentation of [T]::into_vec](https://github.com/rust-lang/rust/pull/42151).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [better error message when == operator is badly used](https://github.com/rust-lang/rust/pull/41559), made [--extend-css stable](https://github.com/rust-lang/rust/pull/41700), added [missing urls for OsStr docs](https://github.com/rust-lang/rust/pull/42198) and added [missing links for CStr and CString](https://github.com/rust-lang/rust/pull/42152).

# Meetings

Next meeting will be on Wednesday 31st of May 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
