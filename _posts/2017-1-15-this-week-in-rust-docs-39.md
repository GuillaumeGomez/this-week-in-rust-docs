---
layout: post
title: This Week in Rust Docs 39
date: 2017-1-15
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

[@Manishearth](https://github.com/Manishearth) improved [rustdoc rendering for unstable features](https://github.com/rust-lang/rust/pull/38843)! The rendering is available on [nightly docs](https://doc.rust-lang.org/nightly/std/convert/trait.TryFrom.html).

Please take a look [to the next rust doc days planning reminder](https://users.rust-lang.org/t/reminder-planning-the-next-rust-doc-days/6901).

The topic to propose crates for the Rust Doc Days is still open and waiting for contributions [here](https://users.rust-lang.org/t/call-for-proposals-for-next-rust-doc-days-crates/6685). Please take a look!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on GitHub!

# Waiting for merge

* [@ollie27](https://github.com/ollie27) gave [primitive types stability attributes in rustdoc](https://github.com/rust-lang/rust/pull/39076).
* [@radix](https://github.com/radix) made a [minor improvement to strange grammar in E0525](https://github.com/rust-lang/rust/pull/39072).
* [@frewsxcv](https://github.com/frewsxcv) added [doc examples & description in `std::os::unix::ffi`.](https://github.com/rust-lang/rust/pull/39065), made [minor improvements to docs in std::env structures/functions.](https://github.com/rust-lang/rust/pull/39028) and added ['platform-specific' section to `sleep_ms` to match `sleep`.](https://github.com/rust-lang/rust/pull/38761).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [missing blank space issue](https://github.com/rust-lang/rust/pull/39069), added [information in case of markdown block code test failure](https://github.com/rust-lang/rust/pull/36320), added [a distinct error code and description for "main function has wrong prototype](https://github.com/rust-lang/rust/pull/38819), added [ref suggestion](https://github.com/rust-lang/rust/pull/37658) and fixed [invalid module suggestion](https://github.com/rust-lang/rust/pull/38255).

* [@jmdyck](https://github.com/jmdyck) added [a link to the second edition of The Book](https://github.com/rust-lang/rust/pull/39043).
* [@steveklabnik](https://github.com/steveklabnik) fixed [wording around sort guarantees](https://github.com/rust-lang/rust/pull/38961).
* [@estebank](https://github.com/estebank) taught [diagnostics to highlight text](https://github.com/rust-lang/rust/pull/38955) and provided [disambiguated syntax for candidates in E0034](https://github.com/rust-lang/rust/pull/38168).
* [@APTy](https://github.com/APTy) added [docs and tests for join_multicast_{v4,v6}](https://github.com/rust-lang/rust/pull/39007).
* [@brson](https://github.com/brson) added [1.15 release notes](https://github.com/rust-lang/rust/pull/38966) and removed [all "consider using an explicit lifetime parameter" sug…](https://github.com/rust-lang/rust/pull/37057).
* [@federicomenaquintero](https://github.com/federicomenaquintero) documented [the optional extra arguments to assert_eq!() / assert_ne!()](https://github.com/rust-lang/rust/pull/38247).
* [@emilio](https://github.com/emilio) added [an attribute to ignore collecting tests per-item in rustdoc](https://github.com/rust-lang/rust/pull/38825).
* [@chris-morgan](https://github.com/chris-morgan) fixed [a couple of bad Markdown links](https://github.com/rust-lang/rust/pull/38922).
* [@insaneinside](https://github.com/insaneinside) updated [src/libcore/ops.rs docs for RFC#1228 (Placement Left Arrow)](https://github.com/rust-lang/rust/pull/38930).
* [@nagisa](https://github.com/nagisa) expanded [documentation of process::exit and exec](https://github.com/rust-lang/rust/pull/38518).
* [@linclark](https://github.com/linclark) added [error explanation for E0328.](https://github.com/rust-lang/rust/pull/38108).
* [@chriskrycho](https://github.com/chriskrycho) documented [RFC 1623: static lifetime elision.](https://github.com/rust-lang/rust/pull/37928).
* [@utkarshkukreti](https://github.com/utkarshkukreti) replaced [all `try!` with `?` in documentation examples](https://github.com/rust-lang/rust/pull/38648).
* [@ConnyOnny](https://github.com/ConnyOnny) added warning [for match enum in The Book](https://github.com/rust-lang/rust/pull/38794).

# Recent doc contributions

* [@chris-morgan](https://github.com/chris-morgan) fixed [rustdoc highlighting of `&` and `*`](https://github.com/rust-lang/rust/pull/38569).
* [@petrochenkov](https://github.com/petrochenkov) fixed [docs for min/max algorithms](https://github.com/rust-lang/rust/pull/38995).
* [@estebank](https://github.com/estebank) escaped [the deprecated and unstable reason text in rustdoc](https://github.com/rust-lang/rust/pull/38244) and taught [diagnostics to correct margin of multiline messages](https://github.com/rust-lang/rust/pull/38916).
* [@steveklabnik](https://github.com/steveklabnik) improved [safety warning on ptr::swap](https://github.com/rust-lang/rust/pull/38910).
* [@frewsxcv](https://github.com/frewsxcv) expanded [{Path,OsStr}::{to_str,to_string_lossy} doc examples](https://github.com/rust-lang/rust/pull/38839), clarified [behavior of `VecDeque::insert`](https://github.com/rust-lang/rust/pull/38581) and clarified [zero-value behavior of `ctlz`/`cttz` intrinsics](https://github.com/rust-lang/rust/pull/38310).
* [@Manishearth](https://github.com/Manishearth) improved [rustdoc rendering for unstable features](https://github.com/rust-lang/rust/pull/38843), added [more docs for CoerceUnsized and Unsize](https://github.com/rust-lang/rust/pull/38816) and removed [restrictions on docs in compiler-docs mode](https://github.com/rust-lang/rust/pull/38929).
* [@F001](https://github.com/F001) updated [usage of rustc](https://github.com/rust-lang/rust/pull/38841).
* [@ollie27](https://github.com/ollie27) fixed [typo in tuple docs](https://github.com/rust-lang/rust/pull/38836).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [instant doc](https://github.com/rust-lang/rust/pull/38362), added [missing doc examples for Mutex](https://github.com/rust-lang/rust/pull/38965) and added [missing links and examples for path modules and structs](https://github.com/rust-lang/rust/pull/38946).
* [@stjepang](https://github.com/stjepang) changed [`to_owned` to `to_string` in docs](https://github.com/rust-lang/rust/pull/39024).
* [@est31](https://github.com/est31) added [tidy check for lang gate tests](https://github.com/rust-lang/rust/pull/38914).
* [@behnam](https://github.com/behnam) fixed [typo in documentation](https://github.com/rust-lang/rust/pull/39027).
* [@BenWiederhake](https://github.com/BenWiederhake) fixed [some typos in Nomicon](https://github.com/rust-lang/rust/pull/38994).
* [@minaguib](https://github.com/minaguib) fixed [docs](https://github.com/rust-lang/rust/pull/38799).

# Meetings

Next meeting will be on Wednesday 18th of January 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
