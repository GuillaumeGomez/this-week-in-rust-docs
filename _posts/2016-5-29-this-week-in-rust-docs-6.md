---
layout: post
title: This Week in Rust Docs 6
date: 2016-05-29
---

Hello and welcome to *This Week in Rust Docs*!

*This Week in Rust Docs* is openly developed [on GitHub](https://github.com/GuillaumeGomez/this-week-in-rust-docs).
If you find any errors in this week's issue, [please submit a PR](https://github.com/GuillaumeGomez/this-week-in-rust-docs/pulls).

And of course, don't forget to look at the docs:

* [Stable](https://doc.rust-lang.org/)
* [Beta](http://doc.rust-lang.org/beta/)
* [Nightly](http://doc.rust-lang.org/nightly/)

This week's edition was edited by: [GuillaumeGomez](https://github.com/GuillaumeGomez).

# Latest news

The [Normalization for long error codes explanations RFC](https://github.com/rust-lang/rfcs/pull/1567) entered its final comment period!

[@pnkfelix](https://github.com/pnkfelix) proposed [to rewrite all the code examples to be song of fire and internal-compiler-error themed](https://github.com/rust-lang/rust/pull/33675#issuecomment-219609913). I think we'll try to put it in place! :p

# Current opened issues

For now, here are the two big issues opened for Rust documentation:

 * [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
 * [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They both need help to move forward so any contribution is very welcome!

There are currently around 50 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on github!

# Recent doc contributions

We had a busy week, thanks to all contributors!

* [@Manishearth](https://github.com/Manishearth) added [doc snippets for trait impls, with a read more link](https://github.com/rust-lang/rust/pull/33679)
* [@lqd](https://github.com/lqd) made [the #[stable(since)] version attribute clearer with a tooltip](https://github.com/rust-lang/rust/pull/33705).
* [@golddranks](https://github.com/golddranks) added [a big-picture explanation for thread::park() & co.](https://github.com/rust-lang/rust/pull/33665).
* [@rkruppe](https://github.com/rkruppe) reworded the [short diagnostic for E0509](https://github.com/rust-lang/rust/pull/33676).
* [@tshepang](https://github.com/tshepang) made a lot of small improvements. Take a look [here](https://github.com/rust-lang/rust/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+33603+33604+33605+33633+33634+33635) to see the list!
* [@alex-ozdemir](https://github.com/alex-ozdemir) added [a `rustdoc` shortcut for collapse/expand all](https://github.com/rust-lang/rust/pull/33765).
* [@postmodern](https://github.com/postmodern) clarified [the English translation of `?Sized`](https://github.com/rust-lang/rust/pull/33747).
* [@crimsun](https://github.com/crimsun) resolved [a rustdoc crash](https://github.com/rust-lang/rust/pull/33702).
* [@dns2utf8](https://github.com/dns2utf8) clarified [docs for sort(&mut self)](https://github.com/rust-lang/rust/pull/33746).

* [@oli-obk](https://github.com/oli-obk) added [display for enum variant fields in docs](https://github.com/rust-lang/rust/pull/33867).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) improved [E0084 error explanation](https://github.com/rust-lang/rust/pull/33865), fixed [compile_fail tag](https://github.com/rust-lang/rust/pull/33793), added [new error code tests](https://github.com/rust-lang/rust/pull/33866), fixed [invalid background color in stability elements](https://github.com/rust-lang/rust/pull/33829).

# Meetings

Next meeting will be on Wednesday 1st of June 2016 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
