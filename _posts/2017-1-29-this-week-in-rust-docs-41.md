---
layout: post
title: This Week in Rust Docs 41
date: 2017-1-29
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

* [@Wilfred](https://github.com/Wilfred) made a [minor grammar fix 'can not' -> 'cannot'](https://github.com/rust-lang/rust/pull/39389).
* [@cengizIO](https://github.com/cengizIO) improved [error message for uninferrable types](https://github.com/rust-lang/rust/pull/39361).
* [@mgattozzi](https://github.com/mgattozzi) added [clearer error message using `&str + &str`](https://github.com/rust-lang/rust/pull/39116) and fixed [full path being output with `rustdoc -h`](https://github.com/rust-lang/rust/pull/39312).
* [@durka](https://github.com/durka) removed [lie about #[cfg] from reference](https://github.com/rust-lang/rust/pull/39374).
* [@canndrew](https://github.com/canndrew) added [warning for () to ! switch](https://github.com/rust-lang/rust/pull/39009).
* [@zackmdavis](https://github.com/zackmdavis) added a [note for individual lint name in messages set via lint group attribute](https://github.com/rust-lang/rust/pull/38103).
* [@jrmuizel](https://github.com/jrmuizel) removed [obsolete documentation about drop-flags](https://github.com/rust-lang/rust/pull/39304).
* [@estebank](https://github.com/estebank) highlighted [code in `rustc --explain`](https://github.com/rust-lang/rust/pull/39300).
* [@federicomenaquintero](https://github.com/federicomenaquintero) clarified [the lack of mutability inside an Rc in std:rc](https://github.com/rust-lang/rust/pull/39299).
* [@rspeer](https://github.com/rspeer) fixed [a misleading statement in `Iterator.nth()`](https://github.com/rust-lang/rust/pull/39174).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [information in case of markdown block code test failure](https://github.com/rust-lang/rust/pull/36320).

# Recent doc contributions

* [@frewsxcv](https://github.com/frewsxcv) added [more references between lowercase/uppercase operations.](https://github.com/rust-lang/rust/pull/39233) and added [doc examples for `std::ffi::OsString` fucntions/methods.](https://github.com/rust-lang/rust/pull/39221).
* [@steveklabnik](https://github.com/steveklabnik) fixed [wording around sort guarantees](https://github.com/rust-lang/rust/pull/38961).
* [@DirkyJerky](https://github.com/DirkyJerky) added [docs for atomic orderings: link to the 'nomicon article for further reading](https://github.com/rust-lang/rust/pull/39200).
* [@cesarb](https://github.com/cesarb) updated The Book: [size and align in trait object vtables are used](https://github.com/rust-lang/rust/pull/39191).
* [@linclark](https://github.com/linclark) added [error explanation for E0328](https://github.com/rust-lang/rust/pull/38108).
* [@jtxx000](https://github.com/jtxx000) fixed [typo in librustc_trans/collector.rs](https://github.com/rust-lang/rust/pull/39378).
* [@osa1](https://github.com/osa1) fixed [typos in libsyntax/tokenstream.rs](https://github.com/rust-lang/rust/pull/39360).
* [@brson](https://github.com/brson) removed [all "consider using an explicit lifetime parameter" suggestions](https://github.com/rust-lang/rust/pull/37057).
* [@stjepang](https://github.com/stjepang) rewrote [the first sentence in slice::sort](https://github.com/rust-lang/rust/pull/39314).
* [@ollie27](https://github.com/ollie27) fixed [a few links in the docs](https://github.com/rust-lang/rust/pull/39344).
* [@king6cong](https://github.com/king6cong) made a [doc comment typo fix](https://github.com/rust-lang/rust/pull/39321), reworded [a doc comment rewording](https://github.com/rust-lang/rust/pull/39267) and improved [a comment wording](https://github.com/rust-lang/rust/pull/39238).
* [@estebank](https://github.com/estebank) pointed [to immutable arg/fields when trying to use as &mut](https://github.com/rust-lang/rust/pull/39139) and fixed [multiple labels when some don't have message](https://github.com/rust-lang/rust/pull/39214).
* [@das-g](https://github.com/das-g) fixed [book: refer to `add_two` as "tested function"](https://github.com/rust-lang/rust/pull/39278).
* [@ConnyOnny](https://github.com/ConnyOnny) updted [match enum warning in The Book](https://github.com/rust-lang/rust/pull/38794).
* [@Wilfred](https://github.com/Wilfred) added [missing URL to release notes](https://github.com/rust-lang/rust/pull/39248).
* [@Eijebong](https://github.com/Eijebong) fixed [minor typo](https://github.com/rust-lang/rust/pull/39242).
* [@utkarshkukreti](https://github.com/utkarshkukreti) replaced [all `try!` with `?` in documentation examples](https://github.com/rust-lang/rust/pull/38648).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing urls for OsStr and OsString](https://github.com/rust-lang/rust/pull/39224), forced [backline on all where in docs](https://github.com/rust-lang/rust/pull/39222), removed [doc generation if doc comments only filled with 'white' characters](https://github.com/rust-lang/rust/pull/39340), added [note for E0117](https://github.com/rust-lang/rust/pull/39306), added [a distinct error code and description for "main function has wrong type"](https://github.com/rust-lang/rust/pull/38819) and added [missing urls for array docs](https://github.com/rust-lang/rust/pull/39276).

# Meetings

Next meeting will be on Wednesday 1st of February 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
