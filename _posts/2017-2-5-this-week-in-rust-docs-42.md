---
layout: post
title: This Week in Rust Docs 42
date: 2017-2-5
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

* [@zackmdavis](https://github.com/zackmdavis) improved [error message when two-arg assert_eq! receives a trailing comma](https://github.com/rust-lang/rust/pull/39554) and used [help rather than span note for no method error; a slight rephrasing](https://github.com/rust-lang/rust/pull/39441).
* [@keeperofdakeys](https://github.com/keeperofdakeys) gave [a better error message for unknown derive messages](https://github.com/rust-lang/rust/pull/39444).
* [@APTy](https://github.com/APTy) added [docs and tests for join_multicast_{v4,v6}](https://github.com/rust-lang/rust/pull/39007).
* [@cengizIO](https://github.com/cengizIO) improved [error message for uninferrable types #38812](https://github.com/rust-lang/rust/pull/39361).
* [@JordiPolo](https://github.com/JordiPolo) changed [deprecation warning to indicate custom derive support was removed](https://github.com/rust-lang/rust/pull/39545).
* [@nagisa](https://github.com/nagisa) expanded [documentation of process::exit and exec](https://github.com/rust-lang/rust/pull/38518).
* [@mgattozzi](https://github.com/mgattozzi) fixed [full path being output with `rustdoc -h`](https://github.com/rust-lang/rust/pull/39312).
* [@rspeer](https://github.com/rspeer) fixed [a misleading statement in `Iterator.nth()`](https://github.com/rust-lang/rust/pull/39174).
* [@bluecereal](https://github.com/bluecereal) updated [if-let.md](https://github.com/rust-lang/rust/pull/38436).
* [@oli-obk](https://github.com/oli-obk) distinguished [guesses from suggestions](https://github.com/rust-lang/rust/pull/39458).
* [@estebank](https://github.com/estebank) highlighted [code in `rustc --explain`](https://github.com/rust-lang/rust/pull/39300), pointed [to enclosing block/fn on nested unsafe](https://github.com/rust-lang/rust/pull/39202) and detected [missing `;` on methods with return type `()`](https://github.com/rust-lang/rust/pull/39231).
* [@phungleson](https://github.com/phungleson) fixed [short hand struct doc](https://github.com/rust-lang/rust/pull/39459) and removed [suggestions to use things which weren't found either](https://github.com/rust-lang/rust/pull/39443).
* [@chriskrycho](https://github.com/chriskrycho) documented [RFC 1623: static lifetime elision.](https://github.com/rust-lang/rust/pull/37928).
* [@durka](https://github.com/durka) removed [lie about #[cfg] from reference](https://github.com/rust-lang/rust/pull/39374).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [invalid module suggestion](https://github.com/rust-lang/rust/pull/38255), added [Debug implementations for libcollection structs](https://github.com/rust-lang/rust/pull/39002) and added [missing urls and small nits](https://github.com/rust-lang/rust/pull/39513).

# Recent doc contributions

* [@Wilfred](https://github.com/Wilfred) made a [minor grammar fix 'can not' -> 'cannot'](https://github.com/rust-lang/rust/pull/39389).
* [@mgattozzi](https://github.com/mgattozzi) added [clearer error message using `&str + &str`](https://github.com/rust-lang/rust/pull/39116).
* [@zackmdavis](https://github.com/zackmdavis) added a [note for individual lint name in messages set via lint group attribute](https://github.com/rust-lang/rust/pull/38103).
* [@federicomenaquintero](https://github.com/federicomenaquintero) clarified [the lack of mutability inside an Rc in std:rc](https://github.com/rust-lang/rust/pull/39299).
* [@alexcrichton](https://github.com/alexcrichton) suppressed [warnings/errors with rustdoc --test](https://github.com/rust-lang/rust/pull/39354).
* [@brson](https://github.com/brson) updated [relnotes for 1.15.1](https://github.com/rust-lang/rust/pull/39517).
* [@phungleson](https://github.com/phungleson) made [a tiny doc wording change](https://github.com/rust-lang/rust/pull/39486).
* [@apasel422](https://github.com/apasel422) updated [nomicon to describe `#[may_dangle]`](https://github.com/rust-lang/rust/pull/39196).
* [@tspiteri](https://github.com/tspiteri) marked [FFI functions with unsafety icon in rustdoc](https://github.com/rust-lang/rust/pull/39416).
* [@Freyskeyd](https://github.com/Freyskeyd) improved [doc cfg(test) and tests directory](https://github.com/rust-lang/rust/pull/38823).
* [@tshepang](https://github.com/tshepang) made [minor doc Option improvements](https://github.com/rust-lang/rust/pull/39405).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [information in case of markdown block code test failure](https://github.com/rust-lang/rust/pull/36320), added [missing urls in HashMap](https://github.com/rust-lang/rust/pull/39506) and added [missing url in convert module](https://github.com/rust-lang/rust/pull/39407).

# Meetings

Next meeting will be on Wednesday 8th of February 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
