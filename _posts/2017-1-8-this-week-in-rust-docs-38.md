---
layout: post
title: This Week in Rust Docs 38
date: 2017-1-8
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

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [A-docs](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-docs) tagged issues on GitHub!

# Waiting for merge

* [@chris-morgan](https://github.com/chris-morgan) fixed [a couple of bad Markdown links](https://github.com/rust-lang/rust/pull/38922) and fixed [rustdoc highlighting of `&` and `*`](https://github.com/rust-lang/rust/pull/38569).
* [@petrochenkov](https://github.com/petrochenkov) resolved: [do not use "resolve"/"resolution" in error messages](https://github.com/rust-lang/rust/pull/38890).
* [@estebank](https://github.com/estebank) suggested [solutions for `fn foo(&foo: Foo)`](https://github.com/rust-lang/rust/pull/38605), removed [`note: ` prefix from type mismatch errors](https://github.com/rust-lang/rust/pull/38902) and escaped [the deprecated and unstable reason text in rustdoc](https://github.com/rust-lang/rust/pull/38244).
* [@steveklabnik](https://github.com/steveklabnik) improved [safety warning on ptr::swap](https://github.com/rust-lang/rust/pull/38910).
* [@liigo](https://github.com/liigo) added [suggestions of #[macro_use] in every case for undefined macros](https://github.com/rust-lang/rust/pull/37910).
* [@frewsxcv](https://github.com/frewsxcv) expanded [{Path,OsStr}::{to_str,to_string_lossy} doc examples.](https://github.com/rust-lang/rust/pull/38839), clarified [behavior of `VecDeque::insert`.](https://github.com/rust-lang/rust/pull/38581) and clarified [zero-value behavior of `ctlz`/`cttz` intrinsics.](https://github.com/rust-lang/rust/pull/38310).
* [@Manishearth](https://github.com/Manishearth) improved [rustdoc rendering for unstable features](https://github.com/rust-lang/rust/pull/38843) and added [more docs for CoerceUnsized and Unsize](https://github.com/rust-lang/rust/pull/38816).
* [@nagisa](https://github.com/nagisa) expanded [documentation of process::exit and exec](https://github.com/rust-lang/rust/pull/38518).
* [@derekdreery](https://github.com/derekdreery) updated [vec.rs](https://github.com/rust-lang/rust/pull/38874).
* [@linclark](https://github.com/linclark) add [error explanation for E0328.](https://github.com/rust-lang/rust/pull/38108).
* [@shahn](https://github.com/shahn) clarified [Extend behaviour wrt existing keys](https://github.com/rust-lang/rust/pull/38636).
* [@F001](https://github.com/F001) updated [usage of rustc](https://github.com/rust-lang/rust/pull/38841).
* [@emilio](https://github.com/emilio) added [an attribute to ignore collecting tests per-item in rustdoc](https://github.com/rust-lang/rust/pull/38825).
* [@ShaunKarran](https://github.com/ShaunKarran) fixed [docs for TcpListener example](https://github.com/rust-lang/rust/pull/38845).
* [@ollie27](https://github.com/ollie27) fixed [typo in tuple docs](https://github.com/rust-lang/rust/pull/38836).
* [@Freyskeyd](https://github.com/Freyskeyd) improved [doc for cfg(test) and tests directory](https://github.com/rust-lang/rust/pull/38823).
* [@cbreeden](https://github.com/cbreeden) updated [sign formatting for numeric types in docs](https://github.com/rust-lang/rust/pull/38704).
* [@rkruppe](https://github.com/rkruppe) replaced [loop {} with abort() in The Book](https://github.com/rust-lang/rust/pull/38138).
* [@bombless](https://github.com/bombless) fixed [doc for `escape_debug`](https://github.com/rust-lang/rust/pull/38629).
* [@chriskrycho](https://github.com/chriskrycho) documented [RFC 1623: static lifetime elision.](https://github.com/rust-lang/rust/pull/37928).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [a distinct error code and description for "main function has wrong prototype"](https://github.com/rust-lang/rust/pull/38819), added [instant doc](https://github.com/rust-lang/rust/pull/38362), fixed [invalid module suggestion](https://github.com/rust-lang/rust/pull/38255), added [ref suggestion](https://github.com/rust-lang/rust/pull/37658) and added [information in case of markdown block code test failure](https://github.com/rust-lang/rust/pull/36320).

# Recent doc contributions

* [@estebank](https://github.com/estebank) disambiguated [Implementors when the type name is not unique in rustdoc](https://github.com/rust-lang/rust/pull/38414).
* [@jonathandturner](https://github.com/jonathandturner) fixed [E0088/E0090](https://github.com/rust-lang/rust/pull/38859).
* [@sanxiyn](https://github.com/sanxiyn) removed [rustdoc ICE when an unstable feature is used](https://github.com/rust-lang/rust/pull/38773).
* [@steveklabnik](https://github.com/steveklabnik) documented [custom derive](https://github.com/rust-lang/rust/pull/38770).
* [@clarcharr](https://github.com/clarcharr) reworded ['stupid' and 'crazy' in docs](https://github.com/rust-lang/rust/pull/38782).
* [@programble](https://github.com/programble) added [links to methods on all slice iterator struct docs](https://github.com/rust-lang/rust/pull/38711).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [missing example for Thread struct](https://github.com/rust-lang/rust/pull/38548).

# Meetings

Next meeting will be on Wednesday 11th of January 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
