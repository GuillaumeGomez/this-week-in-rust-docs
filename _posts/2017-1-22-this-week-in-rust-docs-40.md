---
layout: post
title: This Week in Rust Docs 40
date: 2017-1-22
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

Please take a look [to the next rust doc days planning reminder](https://users.rust-lang.org/t/reminder-planning-the-next-rust-doc-days/6901).

The topic to propose crates for the Rust Doc Days is still open and waiting for contributions [here](https://users.rust-lang.org/t/call-for-proposals-for-next-rust-doc-days-crates/6685). Please take a look!

# Current opened issues

For now, here are the two big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on GitHub!

# Waiting for merge

* [@frewsxcv](https://github.com/frewsxcv) added [more references between lowercase/uppercase operations.](https://github.com/rust-lang/rust/pull/39233).
* [@steveklabnik](https://github.com/steveklabnik) fixed [wording around sort guarantees](https://github.com/rust-lang/rust/pull/38961).
* [@bluecereal](https://github.com/bluecereal) updated [if-let.md](https://github.com/rust-lang/rust/pull/38436).
* [@nagisa](https://github.com/nagisa) expanded [documentation of process::exit and exec](https://github.com/rust-lang/rust/pull/38518).
* [@DirkyJerky](https://github.com/DirkyJerky) added [docs for atomic orderings: link to the 'nomicon article for further reading](https://github.com/rust-lang/rust/pull/39200).
* [@rspeer](https://github.com/rspeer) fixed [a misleading statement in `Iterator.nth()`](https://github.com/rust-lang/rust/pull/39174).
* [@cesarb](https://github.com/cesarb) updated The Book: [size and align in trait object vtables are used](https://github.com/rust-lang/rust/pull/39191).
* [@apasel422](https://github.com/apasel422) updated [nomicon to describe `#[may_dangle]`](https://github.com/rust-lang/rust/pull/39196).
* [@APTy](https://github.com/APTy) added [docs and tests for join_multicast_{v4,v6} for UDP socket](https://github.com/rust-lang/rust/pull/39007).
* [@linclark](https://github.com/linclark) added [error explanation for E0328](https://github.com/rust-lang/rust/pull/38108).
* [@Freyskeyd](https://github.com/Freyskeyd) improved [doc cfg(test) and tests directory](https://github.com/rust-lang/rust/pull/38823).
* [@insaneinside](https://github.com/insaneinside) updated [src/libcore/ops.rs docs for RFC#1228 (Placement Left Arrow)](https://github.com/rust-lang/rust/pull/38930).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing urls for OsStr and OsString](https://github.com/rust-lang/rust/pull/39224), added [information in case of markdown block code test failure](https://github.com/rust-lang/rust/pull/36320), forced [backline on all where in docs](https://github.com/rust-lang/rust/pull/39222), added ref [suggestion](https://github.com/rust-lang/rust/pull/37658) and fixed [invalid module suggestion](https://github.com/rust-lang/rust/pull/38255).

# Recent doc contributions

* [@ollie27](https://github.com/ollie27) gave [primitive types stability attributes in rustdoc](https://github.com/rust-lang/rust/pull/39076).
* [@radix](https://github.com/radix) made a [minor improvement to strange grammar in E0525](https://github.com/rust-lang/rust/pull/39072).
* [@frewsxcv](https://github.com/frewsxcv) added [doc examples & description in `std::os::unix::ffi`](https://github.com/rust-lang/rust/pull/39065), made [minor improvements to docs in std::env structures/functions](https://github.com/rust-lang/rust/pull/39028), added ['platform-specific' section to `sleep_ms` to match `sleep`](https://github.com/rust-lang/rust/pull/38761), added [doc examples for `std::ffi::OsString` fucntions/methods](https://github.com/rust-lang/rust/pull/39221), made [a few improvements to the slice docs](https://github.com/rust-lang/rust/pull/39165) and made [improvements to 'include' macro documentation](https://github.com/rust-lang/rust/pull/38457).
* [@brson](https://github.com/brson) added [1.15 release notes](https://github.com/rust-lang/rust/pull/38966).
* [@federicomenaquintero](https://github.com/federicomenaquintero) documented [the optional extra arguments to assert_eq!() / assert_ne!()](https://github.com/rust-lang/rust/pull/38247).
* [@chris-morgan](https://github.com/chris-morgan) fixed [a couple of bad Markdown links](https://github.com/rust-lang/rust/pull/38922).
* [@ranma42](https://github.com/ranma42) documented [that `Metadata` can be obtained from `symlink_metadata`](https://github.com/rust-lang/rust/pull/39203).
* [@TheCycoONE](https://github.com/TheCycoONE) clarified [when range is removed by drain](https://github.com/rust-lang/rust/pull/39135).
* [@grimreaper](https://github.com/grimreaper) fixed a [minor typo](https://github.com/rust-lang/rust/pull/39121).
* [@king6cong](https://github.com/king6cong) improved [doc wording](https://github.com/rust-lang/rust/pull/39115).
* [@richard-imaoka](https://github.com/richard-imaoka) added [error explanation for E0491](https://github.com/rust-lang/rust/pull/39091).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [missing blank space issue](https://github.com/rust-lang/rust/pull/39069) and specified [the result of integer cast on boolean](https://github.com/rust-lang/rust/pull/39210).

# Meetings

Next meeting will be on Wednesday 25th of January 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
