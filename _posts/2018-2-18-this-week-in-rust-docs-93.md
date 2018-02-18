---
layout: post
title: This Week in Rust Docs 93
date: 2018-2-18
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

Hoedown is finally being removed from rustdoc! I'll post the approval message from [@QuietMisdreavus](https://github.com/QuietMisdreavus) in here:

> The preparations are complete. It is time...
>
> _**Begone, demon of the foul C! Your presence is no longer wanted here! With this strike, I commit you to the depths of history, never to torment our fair land again!**_

You can see the pull request [here](https://github.com/rust-lang/rust/pull/48274).

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@estebank](https://github.com/estebank) reworded [E0044 and message for `!Send` types](https://github.com/rust-lang/rust/pull/48138), detected [possibly non-Rust closure syntax during parse](https://github.com/rust-lang/rust/pull/47763), suggested [setting associated type when type argument is given instead](https://github.com/rust-lang/rust/pull/48288) and avoidED [ICE in arg mistmatch error for tuple variants](https://github.com/rust-lang/rust/pull/48246).
* [@partim](https://github.com/partim) improved [documentation for Borrow, AsRef, and friends](https://github.com/rust-lang/rust/pull/46518).
* [@dbrgn](https://github.com/dbrgn) whitelisted [based suggestions](https://github.com/rust-lang/rust/pull/46815).
* [@vi](https://github.com/vi) added [foldable impl blocks in rustdoc](https://github.com/rust-lang/rust/pull/47894).
* [@wesleywiser](https://github.com/wesleywiser) fixed [how paths are printed by error messages during bootstrap](https://github.com/rust-lang/rust/pull/47731).
* [@Aaron1011](https://github.com/Aaron1011) generated [documentation for auto-trait impls](https://github.com/rust-lang/rust/pull/47833).
* [@topecongiro](https://github.com/topecongiro) fixed [span of visibility](https://github.com/rust-lang/rust/pull/47799).
* [@NovemberZulu](https://github.com/NovemberZulu) rephrased [UnsafeCell doc](https://github.com/rust-lang/rust/pull/48201).
* [@csmoe](https://github.com/csmoe) informed [user where to give a type annotation](https://github.com/rust-lang/rust/pull/48198).
* [@frewsxcv](https://github.com/frewsxcv) unified ['Platform-specific behavior' documentation headings](https://github.com/rust-lang/rust/pull/48312), fixed [broken documentation link](https://github.com/rust-lang/rust/pull/48314) and removed [section about compiler-rt in COPYRIGHT](https://github.com/rust-lang/rust/pull/48305).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) moved [manual "extern crate" statements outside automatic "fn main"s in doctests in rustdoc](https://github.com/rust-lang/rust/pull/48106) and added [readme for librustdoc](https://github.com/rust-lang/rust/pull/48283).
* [@alercah](https://github.com/alercah) added [a warning to File about mutability](https://github.com/rust-lang/rust/pull/48273).
* [@matthiaskrgr](https://github.com/matthiaskrgr) fixed [more typos found by codespell](https://github.com/rust-lang/rust/pull/48275).
* [@FraGag](https://github.com/FraGag) improved [documentation of Clone and Copy implementors](https://github.com/rust-lang/rust/pull/48171).
* [@zilbuz](https://github.com/zilbuz) showed [the used type variable when issuing a "can't use type parameters from outer function" error message](https://github.com/rust-lang/rust/pull/47574).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) removed [hoedown from rustdoc](https://github.com/rust-lang/rust/pull/48274) and added [doc test command](https://github.com/rust-lang/rust/pull/48194).

# Recent doc contributions

* [@antoyo](https://github.com/antoyo) greatly improved [primitive docs](https://github.com/rust-lang/rust/pull/48152).
* [@estebank](https://github.com/estebank) added [`-Zteach` documentation](https://github.com/rust-lang/rust/pull/47843).
* [@PramodBisht](https://github.com/PramodBisht) changed [color of struct link from #ff794d to #2dbfb8 for Rust docs](https://github.com/rust-lang/rust/pull/47806).
* [@matthiaskrgr](https://github.com/matthiaskrgr) fixed typo [endianess to endianness (this also changes function names!)](https://github.com/rust-lang/rust/pull/48133).
* [@SergioBenitez](https://github.com/SergioBenitez) clarified [contiguity of Vec's elements](https://github.com/rust-lang/rust/pull/48286).
* [@dns2utf8](https://github.com/dns2utf8) added [link to yield_now](https://github.com/rust-lang/rust/pull/48260).
* [@QuietMisdreavus](https://github.com/QuietMisdreavus) added [unit tests for rustdoc's processing of doctests](https://github.com/rust-lang/rust/pull/48095).
* [@jacob-hughes](https://github.com/jacob-hughes) clarified [why `Sized` bound not implicit on trait's implicit `Self` type](https://github.com/rust-lang/rust/pull/48210).
* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.24.0](https://github.com/rust-lang/rust/pull/47286).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) showed [better warning for trying to cast non-u8 scalar to char](https://github.com/rust-lang/rust/pull/48033), rollup [of 8 pull requests](https://github.com/rust-lang/rust/pull/48294) and fix [condvar example](https://github.com/rust-lang/rust/pull/48239).

# Meetings

Next meeting will be on Tuesday 20th of February 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
