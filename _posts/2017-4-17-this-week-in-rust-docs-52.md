---
layout: post
title: This Week in Rust Docs 52
date: 2017-4-17
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

The jquery dependency [is being removed](https://github.com/rust-lang/rust/pull/41307) from the rustdoc javascript. When navigating in the docs, please check if everything's working as expected!

# Current opened issues

For now, here are the two big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@estebank](https://github.com/estebank) pointed [at fields that make the type recursive](https://github.com/rust-lang/rust/pull/40857), reduced [visual clutter of multiline start when possible](https://github.com/rust-lang/rust/pull/41245) and added [a way to get shorter spans until `char` for pointing at defs](https://github.com/rust-lang/rust/pull/41214).
* [@irfanhudda](https://github.com/irfanhudda) improved [documentation of next_power_of_two](https://github.com/rust-lang/rust/pull/40706).
* [@stepancheg](https://github.com/stepancheg) improved [BufRead::is_eof documentation](https://github.com/rust-lang/rust/pull/40747).
* [@maccoda](https://github.com/maccoda) improved [Convert docs](https://github.com/rust-lang/rust/pull/40987).
* [@mgattozzi](https://github.com/mgattozzi) updated [`Child` docs to not have a note section](https://github.com/rust-lang/rust/pull/40812).
* [@icefoxen](https://github.com/icefoxen) made [a tiny update to rustdoc CSS](https://github.com/rust-lang/rust/pull/40719).
* [@frewsxcv](https://github.com/frewsxcv) added [top level sections to the Unstable Book.](https://github.com/rust-lang/rust/pull/41295).
* [@cengizIO](https://github.com/cengizIO) moved [E0101 and E0102 logic into new E0282 mechanism](https://github.com/rust-lang/rust/pull/41236).
* [@jonhoo](https://github.com/jonhoo) renamed [compiler_barrier to compiler_fence](https://github.com/rust-lang/rust/pull/41262).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [a list of headings to the sidebar in rustdoc](https://github.com/rust-lang/rust/pull/41280).
* [@topecongiro](https://github.com/topecongiro) updated [docs of 'fence'](https://github.com/rust-lang/rust/pull/41217).
* [@alexeyzab](https://github.com/alexeyzab) fixed [old docs](https://github.com/rust-lang/rust/pull/41264).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [ref suggestion](https://github.com/rust-lang/rust/pull/37658), added [more explanation on RefCell::get_mut](https://github.com/rust-lang/rust/pull/40634), removed [jquery dependency](https://github.com/rust-lang/rust/pull/41307) and made [hoedown big comeback](https://github.com/rust-lang/rust/pull/41290).

# Recent doc contributions

* [@QuietMisdreavus](https://github.com/QuietMisdreavus) updated [formatting of fn signatures and where clauses to match style rfcs in rustdoc](https://github.com/rust-lang/rust/pull/41084).
* [@estebank](https://github.com/estebank) added [an explicit help message for binop type mismatch](https://github.com/rust-lang/rust/pull/40565), added [end line display of multiline annotations](https://github.com/rust-lang/rust/pull/41136) and used [proper span for tuple index parsed as float](https://github.com/rust-lang/rust/pull/41087).
* [@frewsxcv](https://github.com/frewsxcv) made a [couple minor improvements for tidy error handling](https://github.com/rust-lang/rust/pull/40653).
* [@sagebind](https://github.com/sagebind) improved [examples for ThreadId](https://github.com/rust-lang/rust/pull/41008).
* [@mgattozzi](https://github.com/mgattozzi) updated [ChildStderr docs to be clearer](https://github.com/rust-lang/rust/pull/40829).
* [@pirate](https://github.com/pirate) added [contribution instructions to stdlib docs](https://github.com/rust-lang/rust/pull/40765).
* [@projektir](https://github.com/projektir) added [channel error docs](https://github.com/rust-lang/rust/pull/41103), fixed [minor nits in primitive str](https://github.com/rust-lang/rust/pull/41243), updated [docs for std::sync::Weak](https://github.com/rust-lang/rust/pull/41240) and updated [docs for std::rc::Rc](https://github.com/rust-lang/rust/pull/41266).
* [@lukaramu](https://github.com/lukaramu) improved [std::hash docs](https://github.com/rust-lang/rust/pull/41125) and made [various improvements in std::collections docs](https://github.com/rust-lang/rust/pull/41286).
* [@palango](https://github.com/palango) improved [module documentation for std::f32 and std::f64](https://github.com/rust-lang/rust/pull/41122).
* [@tedsta](https://github.com/tedsta) updated [magenta error codes](https://github.com/rust-lang/rust/pull/41311).
* [@Aaron1011](https://github.com/Aaron1011) fixed [rustdoc infinitely recursing when an external crate reexports itself](https://github.com/rust-lang/rust/pull/41172).
* [@steveklabnik](https://github.com/steveklabnik) bumped [book repos](https://github.com/rust-lang/rust/pull/41281).
* [@nodakai](https://github.com/nodakai) removed [hoedown license](https://github.com/rust-lang/rust/pull/41183).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) fixed [invalid associated type rendering in rustdoc](https://github.com/rust-lang/rust/pull/41249).

# Meetings

Next meeting will be on Wednesday 19th of April 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
