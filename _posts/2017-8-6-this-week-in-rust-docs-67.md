---
layout: post
title: This Week in Rust Docs 67
date: 2017-8-6
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

The [rewrite of rustdoc](https://github.com/steveklabnik/rustdoc) is still under heavy development. Don't hesitate to give it a try!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@RalfJung](https://github.com/RalfJung) clarified [wording for E0122](https://github.com/rust-lang/rust/pull/43176).
* [@kennytm](https://github.com/kennytm) exposed [all OS-specific modules in libstd doc](https://github.com/rust-lang/rust/pull/43348).
* [@oli-obk](https://github.com/oli-obk) added [lint casting signed integers smaller than `isize` to raw pointers](https://github.com/rust-lang/rust/pull/43641).
* [@estebank](https://github.com/estebank) pointed [at return type always when type mismatch against it](https://github.com/rust-lang/rust/pull/43484).
* [@Aaronepower](https://github.com/Aaronepower) updated [release notes for 1.20](https://github.com/rust-lang/rust/pull/43627).
* [@ruuda](https://github.com/ruuda) detected [relative urls in tidy check](https://github.com/rust-lang/rust/pull/43632) and pointed ["deref coercions" links to new book](https://github.com/rust-lang/rust/pull/43631).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings when rustdoc html rendering differs](https://github.com/rust-lang/rust/pull/41991), removed [warn on unused field on union](https://github.com/rust-lang/rust/pull/43397), fixed [rustdoc error on '\0'](https://github.com/rust-lang/rust/pull/43691) and added [union and const colors](https://github.com/rust-lang/rust/pull/43558).

# Recent doc contributions

* [@xliiv](https://github.com/xliiv) added [simple docs example for struct Cell](https://github.com/rust-lang/rust/pull/43423).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) printed [associated types in traits "implementors" section in rustdoc](https://github.com/rust-lang/rust/pull/43515), added [documentation for function pointers as a primitive](https://github.com/rust-lang/rust/pull/43529), added [[src] links to associated functions inside an impl block in rustdoc](https://github.com/rust-lang/rust/pull/43509), shrank [headings in non-top-level docblocks in rustdoc](https://github.com/rust-lang/rust/pull/43602) and added [docs for references as a primitive](https://github.com/rust-lang/rust/pull/43560).
* [@edaniels](https://github.com/edaniels) fixed [typo in coerce_forced_unit docstring](https://github.com/rust-lang/rust/pull/43689).
* [@frewsxcv](https://github.com/frewsxcv) improved [string slice doc](https://github.com/rust-lang/rust/pull/43652), fixed and improved [thread docs](https://github.com/rust-lang/rust/pull/43619) and improved [docs & doc examples for HashSet](https://github.com/rust-lang/rust/pull/43585).
* [@oli-obk](https://github.com/oli-obk) uplifted [some comments to Doc comments](https://github.com/rust-lang/rust/pull/43640).
* [@zackmdavis](https://github.com/zackmdavis) improved [field does not exist error: note fields if Levenshtein suggestion fails](https://github.com/rust-lang/rust/pull/43442) and added [a couple more error explanations for posterity](https://github.com/rust-lang/rust/pull/43519).
* [@SimonSapin](https://github.com/SimonSapin) updated [nomicon](https://github.com/rust-lang/rust/pull/43618).
* [@tshepang](https://github.com/tshepang) made [into_iter doc example more concise](https://github.com/rust-lang/rust/pull/43409).
* [@tbu-](https://github.com/tbu-) documented [the `from_str_radix` panic](https://github.com/rust-lang/rust/pull/43563).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) throw [errors when doc comments are added where they're unused](https://github.com/rust-lang/rust/pull/43009).

# Meetings

Next meeting will be on Wednesday 9th of August 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
