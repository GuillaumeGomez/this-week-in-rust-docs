---
layout: post
title: This Week in Rust Docs 59
date: 2017-6-3
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

* [@kennytm](https://github.com/kennytm) introduced ['ui-run' test to compiletest](https://github.com/rust-lang/rust/pull/41968).
* [@mjkillough](https://github.com/mjkillough) documented [direct implementations on type aliases.](https://github.com/rust-lang/rust/pull/42027).
* [@oli-obk](https://github.com/oli-obk) changed [some notes into suggestions](https://github.com/rust-lang/rust/pull/42033).
* [@alex-ozdemir](https://github.com/alex-ozdemir) made [clearer error message for Duplicate Definition](https://github.com/rust-lang/rust/pull/42076).
* [@irfanhudda](https://github.com/irfanhudda) improved [documentation of next_power_of_two](https://github.com/rust-lang/rust/pull/40706).
* [@pwoolcoc](https://github.com/pwoolcoc) added [`allow_fail` test attribute](https://github.com/rust-lang/rust/pull/42219).
* [@photoszzt](https://github.com/photoszzt) made [better suggestion for unknown method](https://github.com/rust-lang/rust/pull/42391).
* [@clarcharr](https://github.com/clarcharr) made [rustdoc.js use license comments.](https://github.com/rust-lang/rust/pull/42307).
* [@steveklabnik](https://github.com/steveklabnik) created [the Rustdoc book](https://github.com/rust-lang/rust/pull/42378).
* [@ollie27](https://github.com/ollie27) hid [`self: Box<Self>` in list of deref methods in rustdoc](https://github.com/rust-lang/rust/pull/42394).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) printed [the two types in the span label for transmute errors.](https://github.com/rust-lang/rust/pull/42304).
* [@Manishearth](https://github.com/Manishearth) changed [vec<T> pronunciation](https://github.com/rust-lang/rust/pull/42385).
* [@estebank](https://github.com/estebank) used [multiline note for trait suggestion](https://github.com/rust-lang/rust/pull/42383).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings when rustdoc html rendering differs](https://github.com/rust-lang/rust/pull/41991), added [E0602](https://github.com/rust-lang/rust/pull/42361) and added [E0603 error code](https://github.com/rust-lang/rust/pull/42387).

# Recent doc contributions

* [@gamazeps](https://github.com/gamazeps) expanded [`detach` documentation in `thread::JoinHande`](https://github.com/rust-lang/rust/pull/41981).
* [@Aaronepower](https://github.com/Aaronepower) updated [releases notes for 1.18](https://github.com/rust-lang/rust/pull/41953).
* [@clarcharr](https://github.com/clarcharr) clarified [docs on implementing Into](https://github.com/rust-lang/rust/pull/42126).
* [@tommyip](https://github.com/tommyip) explained [why a closure is `FnOnce` in closure errors](https://github.com/rust-lang/rust/pull/42196).
* [@stjepang](https://github.com/stjepang) unified [the docs of PartialEq, PartialOrd and Ord](https://github.com/rust-lang/rust/pull/42260) and clarified [the docs for align_of and its variants](https://github.com/rust-lang/rust/pull/42252).
* [@bjorn3](https://github.com/bjorn3) added [syntax highlight rust code in librustc/dep_graph/README.md](https://github.com/rust-lang/rust/pull/42355) and added [syntax highlight all rust code in librustc/traits/README.md](https://github.com/rust-lang/rust/pull/42311).
* [@frewsxcv](https://github.com/frewsxcv) rewrote [a couple `Receiver` doc examples](https://github.com/rust-lang/rust/pull/42372) and rewrote [doc examples for `Receiver::recv_timeout`](https://github.com/rust-lang/rust/pull/42347).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) added [note regarding parent module containing use statement](https://github.com/rust-lang/rust/pull/42283).
* [@steveklabnik](https://github.com/steveklabnik) updated [various book repos for the next release.](https://github.com/rust-lang/rust/pull/42353).
* [@brson](https://github.com/brson) updated [releases notes for 1.18](https://github.com/rust-lang/rust/pull/42338).
* [@mbrubeck](https://github.com/mbrubeck) added [[[T]] -> [T] examples to SliceConcatExt docs](https://github.com/rust-lang/rust/pull/42370).
* [@ollie27](https://github.com/ollie27) renamed [`Vector` and `FixedVector` to `Slice` and `Array` in rustdoc](https://github.com/rust-lang/rust/pull/42360) and cleaned up [associated const value rendering](https://github.com/rust-lang/rust/pull/42286).
* [@Manishearth](https://github.com/Manishearth) improved [error message for const extern fn](https://github.com/rust-lang/rust/pull/42319).
* [@rap2hpoutre](https://github.com/rap2hpoutre) fixed [links to "module-level documentation"](https://github.com/rust-lang/rust/pull/42329).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) updated [rustdoc man page](https://github.com/rust-lang/rust/pull/42180), added [new error codes](https://github.com/rust-lang/rust/pull/42264), added [new error codes next](https://github.com/rust-lang/rust/pull/42302) and fixed [signature by adding parens when needed in rustdoc](https://github.com/rust-lang/rust/pull/42318).

# Meetings

Next meeting will be on Wednesday 7th of June 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
