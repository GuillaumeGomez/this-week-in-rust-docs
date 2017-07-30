---
layout: post
title: This Week in Rust Docs 66
date: 2017-7-30
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

* [@RalfJung](https://github.com/RalfJung) clarified [wording for E0122](https://github.com/rust-lang/rust/pull/43176).
* [@xliiv](https://github.com/xliiv) added [simple docs example for struct Cell](https://github.com/rust-lang/rust/pull/43423).
* [@kennytm](https://github.com/kennytm) exposed [all OS-specific modules in libstd doc](https://github.com/rust-lang/rust/pull/43348).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) printed [associated types in traits "implementors" section in rustdoc](https://github.com/rust-lang/rust/pull/43515) and added [documentation for function pointers as a primitive](https://github.com/rust-lang/rust/pull/43529).
* [@Mark-Simulacrum](https://github.com/Mark-Simulacrum) made [rustdoc build only at the topmost stage](https://github.com/rust-lang/rust/pull/43528).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [warnings when rustdoc html rendering differs](https://github.com/rust-lang/rust/pull/41991) and removed [warn on unused field on union](https://github.com/rust-lang/rust/pull/43397).

# Recent doc contributions

* [@oli-obk](https://github.com/oli-obk) adjusted [new suggestions to the suggestion guidelines](https://github.com/rust-lang/rust/pull/43386).
* [@waywardmonkeys](https://github.com/waywardmonkeys) fixed [some doc comment typos](https://github.com/rust-lang/rust/pull/43428).
* [@mandeep](https://github.com/mandeep) added [generic example of std::ops::Sub in doc comments](https://github.com/rust-lang/rust/pull/43413).
* [@stjepang](https://github.com/stjepang) clarified [that sort_unstable is deterministic](https://github.com/rust-lang/rust/pull/43374).
* [@tshepang](https://github.com/tshepang) made [into_iter example more concise](https://github.com/rust-lang/rust/pull/43409).
* [@cuviper](https://github.com/cuviper) corrected [the spelling of "homogeneous"](https://github.com/rust-lang/rust/pull/43401).
* [@s3rvac](https://github.com/s3rvac) added [a missing verb to the description of std::process::ExitStatus::success()](https://github.com/rust-lang/rust/pull/43379).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [[src] links to associated functions inside an impl block in rustdoc](https://github.com/rust-lang/rust/pull/43509) and added [a note to Vec's Extend<&T> impl about its slice specialization](https://github.com/rust-lang/rust/pull/43455).
* [@gaurikholkar](https://github.com/gaurikholkar) changed [E0623 error message - both anonymous lifetime regions](https://github.com/rust-lang/rust/pull/43541) and improved [case with both anonymous lifetime parameters #43269](https://github.com/rust-lang/rust/pull/43298).
* [@pczarn](https://github.com/pczarn) made [the macro parser theory description more accurate](https://github.com/rust-lang/rust/pull/43432).
* [@petrochenkov](https://github.com/petrochenkov) made [better diagnostics and recovery for `mut ref` in patterns](https://github.com/rust-lang/rust/pull/43489).
* [@joshlf](https://github.com/joshlf) fixed [grammar in std::thread::spawn documentation](https://github.com/rust-lang/rust/pull/43456).
* [@ivanbakel](https://github.com/ivanbakel) extended [error message for mut borrow conflicts in loops](https://github.com/rust-lang/rust/pull/43479).
* [@zackmdavis](https://github.com/zackmdavis) made [major section headers self-links in rustdoc](https://github.com/rust-lang/rust/pull/43445), added [unions to whitelist of sidebar types in rustdoc](https://github.com/rust-lang/rust/pull/43446) and fixed [layout of Fields section in documentation for unions](https://github.com/rust-lang/rust/pull/43436).
* [@leshow](https://github.com/leshow) fixed docs: [BufReader/File doesn't need to be mut](https://github.com/rust-lang/rust/pull/43366).
* [@ranweiler](https://github.com/ranweiler) documented [usage of `compiler_builtins` with `no_std` binaries](https://github.com/rust-lang/rust/pull/43342).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) added [lint for when doc comments are added where they're unused](https://github.com/rust-lang/rust/pull/43009).

# Meetings

Next meeting will be on Wednesday 2nd of August 2017 at 20:00 GMT on #rust-docs channel on irc.mozilla.org. Feel free to come!
