---
layout: post
title: This Week in Rust Docs 65
date: 2017-7-23
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

* [@Emilgardis](https://github.com/Emilgardis) fixed [wrong report on closure args mismatch when a ref is expected but not found](https://github.com/rust-lang/rust/pull/42270).
* [@RalfJung](https://github.com/RalfJung) clarified [wording for E0122](https://github.com/rust-lang/rust/pull/43176).
* [@afshinm](https://github.com/afshinm) added [`+` sign to static lifetime help message](https://github.com/rust-lang/rust/pull/43363).
* [@oli-obk](https://github.com/oli-obk) adjusted [new suggestions to the suggestion guidelines](https://github.com/rust-lang/rust/pull/43386).
* [@waywardmonkeys](https://github.com/waywardmonkeys) fixed [some doc comment typos](https://github.com/rust-lang/rust/pull/43428).
* [@mandeep](https://github.com/mandeep) added [generic example of std::ops::Sub in doc comments](https://github.com/rust-lang/rust/pull/43413).
* [@xliiv](https://github.com/xliiv) added [simple docs example for struct Cell](https://github.com/rust-lang/rust/pull/43423).
* [@stjepang](https://github.com/stjepang) clarified [that sort_unstable is deterministic](https://github.com/rust-lang/rust/pull/43374).
* [@tshepang](https://github.com/tshepang) made [into_iter example more concise](https://github.com/rust-lang/rust/pull/43409).
* [@cuviper](https://github.com/cuviper) corrected [the spelling of "homogeneous"](https://github.com/rust-lang/rust/pull/43401).
* [@s3rvac](https://github.com/s3rvac) added [a missing verb to the description of std::process::ExitStatus::success()](https://github.com/rust-lang/rust/pull/43379).
* [@kennytm](https://github.com/kennytm) exposed [all OS-specific modules in libstd doc](https://github.com/rust-lang/rust/pull/43348).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings when rustdoc html rendering differs](https://github.com/rust-lang/rust/pull/41991), added [lint for when doc comments are added where they're unused](https://github.com/rust-lang/rust/pull/43009) and removed [warn on unused field on union](https://github.com/rust-lang/rust/pull/43397).

# Recent doc contributions

* [@oli-obk](https://github.com/oli-obk) changed [some notes into suggestions](https://github.com/rust-lang/rust/pull/42033).
* [@rthomas](https://github.com/rthomas) updated [docs on Error struct](https://github.com/rust-lang/rust/pull/42837).
* [@gaurikholkar](https://github.com/gaurikholkar) reordered [span suggestions to appear below main labels](https://github.com/rust-lang/rust/pull/43251).
* [@Others](https://github.com/Others) improved [panic docs for Instant::duration_since](https://github.com/rust-lang/rust/pull/43256).
* [@tshepang](https://github.com/tshepang) provided [an actual equivalent to filter_map doc](https://github.com/rust-lang/rust/pull/43416).
* [@petrochenkov](https://github.com/petrochenkov) added [an extra note to `late_bound_lifetime_arguments` error/lint](https://github.com/rust-lang/rust/pull/43343).
* [@perryprog](https://github.com/perryprog) made [a less verbose output for unused arguments](https://github.com/rust-lang/rust/pull/43323).
* [@zackmdavis](https://github.com/zackmdavis) made [JSON error byte position start at top of file](https://github.com/rust-lang/rust/pull/42973), made [explanatory error on `--print target-spec-json` without unstable options](https://github.com/rust-lang/rust/pull/43260) and suggested [one-argument enum variant to fix type mismatch when applicable](https://github.com/rust-lang/rust/pull/43178).
* [@Aaronepower](https://github.com/Aaronepower) updated [release notes for 1.19.0](https://github.com/rust-lang/rust/pull/43368).
* [@vbrandl](https://github.com/vbrandl) documented [default values for primitive types](https://github.com/rust-lang/rust/pull/43252).

# Meetings

Next meeting will be on Wednesday 26th of July 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
