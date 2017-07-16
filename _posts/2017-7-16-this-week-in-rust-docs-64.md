---
layout: post
title: This Week in Rust Docs 64
date: 2017-7-16
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

[@steveklabnik](https://github.com/steveklabnik) ended the first version of [the rewrite of rustdoc](https://github.com/steveklabnik/rustdoc) using RLS. It's far from done but don't hesitate to give it a try!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@oli-obk](https://github.com/oli-obk) changed [some notes into suggestions](https://github.com/rust-lang/rust/pull/42033).
* [@Aaronepower](https://github.com/Aaronepower) updated [releases notes for 1.19](https://github.com/rust-lang/rust/pull/42503).
* [@rthomas](https://github.com/rthomas) updated [docs on Error struct](https://github.com/rust-lang/rust/pull/42837).
* [@Emilgardis](https://github.com/Emilgardis) fixed [wrong report on closure args mismatch when a ref is expected but not found](https://github.com/rust-lang/rust/pull/42270).
* [@gaurikholkar](https://github.com/gaurikholkar) reordered [span suggestions to appear below main labels](https://github.com/rust-lang/rust/pull/43251).
* [@Others](https://github.com/Others) improved [panic docs for Instant::duration_since](https://github.com/rust-lang/rust/pull/43256).
* [@RalfJung](https://github.com/RalfJung) clarified [wording for E0122](https://github.com/rust-lang/rust/pull/43176).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings when rustdoc html rendering differs](https://github.com/rust-lang/rust/pull/41991), added [errors when doc comments are added where they're unused](https://github.com/rust-lang/rust/pull/43009), added [TryFrom implementation for bool, f32 and f64](https://github.com/rust-lang/rust/pull/43220) and added [a message when a variable name collides with a function name](https://github.com/rust-lang/rust/pull/43173).

# Recent doc contributions

* [@dns2utf8](https://github.com/dns2utf8) added [hint about the return code of panic!](https://github.com/rust-lang/rust/pull/42670).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) refactored [pretty printing slightly](https://github.com/rust-lang/rust/pull/42897) and tested [src/doc once more](https://github.com/rust-lang/rust/pull/43152).
* [@steveklabnik](https://github.com/steveklabnik) updated [the books.](https://github.com/rust-lang/rust/pull/43240) and added [the Code of Conduct to the repository](https://github.com/rust-lang/rust/pull/43187).
* [@kennytm](https://github.com/kennytm) fixed [minor typo in std::path documentation.](https://github.com/rust-lang/rust/pull/43229).
* [@Havvy](https://github.com/Havvy) documented [what happens on failure in path ext is_file is_dir](https://github.com/rust-lang/rust/pull/42926).
* [@jgallag88](https://github.com/jgallag88) added [warning to BufWriter documentation](https://github.com/rust-lang/rust/pull/43136).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) cleaned up [some code](https://github.com/rust-lang/rust/pull/43006), added [spacing between trait functions in rustdoc](https://github.com/rust-lang/rust/pull/43130) and added [a failure in case nothing to run was found](https://github.com/rust-lang/rust/pull/43145).

# Meetings

Next meeting will be on Wednesday 19th of July 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
