---
layout: post
title: This Week in Rust Docs 60
date: 2017-6-11
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

* [@oli-obk](https://github.com/oli-obk) changed [some notes into suggestions](https://github.com/rust-lang/rust/pull/42033).
* [@alex-ozdemir](https://github.com/alex-ozdemir) made [clearer error message for Duplicate Definition](https://github.com/rust-lang/rust/pull/42076).
* [@pwoolcoc](https://github.com/pwoolcoc) added [`allow_fail` test attribute](https://github.com/rust-lang/rust/pull/42219).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) printed [the two types in the span label for transmute errors](https://github.com/rust-lang/rust/pull/42304).
* [@ollie27](https://github.com/ollie27) used [`create_dir_all` to create output directory in rustdoc](https://github.com/rust-lang/rust/pull/42572).
* [@maccoda](https://github.com/maccoda) completed [env docs](https://github.com/rust-lang/rust/pull/42579).
* [@birkenfeld](https://github.com/birkenfeld) added [dedicated docstrings to Sum/Product impl of Result](https://github.com/rust-lang/rust/pull/42570) and simplified [FromIterator example of Result](https://github.com/rust-lang/rust/pull/42569).
* [@Aaronepower](https://github.com/Aaronepower) updated [releases notes for 1.19](https://github.com/rust-lang/rust/pull/42503).
* [@ucarion](https://github.com/ucarion) explicated [what "Rc" and "Arc" stand for](https://github.com/rust-lang/rust/pull/42419).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings when rustdoc html rendering differs](https://github.com/rust-lang/rust/pull/41991), created [more error codes](https://github.com/rust-lang/rust/pull/42519), added [E0609](https://github.com/rust-lang/rust/pull/42585) and added [0608](https://github.com/rust-lang/rust/pull/42568).

# Recent doc contributions

* [@steveklabnik](https://github.com/steveklabnik) created [the Rustdoc book](https://github.com/rust-lang/rust/pull/42378).
* [@mjkillough](https://github.com/mjkillough) documented [direct implementations on type aliases](https://github.com/rust-lang/rust/pull/42027).
* [@irfanhudda](https://github.com/irfanhudda) improved [documentation of next_power_of_two](https://github.com/rust-lang/rust/pull/40706).
* [@photoszzt](https://github.com/photoszzt) made [better suggestion for unknown method](https://github.com/rust-lang/rust/pull/42391).
* [@clarcharr](https://github.com/clarcharr) made [rustdoc.js use license comments](https://github.com/rust-lang/rust/pull/42307).
* [@ollie27](https://github.com/ollie27) hid [`self: Box<Self>` in list of deref methods in rustdoc](https://github.com/rust-lang/rust/pull/42394) and renamed [`Vector` and `FixedVector` to `Slice` and `Array` in rustdoc](https://github.com/rust-lang/rust/pull/42360).
* [@Manishearth](https://github.com/Manishearth) changed [vec<T> pronunciation](https://github.com/rust-lang/rust/pull/42385).
* [@estebank](https://github.com/estebank) used [multiline note for trait suggestion](https://github.com/rust-lang/rust/pull/42383) and showed [trait method signature when impl differs](https://github.com/rust-lang/rust/pull/42362).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) skipped [printing for skipped doc tests](https://github.com/rust-lang/rust/pull/42485) and skipped [documentation files without ``` when running markdown tests](https://github.com/rust-lang/rust/pull/42437).
* [@xfq](https://github.com/xfq) updated [TRPL link in README.md](https://github.com/rust-lang/rust/pull/42558).
* [@tshepang](https://github.com/tshepang) improved [cell doc example](https://github.com/rust-lang/rust/pull/42551).
* [@frewsxcv](https://github.com/frewsxcv) added [doc examples for `CString` methods](https://github.com/rust-lang/rust/pull/42470) and improved [`Cow` method doc examples](https://github.com/rust-lang/rust/pull/42414).
* [@mbrubeck](https://github.com/mbrubeck) updated [step_by docs to say iterator instead of range](https://github.com/rust-lang/rust/pull/42510).
* [@citizen428](https://github.com/citizen428) updated [doc for the assert macros](https://github.com/rust-lang/rust/pull/42469).
* [@king6cong](https://github.com/king6cong) reworded [doc](https://github.com/rust-lang/rust/pull/42438).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [E0602](https://github.com/rust-lang/rust/pull/42361) and added [E0603 error code](https://github.com/rust-lang/rust/pull/42387).
* [@tommyip](https://github.com/tommyip) only [emit one error for `use foo::self;`](https://github.com/rust-lang/rust/pull/42580) and better [closure error message](https://github.com/rust-lang/rust/pull/42443).

# Meetings

Next meeting will be on Wednesday 14th of June 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
