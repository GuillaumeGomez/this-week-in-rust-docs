---
layout: post
title: This Week in Rust Docs 87
date: 2018-1-7
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

Happy new year! The last year has been very intense in the Rust documentation world:

 * We improved the documentation search (both display and search itself).
 * We improved the documentation display (it now fully works on mobile devices!).
 * We added more information into the documentation (the crate version, if the return type is implements any of Iterator/Read/Write trait, and a lot more...).
 * We added the possibility to include external files in documentation.
 * We (finally!) started the migration of our markdown renderer from hoedown to pulldown.
 * We added examples to **every** function/methods/types to allow readers to understand more quickly.
 * We added a lint (`missing_docs`) to allow you to never miss an item not being documented.
 * And a lot more of awesome changes!

Maybe a blog post will be wrote to sum all this up, we'll see.

Now time to catch up the two missing weeks!

# Current opened issues

For now, here are the three big issues for Rust documentation:

* [The Standard Library Documentation Checklist](https://github.com/rust-lang/rust/issues/29329)
* [Add error explanations for all error codes](https://github.com/rust-lang/rust/issues/32777)
* [Document all features in the Rust reference](https://github.com/rust-lang-nursery/reference/issues/9)

They all need help to move forward so any contribution is very welcome!

There are currently around 70 other documentation issues opened. Look for [T-doc](https://github.com/rust-lang/rust/labels/T-doc) tagged issues on GitHub!

# Waiting for merge

* [@estebank](https://github.com/estebank) highlighted [code on diagnostics when underlined](https://github.com/rust-lang/rust/pull/45752), suggested [casting on numeric type error](https://github.com/rust-lang/rust/pull/47247), provided [suggestion when trying to use method on numeric literal](https://github.com/rust-lang/rust/pull/47171) and added [a custom error when moving arg outside of its closure](https://github.com/rust-lang/rust/pull/47144).
* [@zackmdavis](https://github.com/zackmdavis) added [type error method suggestions use whitelisted identity-like conversions](https://github.com/rust-lang/rust/pull/46461) and fixed [the doc-comment-decoration-trimming edge-case rustdoc ICE](https://github.com/rust-lang/rust/pull/47210).
* [@SimonSapin](https://github.com/SimonSapin) documented [the size of bool](https://github.com/rust-lang/rust/pull/46156).
* [@partim](https://github.com/partim) improved [documentation for Borrow, AsRef, and friends](https://github.com/rust-lang/rust/pull/46518).
* [@keatinge](https://github.com/keatinge) added [help message for incorrect pattern syntax](https://github.com/rust-lang/rust/pull/47232).
* [@clarcharr](https://github.com/clarcharr) documented [std::os::raw](https://github.com/rust-lang/rust/pull/46962), better [Debug impl for io::Error](https://github.com/rust-lang/rust/pull/47120).
* [@hellow554](https://github.com/hellow554) added [kbd style tag to main.css in rustdoc](https://github.com/rust-lang/rust/pull/46938).
* [@dbrgn](https://github.com/dbrgn) whitelisted [based suggestions](https://github.com/rust-lang/rust/pull/46815).
* [@vramana](https://github.com/vramana) improved [error messages in the case of partial and collateral moves for NLL](https://github.com/rust-lang/rust/pull/47020) and improved [move related error messages](https://github.com/rust-lang/rust/pull/47093).
* [@ollie27](https://github.com/ollie27) added [missing src links for generic impls on trait pages in rustdoc](https://github.com/rust-lang/rust/pull/47039).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) stabilized [allow_fail flag test feature](https://github.com/rust-lang/rust/pull/46501).

# Recent doc contributions

* [@Aaronepower](https://github.com/Aaronepower) updated [RELEASES.md for 1.23.0](https://github.com/rust-lang/rust/pull/46327).
* [@MaloJaffre](https://github.com/MaloJaffre) added [compiler docs testing to CI](https://github.com/rust-lang/rust/pull/46278).
* [@tspiteri](https://github.com/tspiteri) improved [None condition doc for `checked_div` and `checked_rem` in docs](https://github.com/rust-lang/rust/pull/46947).
* [@stjepang](https://github.com/stjepang) wrote [examples for {BTree,Hash}Set::{get,replace,take}](https://github.com/rust-lang/rust/pull/47217).
* [@kennytm](https://github.com/kennytm) added [a tidy check for missing or too many trailing newlines](https://github.com/rust-lang/rust/pull/47064).
* [@SergioBenitez](https://github.com/SergioBenitez) clarified [appending behavior of 'io::Read::read_to_string()'](https://github.com/rust-lang/rust/pull/47216).
* [@frewsxcv](https://github.com/frewsxcv) minor [rewrite of env::current_exe docs; clarified symlinks](https://github.com/rust-lang/rust/pull/46987) and documented [when LineWriter flushes; document errors for into_inner](https://github.com/rust-lang/rust/pull/47145).
* [@ollie27](https://github.com/ollie27) corrected [a few stability attributes](https://github.com/rust-lang/rust/pull/47030).
* [@dzamlo](https://github.com/dzamlo) fixed [an error in std::process documentation](https://github.com/rust-lang/rust/pull/47198).
* [@varkor](https://github.com/varkor) fixed [doc typo for is_ascii_graphic](https://github.com/rust-lang/rust/pull/47079).
* [@Sogomn](https://github.com/Sogomn) defocused [search bar in rustdoc pages](https://github.com/rust-lang/rust/pull/47134).
* [@estebank](https://github.com/estebank) reworded [reason for move note](https://github.com/rust-lang/rust/pull/47124) and reworded [trying to operate in immutable fields](https://github.com/rust-lang/rust/pull/47098).
* [@mark-i-m](https://github.com/mark-i-m) fixed [typo](https://github.com/rust-lang/rust/pull/47107).
* [@fschutt](https://github.com/fschutt) improved [error messages for linking failure](https://github.com/rust-lang/rust/pull/47052).
* [@GuillaumeGomez](https://github.com/GuillaumeGomez) removed [display of hidden types in rustdoc](https://github.com/rust-lang/rust/pull/46359), made [doc search more relevant](https://github.com/rust-lang/rust/pull/46700) and fixed [search bar defocus](https://github.com/rust-lang/rust/pull/47202).

# Meetings

Next meeting will be on Tuesday 9th of January 2018 at 19:00 UTC on #rust-docs channel on irc.mozilla.org. Feel free to come!
